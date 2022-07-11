import csv
from time import sleep
from time import time
from textos import embelezeTempo as eT
import requests

API = "https://www.speedrun.com/api/v1/"

def anyRequests(text):
    while True:
        try:
            return requests.get(text).json()
        except:
            print("connection")

def compare(a,b):
    global ALPHA
    a = a[0].lower()
    if b not in ALPHA:
        print(b)
        return 'inconclusive'
    if ALPHA.index(a) > ALPHA.index(b):
        return "greater"
    elif ALPHA.index(a) < ALPHA.index(b):
        return "less"
    return "equal"

def find(term):
    initiator = [0,1200000]
    while abs(initiator[1]-initiator[0]) > 200:
        value = (initiator[0]+initiator[1])//2
        print(value)
        person = anyRequests(f"{API}users?name={term}&max=1&offset={value}&order=asc")['data']
        if person:
            person = person[0]['names']['international']
            if compare(person,term) == "less":
                initiator[0] = value
            else:
                initiator[1] = value
        else:
            initiator[1] = value
    return initiator[0]

allIDS = set()
with open("allRunners.csv",'r',newline = "") as file:
    reader = csv.reader(file,delimiter = ";")
    for i in reader:
        allIDS.add(i[0])
ALPHA = ['_','-','+','.','|','@', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
offsets = [0,0,-1,0,0,0,0,400,800,1000,1000,800,800,1000,1000,1400,7200,12000,28000,49200,147800]
for letter in ALPHA:
    if letter == '+':
        continue
    if ALPHA.index(letter) < len(offsets):
        offset = offsets[ALPHA.index(letter)]
    else:
        offset = find(letter)
    foundFirst = False
    while True:
        print(offset)
        people = anyRequests(f"{API}users?name={letter}&max=200&offset={offset}&order=asc")
        if 'data' not in people:
            break
        for person in people['data']:
            name = person['names']['international'].lower()
            if not foundFirst:
                if name[0] == letter:
                    foundFirst = True
                else:
                    continue
            allIDS.add(person['id'])
            if name[0] != letter:
                people['data'].pop(0)
                break
        if len(people['data'])<200:
            break
        offset += 200
with open("allRunners.csv",'a',newline = "") as file:
    writer = csv.writer(file,delimiter = ";")
    for ID in allIDS:
        writer.writerow([ID])
