import os
import re

with open("data_new.txt", "w"): pass
with open("data.txt","r") as data:
    for line in data:
        line = line.replace(".", "")
        line = line.replace(",", "")
        line = line.lower()
        while "  " in line:
            line = line.replace("  ", " ")
        with open ("data_new.txt", "a") as data_new:
            data_new.write(line)

