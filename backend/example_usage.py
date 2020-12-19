from backend.ingredientClassifier import ingredientClassifier

classifier = ingredientClassifier('second_model.h5')  # <- This file is where our keras model is stored

# A classifier object has a 'cached_ingredients' field, which is mostly internally managed, however, could be modified if necessary
print('Cached Ingredients ' + str(classifier.cached_ingredients))

# The goals of this object is to handle queries, and do image processing. Let's do a basic String query
incoming_ingredients = ['Milk', 'Potato', 'Vinegar']
print(str(incoming_ingredients) + ' will be added to ' + str(classifier.cached_ingredients))
print('json object: ' + str(classifier.urls_from_list(incoming_ingredients)))  # classifier defaults to save incoming new ingredients to the cache
print("Here's the cache now!: " + str(classifier.cached_ingredients))

# We can prevent things from being added to the cache like so:
incoming_ingredients = ['Sardines']
classifier.urls_from_list(incoming_ingredients, save_to_cache=False)
print('Look at the lack of sardines!: ' + str(classifier.cached_ingredients))

# Here's how image classification works:
image_filepath = r'validating_my_model_images/Apple/apple.jpg'
print("Look at these goods! " + str(classifier.urls_from_image(image_filepath)))
print("And that ingredient was saved to the cache (should be an apple): " + str(classifier.cached_ingredients))

image_filepath = r'validating_my_model_images/Apple/apple2.jpg'
print(str(classifier.urls_from_image(image_filepath)))
print(str(classifier.cached_ingredients))  # note that duplicate entries are avoided, and everything is stored in lower case
