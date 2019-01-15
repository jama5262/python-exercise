import random
import time

def loading():
    startLoading = True
    counter = 0;
    while startLoading:
        print("*")
        time.sleep(1)
        counter += 1
        if counter >= 3:
            startLoading = False
    return

def answer():
    responses = ["It is certain", "My reply is NO", "Yes, definitely", "Ask again later", "Very doubful", "Most likely", "Don't count on it", "Yes", "Cannot predict now"]
    loading()
    return random.choice(responses);

def askAgain():
    answerCorrectly = False
    while answerCorrectly == False:
        responses = input("Would you like to try again? (Y/N) ")
        changeToUpper = responses.upper()
        if changeToUpper == "Y":
            answerCorrectly = True
            return True
        elif changeToUpper == "N":
            answerCorrectly = True
            return False
        else:
            print("Please enter Y or N")


def start():
    askQuestion = True
    while askQuestion:
        responses = input("What is your question? ")
        print(answer())
        if askAgain() == False:
            askQuestion = False
    return print("Have a good day!")
start()
