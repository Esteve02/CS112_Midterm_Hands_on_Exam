import random

while True:

    print("\nChoose an operand to practice. \n(1)Addition (2)Subtraction (3)Multiplication (4)Division")

    operand = int(input("Enter the corresponding number: "))
    random1 = random.randint(1, 99)
    random2 = random.randint(1, 99)

    if operand == 1:
        print("What is " + str(random1), "+", str(random2))
        correct = random1 + random2
    elif operand == 2:
        print("What is " + str(random1), "-", str(random2))
        correct = random1 - random2
    elif operand == 3:
        print("What is " + str(random1), "*", str(random2))
        correct = random1 * random2
    else:
        print("What is " + str(random1), "/", str(random2))
        correct = random1 / random2

    correctFinal = int(correct)

    answer = eval(input("Enter your answer: "))

    if answer == correctFinal:
        print("Correct!")
    else:
        print("Wrong")

    res = input("\ndo you want to try again?(y/n): ")
    if res != 'y':
        break
