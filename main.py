import click


class CardTable:
    def __init__(self):
        self.number = 0
        self.cards = []
        self.active = True

    def hit(self):
        self.number = self.number + 1
        print('hit')
        print(self.number)

    def stay(self):
        self.active = False




@click.command()
def game():
    table.hit()
    table.hit()

    table.stay()




if __name__ == '__main__':
    # Create a new game instance
    table = CardTable()
    # Start the game!
    game()