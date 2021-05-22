"""
Contains the information of the transaction that will be executed.

sell (str) : "buy" or "sell".
If set to "buy", we want to buy <amount> <coin_b> using <coin_a>
If set to "sell", we want to sell <amount> <coin_a> to obtain <coin_b>

coin_a (str) : name of the first crypto used in the transaction. The name has
to be the one used in coinmarketcap.com url

coin_b (str) : name of the second crypto used in the transaction.
amount (float) : quantity of crypto to exchange (in wei)
min_max (float) : if we want to buy <coin_b>, it's the maximum amount of input
tokens that can be required before the transaction reverts. if we want to sell
<coin_a>, it's the minimum amount of output tokens that must be received for
the transaction not to revert.

dest_address (str) : Default=config.address. Address that will receive <coin_b>
deadline (int) : Maximum amount of time in seconds we wait for the transaction
not to revert.

    Example :
status = "sell"
coin_a = "ethereum"
coin_b = "basic-attention-token"
amount = 0.01
min_max = 0.
dest_address = config.address
deadline = 600
"""


import config

status = "sell"
coin_a = "ethereum"
coin_b = "basic-attention-token"
amount = 0.005
min_max = 0.
dest_address = config.address
deadline = 600
