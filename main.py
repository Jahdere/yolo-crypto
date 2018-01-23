from transaction import Transaction
from bank import Bank
from hash import encrypt
from chain import Chain
import json, sys

if __name__ == '__main__':
    bank = Bank()
    transactions = [Transaction().generate(10) for i in range(30)]

    accounts = bank.getAccounts()

    # Create new chain and init with firt block base on bank accounts
    chain = Chain()
    chain.makeBlock([accounts])

    maxTransactionsPerBlock = 5
    blockTransactions = []

    # Let's generate block for all valid transactions !!
    for transaction in transactions:
        if bank.isValidTransaction(transaction.get()):
            blockTransactions.append(transaction.get())
            bank.updateAccounts(transaction.get())
        else:
            print("ignored transaction !")
            print(json.dumps(transaction.get()))
            print(json.dumps(bank.getAccounts()))
            sys.stdout.flush()
            continue

        # Make a new block and reset list
        if len(blockTransactions) == maxTransactionsPerBlock:
            chain.makeBlock(blockTransactions)
            blockTransactions = []

    if len(blockTransactions) > 0:
        print("Block is not full, getting " + str(len(blockTransactions)) + " transactions")

    print(json.dumps(chain.get(), indent=4, sort_keys=True))
    print(json.dumps(bank.getAccounts(), indent=4, sort_keys=True))
