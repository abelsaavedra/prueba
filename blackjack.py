import random
from turtledemo.minimal_hanoi import play


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.number, self.suit)


class Deck:
    suits = ["diamonds", "heart", "spades", "clubs"]
    max_number = 13

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))
        random.shuffle(self.cards)

    def give_random_card(self):
        pos = 0
        return self.cards.pop(pos)

    def __str__(self):
        str_cards = [str(card) for card in self.cards]
        return "Deck with {} cards:\n{}".format(len(self.cards), ",\n".join(str_cards))


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.win_lose_draw = ""


class Game:
    card_values = {
        1: 11,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 10,
        12: 10,
        13: 10,
    }

    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.table_cards = []

    def draft_card(self):
        card = self.deck.give_random_card()
        self.table_cards.append(card)
        print(card)

    def count_table_cards(self):
        total = 0
        for card in self.table_cards:
            if card.number == 1 and total + card.number > 21:
                total += 1
            else:
                total += self.card_values[card.number]
        return total

    def ask_how_many_players(self):
        number = ""
        while not number.isdigit():
            number = input("How many players? ")
        return int(number)

    def player_wants_to_continue(self):
        response = input("Do you want another card? (Y/N)")
        return response == "Y" or response == "y"

    def ask_player_name(self, number_of_player):
        name = ""
        while name == "":
            name = input("Name for player {}: ".format(number_of_player))
        return name

    def run(self):
        num_players = self.ask_how_many_players()

        if num_players > 0:
            for n in range(1, num_players + 1):
                self.players.append(Player(self.ask_player_name(n)))

            max_score = 0
            num_winner = 0
            num = 0
            for player in self.players:
                print("\nPlayer {} turn:\n".format(player.name))
                num += 1
                user_continue = True
                self.table_cards.clear()
                while user_continue and self.count_table_cards() < 21:
                    self.draft_card()
                    user_continue = self.player_wants_to_continue()

                player.score = self.count_table_cards()
                if player.score > 21:
                    player.win_lose_draw = "loses"
                else:
                    if player.score > max_score:
                        max_score = player.score
                        player.win_lose_draw = "wins"
                    else:
                        player.win_lose_draw = "loses"
                print("Your score {}".format(player.score))

            print("\nSCORES\n------")
            temp = sorted(self.players, key=lambda player: player.score, reverse=True)
            for player in temp:
                print("{} {} with {}".format(player.name, player.win_lose_draw, player.score))


if __name__ == "__main__":
    blackjack = Game()
    blackjack.run()
