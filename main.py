
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
        self.number = 0
        self.points = random.randint(1, 13)
        self.suite = random.randint(1, 4)


    def __repr__(self):

        return '{} of {}'.format(self.faces.get(self.points), self.suites.get(self.suite))


class Table:
    def __init__(self): 
        self.points = 0
        self.cards = []
        self.active = True

    def startGame(self):
        self.hit()
        self.hit()
    
    def showHand(self):
        print('You are at ', self.points)   
        print(self.cards)
        
    def hit(self):
        card = Card()
        self.cards.append(card)
        self.points = self.points + card.points
        

    def stay(self):
        self.active = False
        print('Final score', self.points)
    


@click.command()
@click.option('--hit', prompt="Hit?")
def drawCardPrompt(hit):
    if(hit == 'y'):
        table.hit()
        table.showHand()
        drawCardPrompt()
    
    
    if(hit != 'y'):
        table.stay()
    
    if(table.points > 21):
        table.stay()

    



if __name__ == '__main__':
    # Create a new game instance
    table = Table()
    # Start the game with two cards!
    table.startGame()

    while table.active:
        table.showHand()
        drawCardPrompt()