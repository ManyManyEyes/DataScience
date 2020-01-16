import os
import re


with open("data.txt","r") as data:
    for line in data:
        line = line.replace(".", "")
        line = line.replace(",", "")
        line = line.lower()
        while "  " in line:
            line = line.replace("  ", " ")
        with open ("data_new.txt", "w") as data_new:
            data_new.writelines(line+'\n')
        print(line)
print("Done!")

