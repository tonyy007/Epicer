import keras
from keras.preprocessing.image import ImageDataGenerator

model = keras.models.load_model(r'second_model.h5')

generator = ImageDataGenerator().flow_from_directory(r'C:\Users\Walker Sorensen\PycharmProjects\hackUmass2020\backend\validating_my_model_images',
                                                     target_size=(358, 358), class_mode='binary', batch_size=1, shuffle=False)

filenames = generator.filenames
nb_samples = len(filenames)

predict = model.predict_generator(generator, steps = nb_samples)
print(predict)
