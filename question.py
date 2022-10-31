import requests
import random
import html

urlNS = (
    "https://opentdb.com/api.php?amount=50&category=17&difficulty=medium&type=multiple"
)

NS = requests.get(urlNS)


urlVG = (
    "https://opentdb.com/api.php?amount=50&category=15&difficulty=medium&type=multiple"
)
VG = requests.get(urlVG)

urlG = (
    "https://opentdb.com/api.php?amount=25&category=22&difficulty=medium&type=multiple"
)
G = requests.get(urlG)

urlH = (
    "https://opentdb.com/api.php?amount=25&category=23&difficulty=medium&type=multiple"
)
H = requests.get(urlH)

urlGK = "https://opentdb.com/api.php?amount=50&category=9&difficulty=hard&type=multiple"
GK = requests.get(urlGK)


def createList(r1, r2):
    return list(range(r1, r2 + 1))


available_questions = {
    "NS": createList(0, 49),
    "VG": createList(0, 49),
    "G": createList(0, 24),
    "H": createList(0, 24),
    "GK": createList(0, 49),
}


def getQuestion(category, category_name):
    questionNum = random.choice(available_questions[category_name])
    question = category.json()["results"][questionNum]["question"]
    correct_string = category.json()["results"][questionNum]["correct_answer"]
    options = category.json()["results"][questionNum]["incorrect_answers"]
    correct_answer_index = random.randint(0, 3)
    options.insert(correct_answer_index, correct_string)

    for i in range(4):
        options[i] = html.unescape(options[i])

    question = html.unescape(question)

    print("\n")
    print(question)
    print(options)

    player_answer = input("Type A,B,C,D for your corresponding answer\n")
    player_answer = player_answer.lower()

    match player_answer:
        case "a":
            player_answer_index = 0
        case "b":
            player_answer_index = 1
        case "c":
            player_answer_index = 2
        case "d":
            player_answer_index = 3

    print("\n")

    if player_answer_index == correct_answer_index:
        print("    ****Correct****    ")
    else:
        print("    ****Incorrect****    ")
        print("Correct Answer: " + correct_string)

    print("\n")

    available_questions[category_name].remove(questionNum)


game = True

while game:
    ind = input(
        "What category are you in?\n1) Natural Science\n2} Video Games\n3) History and Geography\n4) General Knowledge\n"
    )
    match ind:
        case "1":
            category = NS
            category_name = "NS"
        case "2":
            category = VG
            category_name = "VG"
        case "3":
            horg = random.randint(0, 1)
            match horg:
                case 0:
                    category = H
                    category_name = "H"
                case 1:
                    category = G
                    category_name = "G"
        case "4":
            category = GK
            category_name = "GK"

    getQuestion(category, category_name)
