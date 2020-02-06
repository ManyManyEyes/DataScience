import re


def redactor(line):
    return line.replace("\t", ",")\
        .replace(";", ",")\
        .replace("-", ",")\
        .replace(",,", ",")\
        .split(",")


def validator_id(userlist):
    if not re.match('^[1-9][0-9]*$', userlist[0]):
        userlist[0] = str(None)
def validator_name(userlist):
    if not re.match('^[A-Z|a-z][a-z]+$', userlist[1]):
        userlist[1] = str(None)
def validator_age(userlist):        
    if not re.match('^[1-9][0-9]*$', userlist[2]):
        userlist[2] = str(None)
def validator_phone(userlist):
    if not re.match('^[+]*[0-9]{0,11}$', userlist[3]):
        userlist[3] = str(None)
def validator_mail(userlist):
    if not re.match('^[a-z0-9]+@[a-z]+.[a-z]+$', userlist[4].lower()):
        userlist[4] = str(None)
def validator_role(userlist):
    if not re.match('^(admin|user|guest)$', userlist[5]):
        userlist[5] = str(None)
def validator_status(userlist):
    if not re.match('^(active|inactive)$', userlist[6]):
        userlist[6] = str(None)


def constructor(keys_line, line):
    return {keys_line[0]:line[0],
            keys_line[1]:line[1],
            keys_line[2]:line[2],
            keys_line[3]:line[3],
            keys_line[4]:line[4],
            keys_line[5]:line[5],
            keys_line[6]:line[6]}


if __name__ == "__main__":
    with open("data.txt", "r") as data:
        pointer_line = data.readline()
        pointer_line = redactor(pointer_line.strip())
        persons = []
        for line in data:
            line = redactor(line)
            validator_id(line)
            validator_name(line)
            validator_age(line)
            validator_phone(line)
            validator_mail(line)
            validator_role(line)
            validator_status(line)
            person = constructor(pointer_line, line)
            persons.append(person)
        print(persons)
