from backend.ingredientClassifier import ingredientClassifier

classifier = ingredientClassifier('second_model.h5')
print(classifier._id_image(r"validating_my_model_images\Apple\apple.jpg"))