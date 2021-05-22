"""
Core functions of our market maker
"""

import requests
import web3
from uniswap_tools import UniswapV2Client
import config


def extract_token(coin_name):
    """Extract the contract address of the token coin_name based
    on etherscan.io database. The name coin_name must be the one contained in
    its coinmarketcap's url.

    Ex : For BAT, we have the following url on coinmarketcap :
    https://coinmarketcap.com/currencies/basic-attention-token/
    Therefore, coin_name would be "basic-attention-token"

    Args:
        coin_name (str): Name of the crypto

    Raises:
        ValueError: If the name is unknown
        ValueError: If the crypto is not registered on
                    Ethereum

    Returns:
        str: The corresponding token address ("0x0d87...")
    """

    cname = coin_name.lower()
    url = f"https://coinmarketcap.com/currencies/{cname}/"
    r = requests.get(url)
    if r.status_code != 200:
        raise ValueError("Unknown coin name. Please check the url "
                         "on coinmarketcap.com")
    else:
        html_page = r.text
        n = html_page.find("https://etherscan.io/token")

        if n == -1:
            raise ValueError("Error : Coin not on Ethereum platform")
        else:
            token = html_page[n+27:n+69]
            return token


def exchange(client, status, coin_a, coin_b, amount_f, min_max_f,
             dest_address, deadline=600):
    """Process the transaction

    Args:
        client (UniswapObject): Store our private information
        sell (str) : "buy" or "sell".
        If set to "buy", we want to buy <amount> <coin_b> using <coin_a>
        If set to "sell", we want to sell <amount> <coin_a> to obtain <coin_b>

        coin_a (str) : name of the first crypto used in the transaction. The
        name has to be the one used in coinmarketcap.com url.
        Ex : For BAT, we have the following url on coinmarketcap :
        https://coinmarketcap.com/currencies/basic-attention-token/
        Therefore, coin_name would be "basic-attention-token"

        coin_b (str) : name of the second crypto used in the transaction.
        amount (float) : quantity of crypto to exchange (in wei)
        min_max (float) : if we want to buy <coin_b>, it's the maximum
        amount of input tokens that can be required before the transaction
        reverts. if we want to sell <coin_a>, it's the minimum amount of
        output tokens that must be received for the transaction not to revert.

        dest_address (str) : Default=config.address. Address that will receive
        <coin_b> deadline (int, optional): Maximum amount of time in seconds
        we wait for the transaction not to revert.
        Defaults to 600 (10 minutes).

    Raises:
        ValueError: if a pair of tokens doesn't exist
        ValueError: if the status is unknown (different from "buy" and "sell")

    Returns:
        str: Transaction hash in Hex
    """

    amount = int(amount_f * 10**9)  # convert into gigawei
    min_max = int(min_max_f * 10**9)

    if coin_a == "ethereum":
        token_a = client.get_weth_address()
        token_b = extract_token(coin_b)
        pair = client.get_pair(token_a, token_b)

        if pair == "0x0000000000000000000000000000000000000000":
            raise ValueError("Direct pair between {ca} and {cb} "
                             "doesn't exist.").format(ca=coin_a, cb=coin_b)
        else:  # pair exists
            c_sum_token_a = web3.Web3.toChecksumAddress(token_a)
            c_sum_token_b = web3.Web3.toChecksumAddress(token_b)
            path = [c_sum_token_a, c_sum_token_b]

            if status == "buy":
                t = client.swap_eth_for_exact_tokens(amount, min_max,
                                                     path, dest_address,
                                                     deadline)
                return t
            elif status == "sell":
                t = client.swap_exact_eth_for_tokens(amount, min_max,
                                                     path, dest_address,
                                                     deadline)
                return t
            else:
                raise ValueError("Unknown status : "
                                 "please type 'buy' or 'sell'")

    elif coin_b == "ethereum":
        token_a = extract_token(coin_a)
        token_b = client.get_weth_address()
        pair = client.get_pair(token_a, token_b)

        if pair == "0x0000000000000000000000000000000000000000":
            raise ValueError("Direct pair between {ca} and {cb} "
                             "doesn't exist.").format(ca=coin_a, cb=coin_b)
        else:  # pair exists
            c_sum_token_a = web3.Web3.toChecksumAddress(token_a)
            c_sum_token_b = web3.Web3.toChecksumAddress(token_b)
            path = [c_sum_token_a, c_sum_token_b]

            if status == "buy":
                t = client.swap_tokens_for_exact_eth(amount, min_max,
                                                     path, dest_address,
                                                     deadline)
                return t
            elif status == "sell":
                t = client.swap_exact_tokens_for_eth(amount, min_max,
                                                     path, dest_address,
                                                     deadline)
                return t
            else:
                raise ValueError("Unknown status : "
                                 "please type 'buy' or 'sell'")
    else:
        token_a = extract_token(coin_a)
        token_b = extract_token(coin_b)
        pair = client.get_pair(token_a, token_b)

        if pair == "0x0000000000000000000000000000000000000000":
            raise ValueError("Direct pair between {ca} and {cb} "
                             "doesn't exist.").format(ca=coin_a, cb=coin_b)
        else:  # pair exists
            c_sum_token_a = web3.Web3.toChecksumAddress(token_a)
            c_sum_token_b = web3.Web3.toChecksumAddress(token_b)
            path = [c_sum_token_a, c_sum_token_b]

            if status == "buy":
                t = client.swap_tokens_for_exact_tokens(amount, min_max,
                                                        path, dest_address,
                                                        deadline)
                return t
            elif status == "sell":
                t = client.swap_exact_tokens_for_tokens(amount, min_max,
                                                        path, dest_address,
                                                        deadline)
                return t
            else:
                raise ValueError("Unknown status : "
                                 "please type 'buy' or 'sell'")
