# Uniswap - Simple Market Maker

Uniswap - Simple Market Maker is a Python library that can be used to process transactions on Uniswap.

## Installation

Clone this repository :

```bash
git clone https://github.com/AdrienC21/uniswap-mm.git
```

## Usage

Edit the file config.py with the following information :

```python
address = ""  # (str) Wallet Address ("0x...")
private_key = ""  # (str) Wallet private key ("0x...")
provider = ""  # (str) url of mainnet (ex : "https://mainnet.infura.io/v3/...")
```

Edit the file transaction_information.py :

```bash
sell (str) : "buy" or "sell".
If set to "buy", we want to buy <amount> <coin_b> using <coin_a>
If set to "sell", we want to sell <amount> <coin_a> to obtain <coin_b>

coin_a (str) : name of the first crypto used in the transaction. The name has
to be the one used in coinmarketcap.com url

coin_b (str) : name of the second crypto used in the transaction.
amount (float) : quantity of crypto to exchange (in wei)
min_max (float) : if we want to buy <coin_b>, it s the maximum amount of input
tokens that can be required before the transaction reverts. if we want to sell
<coin_a>, it s the minimum amount of output tokens that must be received for
the transaction not to revert.

dest_address (str) : Default=config.address. Address that will receive <coin_b>
deadline (int) : Maximum amount of time in seconds we wait for the transaction
not to revert.

    Example :
status = "sell"
coin_a = "ethereum"
coin_b = "basic-attention-token"
amount = 0.005
min_max = 0.
dest_address = config.address
deadline = 600
```

Run the file run_market_maker.py to process a swap on Uniswap.

## Quick Overview

The library is a wrapper of an already existing Web3 / Uniswap wrapper entitled uniswap-python-v2. The file uniswap_tools.py has been modified to correct errors and to add an automatic extraction of the average gas used on Uniswap and an estimation of the current gas price (this function is inside gas.py).

Utils.py contains the core functions and transaction_information.py and config.py store parameters.

run_markmet_maker.py execute a trade.

An estimation of gas parameters and the address of the different crypto we want to use are found by scrapping crypto websites ([Coinmarketcap](https://coinmarketcap.com/coins/) and [Crypto](https://crypto.com/defi/dashboard/gas-fees)).

Those features are obtained here :

![alt text](images/token.png?raw=true "Title")

![alt text](images/gas.png?raw=true "Title")

## Documentation

### gas.py

[get_pair](https://uniswap.org/docs/v2/smart-contracts/factory/#getpair)
```python
token_a = "0x20fe562d797a42dcb3399062ae9546cd06f63280"
token_b = "0xc778417E063141139Fce010982780140Aa0cD5Ab"
pair = client.get_pair(token_a, token_b)
```
Returns the address of the pair for ``token_a`` and ``token_b``, if it has been created, else ``0x0000000000000000000000000000000000000000``.
### utils.py

## License
[MIT](https://choosealicense.com/licenses/mit/)