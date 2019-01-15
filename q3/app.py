from random import randint

def isCorrect(randomNumber, value):
    if str(randomNumber) == value:
        return True
    return False

def start(noOfTries):
    randomNumber = randint(0, 5)
    print(randomNumber)
    for value in range(noOfTries):
        remaining = noOfTries - value
        print('You have ' + str(remaining) + ' tries remaining')
        ans = input("Enter your guess -> ")
        result = isCorrect(randomNumber, ans)

        if result == True:
            print("Correct the answer was " + str(randomNumber))
            break
    else:
        return print("Limit reached, no tries left")

start(3)
