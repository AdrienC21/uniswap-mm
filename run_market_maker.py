"""
Execute the transaction
"""

import config
import time
import web3
from utils import *
from transaction_information import *

address = web3.Web3.toChecksumAddress(config.address)

client = UniswapV2Client(address, config.private_key, provider=config.provider)
transac_info = exchange(client, status, coin_a, coin_b, amount,
                        min_max, dest_address=address,
                        deadline=(deadline + int(time.time())))
hash = "0x" + transac_info.hex()

print("Transaction hash :\n{hash}".format(hash=hash))
