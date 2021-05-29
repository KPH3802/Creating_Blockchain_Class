from Block_class import Block

class Blockchain:
    def __init__(self):
      self.chain = []
      self.all_transactions = []
      self.genesis_block()
    
    def genesis_block(self):
      Block(transactions = [], previous_hash=0)
      self.chain.append(Block)