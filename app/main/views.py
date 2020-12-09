import json
import hashlib
import requests
from flask import jsonify

from . import main
from .blockchain import Blockchain


@main.route('/')
def index():
    blockchain = Blockchain()
    transaction1 = blockchain.new_transaction("Joe", "Anne", "3 BTC")
    transaction2 = blockchain.new_transaction("Anne", "Joe", "1 BTC")
    transaction3 = blockchain.new_transaction("Joe", "Mary", "3 BTC")
    blockchain.new_block(54321)

    transaction4 = blockchain.new_transaction("Jenny", "Alice", "7 BTC")
    transaction5 = blockchain.new_transaction("Alice", "Bob", "0.5 BTC")
    transaction6 = blockchain.new_transaction("Bob", "Jenny", "0.5 BTC")
    blockchain.new_block(98765)

    return jsonify(blockchain.chain)
