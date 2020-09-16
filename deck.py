import random
from card import Card

class DeckOfCards:
     NUMBER_OF_CARDS = 52

     def __init__(self):
        '''Инициализирует колоду'''
        self._curent_card = 0
        self._deck = []

        for i in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[i % 13],Card.SUITS[ i //13]))

        def shuffle(self):
            self._curent_card = 0
            random.shuffle(self._deck)

        def deal_card(self):
            try:
                card = self._deck[self._current_card]
                self._current_card += 1
                return card
            except:
                return None
        def __str__(self):
            s = ''

            for i, card in enumerate(self._deck):
                s += f'{self._deck[i]:<19}'
                if i % 4 == 0:
                    s += '\n'
            return s