import time
import operator
import random

fault = 0
creature = ["mortal", "human", "worm", "weakling", "creature"]


def invalid_command():
    global fault
    fault += 1
    message = f"I don't understand you, {random.choice(creature)}. But I'm giving you another chance."
    if fault < 3:
        print(message)
    elif fault == 3:
        print(message + " Don't try your luck.")
    elif fault == 5:
        print(message + " Our game is dragging on.")
    elif fault == 7:
        print("I'M ANGRY!")
        time.sleep(1)
        for i in range(10):
            print(get_operator(random.randint(0, 666), random.randint(0, 666), "+"))
        time.sleep(1)
        print(f"You've had enough, {random.choice(creature)}")
        fault = 0


def get_operator(number_1, number_2, operation):
    try:
        return {
            '+': operator.add(number_1, number_2),
            '-': operator.sub(number_1, number_2),
            '*': operator.mul(number_1, number_2),
            '/': operator.truediv(number_1, number_2),
            '%': operator.mod(number_1, number_2),
            '**': operator.pow(number_1, number_2),
            '//': operator.floordiv(number_1, number_2)
        }[operation]

    except ZeroDivisionError:
        print(f"Even my powers are not enough to divide by 0, {random.choice(creature)}")
    except KeyError:
        invalid_command()


def calc(answer):
    global fault
    if answer.upper() == "Y":
        try:
            number_1, number_2 = int(input(f"Enter first number,{random.choice(creature)} ")), int(
                input(f"Enter second number,{random.choice(creature)} "))
            operation = input("Choose operation: +, -, *, /, %, **, //. And then hope to get out of here alive. ")
            result = get_operator(number_1, number_2, operation)
            if result is not None:
                print(f"BEHOLD MY POWER!\n{number_1} {operation} {number_2} = {result}")
                fault = 0

        except ValueError:
            invalid_command()

    elif answer.upper() == "N":
        print("You underestimate my POWER!")
        time.sleep(3)
        exit()

    elif answer.upper != "N" or "Y":
        invalid_command()


answer = str(input(f"Hi {random.choice(creature)}!Do you want to see my GREAT power of my GREAT calculation?(Y/N) "))
calc(answer)
while True:
    answer_again = str(input("Do you want to see my GREAT power again?(Y/N) "))
    calc(answer_again)
