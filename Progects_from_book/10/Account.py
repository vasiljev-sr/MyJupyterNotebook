from decimal import Decimal


class Account:
    '''Класс  Account для ведения банковского счета'''

    def __init__(self, name, balance):
        '''Инилициализачия обьекта Account'''
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be >= to 0.00')

        self.balance += amount