import random
import time

def loading(ticks):
    startLoading = True
    counter = 0;
    while startLoading:
        print("*")
        time.sleep(1)
        counter += 1
        if counter >= ticks:
            startLoading = False
    return print("done")

# loading(3)

def respond():
    responses = ["It is certain", "My reply is NO", "Yes, definitely", "Ask agin later", "Very doubful", "Most likely", "Don't count on it", "Yes", "Cannot predict now"]
    loading(2)
    return random.choice(responses);

def askAgain():
    pass

def start():
    repeat = False
    question = input("What is your question? ")
    print(respond())
    askAgain = input("Would you like to sk again? (Y/N)")

    if

start()
