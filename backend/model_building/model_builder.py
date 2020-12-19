# Dataset attributed to the fine work of https://github.com/marcusklasson/GroceryStoreDataset

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras import Sequential
from keras import models
from keras import layers
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

batch_size = 16

model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(358, 358, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])


train_generator = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest').flow_from_directory(r'data\train', batch_size=batch_size,
                                                 class_mode='binary', target_size=(358, 358))

test_generator = ImageDataGenerator().flow_from_directory(
                                                 r'data\test', target_size=(358, 358),
                                                 batch_size=batch_size, class_mode='binary')

model.fit_generator(
        train_generator,
        steps_per_epoch=2000 // batch_size,
        epochs=30,
        validation_data=test_generator,
        validation_steps=800 // batch_size,
        verbose=2
)

model.save('new_model.h5')
