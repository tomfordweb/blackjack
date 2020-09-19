
import click
import random

class Card:
    faces = {
        1: "Ace",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Queen",
        12: "Jack",
        13: "King"
    }

    suites = {
        1: "Spades",
        2: "Hearts",
        3: "Diamonds",
        4: "Clubs"
    }

    def __init__(self):
        self.points = random.randint(1, 13)
        self.suite = random.randint(1, 4)


    def getCardName(self):
        print(this.faces.get(self.points), "of", this.suites.get(self.suite))

class Table:
    def __init__(self):
        self.number = 0
        self.cards = []
        self.active = True

    def hit(self):
        card = Card()
        self.cards.append(card)
        self.number = self.number + card.points
        
        print('HIT!',  self.number)

    def stay(self):
        self.active = False
    


@click.command()
@click.option('--hit', prompt="Hit?")
def drawCardPrompt(hit):
    if(hit == 'y'):
        table.hit()
    
    
    if(hit != 'y'):
        table.stay()
    
    if(table.number >= 21):
        table.stay()



if __name__ == '__main__':
    # Create a new game instance
    table = Table()
    # Start the game with two cards!
    table.hit()
    table.hit()
    while table.active:
        drawCardPrompt()