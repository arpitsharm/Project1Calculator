# Function File
def addition(num1, num2):
    return f"Answer of {num1} + {num2} = {int(num1+num2)}"


def subtrction(num1, num2):
    if (num1 > num2):
        return f"Answer of {num1} - {num2} = {int(num1 - num2)}"


    elif (num2 > num1):
        return f"Answer of {num2} - {num1} = {int(num2 - num1)}"

    elif (num1 == 0 and num2 == 0):
        return "0"


def multiplication(num1, num2):
    return f"Answer of {num1} x {num2} = {int(num1 * num2)}"


def division(num1, num2):
    return f"Answer of {num1} / {num2} = {int(num1 / num2)}"
