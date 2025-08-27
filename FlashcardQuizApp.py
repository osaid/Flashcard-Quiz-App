import json
import os
import random


FILENAME = 'Flashcards.json'
STATS_FILE = 'Stats.json'


def addFlashCards():
    print("you're on add flash card section")
    while True:
        try:
            options = int(input("1.Add Flash Card\n2.Return to menu\n"))

            if options == 1:
                addQuestion = input("Please input the question: ")
                addAnswer = input("Please input the answer: ")
                addCategory = input("Please input the category: ")

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
                    "Answer": addAnswer,
                    "Category": addCategory
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
        except ValueError:
            print("Invalid input! Please enter a number.")


def reviewFlashCards():
    print("you're on review flash card section")
    while True:
        try:
            options = int(input("1.Review Flash Cards\n2.Return to menu\n"))

            if options == 1:

                if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
                    print("Your deck is empty, please first create a flash card!")
                    data = []

                else:
                    with open(FILENAME, "r") as file:
                        try:
                            data = json.load(file)
                        except json.JSONDecodeError:
                            data = []

                if not data:
                    print("No flash cards found.")
                else:
                    for card in data:
                        print(
                            f"ID: {card['ID']} | Q: {card['Question']} | A: {card['Answer']} | C: {card['Category']} ")

            elif options == 2:
                return

            else:
                print("Invalid option")
                return
        except ValueError:
            print("Invalid input! Please enter a number.")


def takeQuiz():
    print("you're on quiz flash card section")
    while True:
        try:
            options = int(input("1.Quiz Flash Cards\n2.Return to menu\n"))
            if options == 1:
                if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
                    print("Your deck is empty, please first create a flash card!")
                    data = []
                else:
                    with open(FILENAME, "r") as file:
                        try:
                            data = json.load(file)
                        except json.JSONDecodeError:
                            data = []

                score = 0
                if not data:
                    print("No flash cards found.")
                else:
                    categories = {}
                    cat_id = 1
                    for card in data:
                        if card['Category'] not in categories.values():
                            categories[cat_id] = card['Category']
                            cat_id += 1

                    print("Category List:")
                    for cid, cname in categories.items():
                        print(f"   {cid}. {cname}")

                    categorySelection = int(input(
                        "Please select the number of the category you'd like to quiz or enter 0 to quiz on all flashcards\n"))

                    if categorySelection == 0:
                        random.shuffle(data)
                        for card in data:
                            questionAnswer = input(f"{card['Question']} ")
                            if questionAnswer.strip().lower() == card['Answer'].strip().lower():
                                print("Correct")
                                score += 1
                                print(f"Current score: {score}")
                            else:
                                print("Incorrect")
                                print(f"Current score: {score}")
                                print(f"Correct answer: {card['Answer']}")

                        print(f"You scored {score} out of {len(data)}")
                        print(f"Accuracy: {score/len(data)*100} %")

                    else:
                        selectedCategory = categories.get(categorySelection)
                        quizCards = [
                            c for c in data if c["Category"] == selectedCategory]

                        random.shuffle(quizCards)
                        for card in quizCards:
                            questionAnswer = input(f"{card['Question']} ")
                            if questionAnswer.strip().lower() == card['Answer'].strip().lower():
                                print("Correct")
                                score += 1
                                print(f"Current score: {score}")
                            else:
                                print("Incorrect")
                                print(f"Current score: {score}")
                                print(f"Correct answer: {card['Answer']}")

                        print(f"You scored {score} out of {len(quizCards)}")
                        print(f"Accuracy: {score/len(quizCards)*100} %")
                        accuracy = score/len(quizCards) * 100
                        updateStats(accuracy)

            elif options == 2:
                return
            else:
                print("Invalid option")
                return

        except ValueError:
            print("Invalid input! Please enter a number.")


def deleteFlashCards():
    print("you're on delete flash card section")
    options = int(input("1.Delete Flash Cards\n2.Return to menu\n"))

    if options == 1:
        if not os.path.exists(FILENAME) or os.stat(FILENAME).st_size == 0:
            print(
                "Your deck is empty, please first create a flash card before deleting.")
            data = []

        else:
            with open(FILENAME, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []

        for card in data:
            print(
                f"ID: {card['ID']} | Q: {card['Question']} | A: {card['Answer']} | C: {card['Category']} ")

        deleteSelection = (input(
            "Please enter the flash card ID's you'd like to delete separated by commas e.g. 1,2,3: "))
        deleteSelection = [x.strip() for x in deleteSelection.split(",")]

        cardsKeep = []
        cardsDelete = []

        if not data:
            print("No flash cards found.")
        else:
            for card in data:
                if str(card["ID"]) in deleteSelection:
                    cardsDelete.append(card)
                else:
                    cardsKeep.append(card)

        with open(FILENAME, "w") as file:
            for i, card in enumerate(cardsKeep, start=1):
                card["ID"] = i
            data = json.dump(cardsKeep, file, indent=4)
            print(
                f"Deleted {len(cardsDelete)} flashcards successfully!")


def viewStats():
    while True:
        try:
            statsOptions = int(input("1.View Stats\n2.Return to menu\n"))
            if statsOptions == 1:
                if not os.path.exists(STATS_FILE) or os.stat(STATS_FILE).st_size == 0:
                    print("No stats found, please complete a quiz to view stats")
                    continue

                with open(STATS_FILE, "r") as file:
                    try:
                        stats = json.load(file)
                    except json.JSONDecodeError:
                        print("No stats found")
                        continue
                print(
                    f"Total Attempts: {stats['Attempts']} Average Accuracy: {stats['AverageAccuracy']: .2f} % \n")
            elif statsOptions == 2:
                return
            else:
                print("Invalid option")
                return
        except ValueError:
            print("Invalid input! Please enter a number.")


def updateStats(accuracy):
    if not os.path.exists(STATS_FILE) or os.stat(STATS_FILE).st_size == 0:
        stats = {"Attempts": 0, "TotalAccuracy": 0}
    else:
        with open(STATS_FILE, "r") as file:
            try:
                stats = json.load(file)
            except json.JSONDecodeError:
                stats = {"Attempts": 0, "TotalAccuracy": 0}

    stats["Attempts"] += 1
    stats["TotalAccuracy"] += accuracy  # accumulate
    stats["AverageAccuracy"] = stats["TotalAccuracy"] / stats["Attempts"]

    with open(STATS_FILE, "w") as file:
        json.dump(stats, file, indent=4)

    # print(f"Updated Stats: {stats}")


def menu():
    print("Welcome to Flash Quiz, ready to learn?")
    while True:
        try:
            navigationOptions = int(input(
                "1.Add Flash Card\n2.Review Flashcards\n3.Take a Quiz\n4.Delete Flashcards\n5.View your stats\n6.Exit\n"))

            if navigationOptions == 1:
                addFlashCards()
            elif navigationOptions == 2:
                reviewFlashCards()
            elif navigationOptions == 3:
                takeQuiz()
            elif navigationOptions == 4:
                deleteFlashCards()
            elif navigationOptions == 5:
                viewStats()
            elif navigationOptions == 6:
                exit()
            else:
                print("Invalid Input")
                continue

            if not navigationOptions:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")


menu()
