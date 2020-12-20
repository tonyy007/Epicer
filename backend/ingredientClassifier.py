import keras
from keras.preprocessing.image import img_to_array, load_img
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
        self.cached_ingredients = ['egg', 'oats', 'flour']
        # above line is within class definition for demo purposes

    def add_to_cache(self, ingredient):
        if ingredient.lower() not in self.cached_ingredients:
            self.cached_ingredients += [ingredient.lower()]

    def clear_cache(self):
        self.cached_ingredients = []

    def remove_ingredient_from_cache(self, target):
        for index, ingredient in enumerate(self.cached_ingredients):
            if ingredient == target:
                del self.cached_ingredients[index]

    def urls_from_image(self, fpath):  # fpath: filepath of image to be classified by CNN -> JSON object
        prediction = self._id_image(fpath)
        self.add_to_cache(prediction)

        return self._query_cached_items()

    # urls_from_list(ingredients: String[], save_to_cache: Boolean) -> JSON object
    def urls_from_list(self, ingredients, save_to_cache=True):
        if save_to_cache:
            for ingredient in ingredients:
                self.add_to_cache(ingredient)

        return self._query_cached_items(ingredients)

    # _id_image(fpath: String) -> String
    def _id_image(self, fpath):
        img = load_img(
            fpath,
            target_size=(358, 358)
        )

        x = img_to_array(img)
        x = x.reshape((1,) + x.shape) # shape: (358, 358, 1)

        numerical_prediction = self.model.predict(x)[0][0]
        prediction = 'Apple' if numerical_prediction < 0.5 else 'Milk'
        return prediction

    # _query_cached_items(**additional_ingredients: String[]) -> JSON object
    def _query_cached_items(self, additional_ingredients=None):
        ingredients = self.cached_ingredients
        if additional_ingredients is not None:
            for ingredient in ingredients:
                self.add_to_cache(ingredient)

        r = requests.get('https://www.bigoven.com/recipes/search?include_ing=' + str(reduce(lambda x, acc: x + "%2C" + acc, ingredients, '')[3:]))
        hacky_html_decode = [item.split('<a href="')[1].split('</a>')[0] for item in r.content.decode('utf8').split('<div class="recipe-tile-full')[1:]]

        recipes = {}

        # {
        #   "result0": {
        #                "url": String,
        #                "title": String
        #               }, ... }

        for index, item in enumerate(hacky_html_decode):
            url = item.split('">')[0]
            title = item.split('alt="')[1].split('"/>')[0]

            recipes[f'result{index}'] = {"url": url,
                                         "title": title}

        return json.dumps(recipes)
