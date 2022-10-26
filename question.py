# from ctypes.wintypes import HGDIOBJ
# from sys import UnraisableHookArgs
# from telnetlib import VT3270REGIME
from termios import NL1
import requests
import random

urlNS = "https://opentdb.com/api.php?amount=50&category=17&difficulty=medium&type=multiple"
payloadNS ={}
headersNS = {}
NS = requests.request("GET", urlNS, headers=headersNS, data=payloadNS)


urlVG = "https://opentdb.com/api.php?amount=50&category=15&difficulty=medium&type=multiple"
payloadVG = {}
headersVG = {}
VG = requests.request("GET", urlVG, headers=headersVG, data=payloadVG)

urlG = "https://opentdb.com/api.php?amount=25&category=22&difficulty=medium&type=multiple"
payloadG ={}
headersG = {}
G = requests.request("GET", urlG, headers=headersG, data=payloadG)

urlH = "https://opentdb.com/api.php?amount=25&category=23&difficulty=medium&type=multiple"
payloadH ={}
headersH = {}
H = requests.request("GET", urlH, headers=headersH, data=payloadH)

urlGK = "https://opentdb.com/api.php?amount=50&category=9&difficulty=hard&type=multiple"
payloadGK ={}
headersGK = {}
GK = requests.request("GET", urlGK, headers=headersGK, data=payloadGK)


ind = input("What category are you in?\n1) Natural Science\n2} Video Games\n3) History and Geography\n4) General Knowledge\n")
match ind:
    case "1":
        category = NS
    case "2":
        category = VG 
    case "3":
        horg = random.randint(0,1)
        match horg:
            case 0:
                category = H
            case 1:
                category = G
    case "4":
        category = GK

def getQuestion(category):
    questionNum = random.randint(0, len(category.json()["results"])-1)
    question = category.json()["results"][questionNum]["question"]
    correct_string = category.json()["results"][questionNum]["correct_answer"]
    options = category.json()["results"][questionNum]["incorrect_answers"]
    correct_answer_index = random.randint(0,3)
    options.insert(correct_answer_index, correct_string)
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
    if player_answer_index == correct_answer_index:
        print("Correct")
    else:
        print("Incorrect")
        print("Correct Answer: " + correct_string)



getQuestion(category)
