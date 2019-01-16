class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return (self.draft - (self.crew * 1.5)) > 20

if __name__ == '__main__':
    titanic = Ship(15, 10)
    flagShip = Ship(200, 40)
    victory = Ship(2, 1)
    print('The titanic is a {}'.format(titanic.is_worth_it()))
    print('The victory is a {}'.format(victory.is_worth_it()))
    print('The flagShip is a {}'.format(flagShip.is_worth_it()))
