 import hashlib
import time

class FixoriumBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = {
            'index': 0,
            'timestamp': time.time(),
            'data': 'Genesis Block',
            'previous_hash': '0',
            'hash': ''
        }
        genesis_block['hash'] = self.calculate_hash(genesis_block)
        self.chain.append(genesis_block)

    def calculate_hash(self, block):
        data_string = str(block['index']) + str(block['timestamp']) + block['data'] + block['previous_hash']
        return hashlib.sha256(data_string.encode()).hexdigest()

# Create a new blockchain instance
fixorium_blockchain = FixoriumBlockchain()
