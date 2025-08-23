import json
import os

FILENAME = 'Flashcards.json'


def addFlashCards():
    print("you're on add flash card section")
    options = int(input("1.Add Flash Card\n2.Return to menu\n"))

    if options == 1:
        addQuestion = input("Please input the question: ")
        addAnswer = input("Please input the answer: ")

        if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
            data = []

        else:
            with open(FILENAME, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        if data:
            newId = data[-1]["ID"] + 1
        else:
            newId = 1

        flascards = {
            "ID": newId,
            "Question": addQuestion,
            "Answer": addAnswer
        }

        data.append(flascards)

        with open(FILENAME, "w") as file:
            json.dump(data, file, indent=4)

        print(f"Flash card {newId} added successfully!")

    elif options == 2:
        return
    else:
        print("Invalid Option")
        return


def reviewFlashCards():
    print("you're on review flash card section")


def takeQuiz():
    print("you're on quiz flash card section")


def deleteFlashCards():
    print("you're on delete flash card section")


def menu():
    print("Welcome to Flash Quiz, ready to learn?")
    while True:

        navigationOptions = int(input(
            "1.Add Flash Card\n2.Review Flashcards\n3.Take a Quiz\n4.Delete Flashcards\n"))

        if navigationOptions == 1:
            addFlashCards()
        elif navigationOptions == 2:
            reviewFlashCards()
        elif navigationOptions == 3:
            takeQuiz()
        elif navigationOptions == 4:
            deleteFlashCards()
        else:
            print("Invalid Input")
            continue

        if not navigationOptions:
            break


menu()
