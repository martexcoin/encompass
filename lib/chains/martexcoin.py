'''Chain-specific MarteXcoin code'''
from cryptocur import CryptoCur, hash_encode, hash_decode, rev_hex, int_to_hex
import os

import coinhash

class martexcoin(CryptoCur):
    PoW = False
    chain_index = 5
    coin_name = 'MarteXcoin'
    code = 'MXT'
    p2pkh_version = 50
    p2sh_version = 5
    wif_version = 176

    header_hash = coinhash.X13Hash

    block_explorers = {
        'MarteXcoin': 'http://be.martexcoin.org/',
    }

    base_units = {
        'MXT': 8,
        'mMXT': 5,
    }

    chunk_size = 2016

    # Network
    DEFAULT_PORTS = {'t':'50001', 's':'50002', 'h':'8081', 'g':'8082'}

    DEFAULT_SERVERS = {
        'electrum.martexcoin.org':DEFAULT_PORTS, # oficial
    }

    checkpoints = {
	0: "81f998298dc023c13c9b7948f75cd1ab90b30d7f9d753e7dbdbfb3b00b193e3b"
        260342: "ced16599e8097e4316e3de8a29d4a283ea9d8a87e824e2f28e0bdfa893cb6e27",
    }

Currency = MarteXcoin
