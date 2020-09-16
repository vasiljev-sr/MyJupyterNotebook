class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6'
                                        '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, face, suit):
        '''Инициалирует карту номиналом и мастью'''
        self._face = face
        self._suit = suit

        @property
        def face(self):
            return self._face

        @property
        def suit(self):
            return self._suit

        @property
        def image_name(self):
            return str(self).replace(' ','_') + '.png'

        def __repr__(self):
            return f'Card(face="{self.face}", suit = "{self.suit}")'

        def __str__(self):
            return f'{self.face} of {self.suit}'

        def __format__(self,format):
            return f'{str(self):format}'
