import os
import re


def redactor_1(line):
    return line.replace(".", "").replace(",", "")


def redactor_2(line):
    return line.lower()


def redactor_3(line):
    return line.replace("  ", " ")


if __name__ == "__main__":
    with open("data_new.txt", "w"): pass
    with open("data.txt","r") as data, open ("data_new.txt", "a") as data_new:
        for line in data:
            data_new.write(redactor_3(redactor_2(redactor_1(line))))
            
