import random
import time

def loader(value):
    ticks = 0;
    while True:
        print("*")
        time.sleep(1)
        ticks += 1
        if ticks >= value:
            break

def getInput(text):
    return input(text)


def answer():
    responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes-definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    loader(5)
    return print(random.choice(responses))

def askAgain():
    while True:
        responses = getInput("Would you like to try again? (Y/N) ")
        changeToUpper = responses.upper()
        if changeToUpper == "Y":
            return True
        elif changeToUpper == "N":
            return False
        else:
            print("Please enter Y or N")


def start():
    while True:
        responses = getInput("What is your question? ")
        answer()
        if askAgain() == False:
            break
    return print("Have a good day!")

if __name__ == '__main__':
    start()
