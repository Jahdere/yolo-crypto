from hash import encrypt

class Chain(object):
    def __init__(self):
        self.chain = []

    def get(self):
        return self.chain

    def makeBlock(self, transactions):
        parentBlock = self.chain[-1] if len(self.chain) > 0 else None
        parentHash  = parentBlock[u'hash'] if parentBlock != None else None
        blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1 if parentBlock != None else 0
        transactionCount = len(transactions)

        blockContents = {
            u'blockNumber':blockNumber,
            u'parentHash':parentHash,
            u'transactionCount':transactionCount,
            'transactions':transactions
        }

        blockHash = encrypt(blockContents)
        block = {u'hash':blockHash,u'contents':blockContents}

        self.chain.append(block)

        return block
