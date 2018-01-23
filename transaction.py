import random

class Transaction(object):

    def __init__(self):
        self.transaction = {}

    def get(self):
        return self.transaction

    def make(self, amount, customer, receiver):
        self.transaction = {customer: amount, receiver: amount * -1}
        return self

    def generate(self, maxValue=3):
        amount    = random.randint(1,maxValue)
        rand = random.randint(0, 1)
        customer = 'Marie' if rand == 0 else 'PL'
        receiver = 'PL' if rand == 0 else 'Marie'
        return self.make(amount, customer, receiver)
