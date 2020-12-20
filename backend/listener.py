import pyrebase
import os
from keras.preprocessing.image import img_to_array, load_img
from shutil import copyfile
import numpy as np
import pyrebase
import time
from ingredientClassifier import ingredientClassifier
import json


def is_new_img(fpath):
    if 'old_img.jpg' not in os.listdir(os.curdir):
        print('old_not_found')
        copyfile(fpath, 'old_img.jpg')

    recent_dwnld = img_to_array(load_img(fpath))
    old_copy = img_to_array(load_img('old_img.jpg'))
    if recent_dwnld.shape == old_copy.shape:
        is_new = np.subtract(recent_dwnld, old_copy).mean() != 0
    else:
        is_new = True
    if is_new:
        # copyfile(fpath, 'old_img.jpg')
        pass

    return is_new


config = {
    "apiKey": "AIzaSyBBqcAa_lefYrflv-O6uhBCz0si9WL8nq0",
    "authDomain": "epicer-9caf5.firebaseapp.com",
    "databaseURL":"https://epicer-9caf5.firebaseio.com/",
    "projectId": "epicer-9caf5",
    "storageBucket": "epicer-9caf5.appspot.com",
    "messagingSenderId": "1011104234229",
    "appId": "1:1011104234229:web:f6934c06f47b9ee86163bc",
    "measurementId": "G-HCRW078NJ9"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
path_on_cloud = "images/foo.png" # Image Classification file

classifier = ingredientClassifier('second_model.h5')

while True:
    # storage.child(path_on_cloud).download("recent_image.png")
    if is_new_img("recent_image.png"):
        with open('result.json', 'w') as f:
            json.dump(classifier.urls_from_image("recent_image.png"), f)
        storage.child("images/result.json").put('result.json')

    else:
        time.sleep(10)
        print('Starting next check...')