#!/usr/bin/env python3
import csv
from random import randint

with open("goodmorning.csv", newline="") as csvfile:
    morns = csv.DictReader(csvfile, delimiter=",")
    iterator = 0
    randomLang = randint(1, 271)
    for row in morns:
        iterator = iterator + 1
        if iterator == randomLang:
            print(row["Language"], ": \n", row["Morning greetings"], "\n\n")
