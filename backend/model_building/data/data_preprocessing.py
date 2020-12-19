import os

paths = [
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/val/Potato',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/val/Tomato',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/train/Apple',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/train/Milk',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/train/Potato',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/train/Tomato',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/test/Apple',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/test/Milk',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/test/Potato',
    'C:/Users/Walker Sorensen/PycharmProjects/hackUmass2020/data/test/Tomato'
]

for path in paths:
    for index, file in enumerate(os.listdir(path)):
        os.rename(path + '/' + file, path + '/' + str(index) + '.jpg')
