def willHeSurvive(noOfBullets, noOfDragons):
    totalBulletsToKillDragon = noOfDragons * 2
    difference = noOfBullets - totalBulletsToKillDragon

    if difference < 0:
        return False

    return True

def start():
    print(willHeSurvive(2, 3))

start()
