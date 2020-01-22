import os
import re

def redactor_1(line):
    line = line.replace(".", "")
    line = line.replace(".", "")
    return line

def redactor_2(line):
    line = line.lower()
    return line

def redactor_3(line):
    line = line.replace("  ", " ")
    return line

if __name__ == "__main__":
    with open("data_new.txt", "w"): pass
    with open("data.txt","r") as data, open ("data_new.txt", "a") as data_new:
        for line in data:
            line = redactor_1(line)
            line = redactor_2(line)
            line = redactor_3(line)
            data_new.write(line)

