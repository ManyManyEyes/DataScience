import time
import operator


def invalid_command():
    print("Invalid value")


def get_operator(number_1, number_2, operation):
    try:
        return {
            '+': operator.add(number_1, number_2),
            '-': operator.sub(number_1, number_2),
            '*': operator.mul(number_1, number_2),
            '/': operator.truediv(number_1, number_2),
            '**': operator.pow(number_1, number_2),
            '//': operator.floordiv(number_1, number_2),
            '%': operator.mod(number_1, number_2)
        }[operation]

    except ZeroDivisionError:
        print("Cannot be divided by 0")
    except KeyError:
        invalid_command()


def calc(answer):
    if answer.upper() == "Y":
        try:
            number_1, number_2 = int(input("Enter first number ")), int(input("Enter second number "))
            operation = input("Choose operation: +, -, *, /, **, //, % ")
            result = get_operator(number_1, number_2, operation)
            if result is not None:
                print(f"Result is \n{number_1} {operation} {number_2} = {result}")

        except ValueError:
            invalid_command()

    elif answer.upper() == "N":
        print("Exit")
        time.sleep(1)
        exit()

    elif answer.upper != "N" or "Y":
        invalid_command()


answer = str(input("Do you want calculation?(Y/N) "))
calc(answer)
while True:
    answer_again = str(input("Do you want calculation? again?(Y/N) "))
    calc(answer_again)
