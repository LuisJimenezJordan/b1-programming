import random

print(f"Welcome to Blackjack. Enter the number of users who will play today: ")
#Looping through until valid input is received, integers
while True:
    try:
        player_count = int((input("")))
        if player_count <= 0:
            print("Please enter a positive integer")
            continue
        else:
            break
    except ValueError:
        print("Please enter an integer.")

#Sets up a variable to store player names, then collects player names
#based on the number of players entered from the above input player_count
player_names = []
for i in range (player_count):
    name = input(f"Enter name for player {i+1}: ")
    player_names.append(name)

class Deck:
    def __init__(self):
        ranks = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'}
        suits = [ 'Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cards = [Card(s,r) for s in suits for r in ranks]

    def draw(self, n=1):
        n = min(n, len(self.cards))
        return [self.cards.pop(random.randrange(len(self.cards)))for _ in range(n)]

class Card:
    rank_values = {"A": 1, "Jack": 11, "Queen": 12, "King": 13, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Card.rank_values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit} (Card value: {self.value})'

class Hand:
    def __init__(self, deck, n_cards=2):
        self.cards = deck.draw(n_cards)

    @property
    def total_value(self):
        return sum(card.value for card in self.cards)

    def __str__(self):
        cards_str = ", and ".join(str(card) for card in self.cards)
        return f"{cards_str}. Total value of the hand is {self.total_value}"

class Player:
    def __init__(self, name, deck):
        self.busted = False
        self.name = name
        self.hand = Hand(deck)

    def hitme(self, deck):
        deck.draw(1)
        return

    @property
    def bust_check(self):
        if self.hand.total_value >21:
            self.busted = True
            return 'busted'
        else:
            self.busted = False
            return 'not busted'

    def __str__(self):
        return f'{self.name} holds the following cards: {self.hand}, meaning they are {self.bust_check}.'

class Game:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = []

        # Create Dealer separately
        self.dealer = Player("Dealer", self.deck)
        self.players.append(self.dealer)

        #Make human player objects from names provided
        for name in player_names:
            self.players.append(Player(name, self.deck))

        #Store number of human players
        self.player_number = len(player_names)

my_deck = Deck()
my_hand = Hand(my_deck)
game = Game(player_names)

for player in game.players:
    print(player)
