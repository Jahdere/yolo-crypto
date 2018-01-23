class Bank(object):
    def __init__(self):
        self.accounts = {
            'Marie': 50,
            'PL': 10
        }

    def getAccounts(self):
        return self.accounts

    def setAccounts(self, accounts):
        self.accounts = accounts
        return self.accounts

    def updateAccounts(self, transaction):
        accounts = self.accounts.copy()
        for key in transaction:
            if key in accounts.keys():
                accounts[key] += transaction[key]
            else:
                accounts[key] = transaction[key]

        self.accounts = accounts
        return self.accounts

    def isValidTransaction(self, transaction):
        if sum(transaction.values()) is not 0:
            return False

        for key in transaction.keys():
            if key in self.accounts.keys():
                accountBalance = self.accounts[key]
            else:
                accountBalance = 0

            if (accountBalance + transaction[key]) < 0:
                return False

        return True
