import keras
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import requests
import json
from functools import reduce


import tensorflow as tf
config = tf.compat.v1.ConfigProto(gpu_options =
                         tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8)
)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
tf.compat.v1.keras.backend.set_session(session)


class ingredientClassifier:
    def __init__(self, model_fpath):
        self.model = keras.models.load_model(model_fpath)
        # self.cached_ingredients = ['egg', 'rice', 'cinnamon', 'flour', 'yeast']
        self.cached_ingredients = ["potato", "apple"]

    def _id_image(self, fpath): # _id_image(fpath: String) -> String
        img = load_img(
            fpath,
            target_size=(358, 358)
                       )
        x = img_to_array(img)

        x = x.reshape((1,) + x.shape) # shape: (358, 358, 1)

        numerical_prediction = self.model.predict(x)[0][0]
        prediction = 'Apple' if numerical_prediction < 0.5 else 'Milk'
        return prediction

    def _query_items(self, items):

        rs = requests.Session()

        cookie_dict = {
            "__utma": "244331399.879364731.1608351112.1608351112.1608389028.2",
            "__utmc" : "244331399",
            "__utmz": "244331399.1608389028.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
            "_ga": "GA1.2.879364731.1608351112",
            "_gid": "GA1.2.1748242046.1608389387",
            "__atuvc": "10%7C51",
            "category_select": "Type%20them",
            "__utmt": "1",
            "myIngredients": str(reduce(lambda x, acc: x + "%2C" + acc, items, '')[3:]),
            "__utmb": "244331399.15.10.1608389028"
        }

        for cookie in cookie_dict:
            rs.cookies.set(cookie, cookie_dict[cookie])

        print(rs.headers)
        r = rs.post('https://www.supercook.com/dyn/results', cookies=cookie_dict)

        print(r.headers)

        data = json.loads(r.content)
        items = []
        for item in data['results']:
            items.append(item)
            print(item['hash'], item['title'])

        return items


classifier = ingredientClassifier('second_model.h5')
classifier._query_items(classifier.cached_ingredients)