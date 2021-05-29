from datetime import datetime 



class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.timestamp = datetime.now()

  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()