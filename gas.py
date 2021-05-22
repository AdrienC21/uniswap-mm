"""
Scrap function on crypto.com to obtain average gas used ans slow transactions
gas price for Uniswap (V2)
"""

import requests


def get_gas():

    res = {}

    url = "https://crypto.com/defi/dashboard/gas-fees"
    r = requests.get(url)
    html_page = r.text

    # Extract GasPrice for slow transactions
    n = html_page.rfind("GasPriceText__GasValueText-sc-1erxzig-0 bHfMrr")
    gasPrice = html_page[n+48:n+51]
    gasPrice = ''.join(c for c in gasPrice if c.isdigit())
    gasPrice = int(gasPrice)

    # Extract Avg Gas Used in Gwei for Swap on Uniswap V2
    for _ in range(2):
        n = html_page.rfind("DefiTable__TableWrapper-dyjxuj-3 "
                            "hwhrta gas-fee-table_container__3b18t container")
        html_page = html_page[:n]
    n = html_page.find("Uniswap V2")
    html_page = html_page[n:]
    n = html_page.find("DefiTableRow__TextCell-aqcgpn-3 iNdgvM priority-md")
    html_page = html_page[n+10:]
    n = html_page.find("DefiTableRow__TextCell-aqcgpn-3 iNdgvM priority-md")
    gas = html_page[n+91:n+104]
    gas = ''.join(c for c in gas if c.isdigit())
    gas = int(gas)

    res["gas"] = gas
    res["gasPrice"] = gasPrice

    return res
