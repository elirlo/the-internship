from ctypes.wintypes import HGDIOBJ
from sys import UnraisableHookArgs
from telnetlib import VT3270REGIME
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
GK = requests.request("GET", urlGK, headers3=headersGK, data=payloadGK)

numQuestions = {"NS" : 49, "VG" : 49,"G": 24,"H": 24,"GK": 49}

ind = input("What category are you in?\n1) Natural Science\n2} Video Games\n3) History and Geography\n4) General Knowledge")
match ind:
    case 1:
        category = NS
    case 2:
        category = VG 
    case 3:
        horg = random.randint(0,1)
        match horg:
            case 0:
                category = H
            case 1:
                category = G
    case 4:
        category = GK

def getQuestion(category, numQuestions):
    questionNum = random.randint(0,numQuestions)
    question = category.json()["results"][questionNum]["question"]
    correct = category.json()["results"][questionNum]["correct_answer"]
    options = category.json()["results"][questionNum]["incorrect_answers"]
    ind = random.randint(0,4)
    options.insert(ind, correct)
    print(question)
    print(options)

getQuestion()
