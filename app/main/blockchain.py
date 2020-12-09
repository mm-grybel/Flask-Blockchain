import hashlib
import json
from datetime import datetime


class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(
            previous_hash="The Times 03/Jan/2009 Chancellor " \
            "on brink of second bailout for banks.",
            proof=12345)
        print("Created the genesis block")

    # Create a new block consisting of key/value pairs
    # of block information in a JSON object
    def new_block(self, proof, previous_hash=None):

        block = {
            "index": len(self.chain) + 1,
            "timestamp": datetime.utcnow().isoformat(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash
        }

        # Get the hash of this new block and add it to the block
        block_hash = self.hash(block)
        block["hash"] = block_hash

        # Reset the list of pending transactions
        self.current_transactions = []

        # Append this new block to the chain
        self.chain.append(block)
        print(f"Created block {block['index']}")

        return block

    # Search the blockchain for the most recent block
    @property
    def last_block(self):
        # Return the last block in the chain, if there are any blocks
        return self.chain[-1] if self.chain else None

    @staticmethod
    def hash(block):
        # Convert the received block into a string
        # Ensure the dictionary is sorted
        # so that we will not have inconsistent hashes
        received_block = json.dumps(block, sort_keys=True)

        # Convert the string to Unicode
        block_string = received_block.encode()

        # Hash it with SHA256
        raw_hash = hashlib.sha256(block_string)

        # Transform the hash into a hexadecimal string
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    # Add a transaction to the block pool
    def new_transaction(self, sender, recipient, amount):

        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }

        # Add the new transaction to the list of pending transactions
        self.current_transactions.append(transaction)

        return self.last_block['index'] + 1
