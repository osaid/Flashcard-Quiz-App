import os
import json

FILENAME = 'Flashcards.json'


def addFlashcardsloadJson():

    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        data = []
    else:
        with open(FILENAME, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    return data


def loadJson():

    if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
        print("Your deck is empty, please first create a flash card!")
        data = []

    else:
        with open(FILENAME, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    return data
