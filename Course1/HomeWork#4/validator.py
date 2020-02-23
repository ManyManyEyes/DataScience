import re


def redactor(line):
    return re.split(r'[\n\t;-]+', line)


def validator(userlist, pointer_line):
    if not re.match('^[1-9][0-9]*$', userlist[pointer_line.index('id')]):
        userlist[0] = str(None)
    if not re.match('^[A-Z|a-z][a-z]+$', userlist[pointer_line.index('name')]):
        userlist[1] = str(None)
    if not re.match('^[1-9][0-9]*$', userlist[pointer_line.index('age')]):
        userlist[2] = str(None)
    if not re.match('^[+]*[0-9]{0,11}$', userlist[pointer_line.index('phone')]):
        userlist[3] = str(None)
    if not re.match('^[a-z0-9]+@[a-z]+.[a-z]+$', userlist[pointer_line.index('email')].lower()):
        userlist[4] = str(None)
    if not re.match('^(admin|user|guest)$', userlist[pointer_line.index('role')]):
        userlist[5] = str(None)
    if not re.match('^(active|inactive)$', userlist[pointer_line.index('status')]):
        userlist[6] = str(None)


def constructor(keys_line, line):
    return {keys_line[0]: line[0],
            keys_line[1]: line[1],
            keys_line[2]: line[2],
            keys_line[3]: line[3],
            keys_line[4]: line[4],
            keys_line[5]: line[5],
            keys_line[6]: line[6]}


if __name__ == "__main__":
    with open("data.txt", "r") as data:
        raw_line = data.readline()
        pointer_line = redactor(raw_line.strip())
        persons = []
        for line in data:
            line = redactor(line)
            validator(line, pointer_line)
            person = constructor(pointer_line, line)
            persons.append(person)
        print(persons)
