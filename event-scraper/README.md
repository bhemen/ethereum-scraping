# Scanning the Ethereum blockchain for smart contract events

The main purpose of these scripts is to scan the entire chain, block-by-block and extract all events of specified from a given contract, and pushes the events into a pandas dataframe, which is eventually saved as a csv.

In order to use the script you will need to 

* Find the address of the contract you want to scrape
* Read the contract to find all the events
* Find the argument names of all the events
* Update the template
* Run the script
    * Make sure to point the script to a local node.  There are over 16M blocks on the blockchain, so the script will make millions of calls to the node, which will burn through any capped data plans

## Examples

This code is very easy to use, and we provide two examples

* [get_bayc](get_bayc.py) gets all the "Transfer", "Approval" and "ApproveForAll" events from the [Bored Apes NFT contract](https://etherscan.io/address/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d)

* [get_3pool](get_3pool.py) gets events from the [Curve 3Pool](https://curve.fi/#/ethereum/pools/3pool/deposit)

This code is based on the [EventScanner](https://web3py.readthedocs.io/en/v5/examples.html#example-code) class that is part of the Python Web3 library.

## Other files

* [utils](utils.py) provides a get_cached_abi function that takes a contract address and gets the abi for you from etherscan, and then caches it locally (to prevent further calls to etherscan).
* [eventscanner](tools/eventscanner.py) and [scannerstate](tools/scannerstate.py) are generic files that provide the underlying tools for the scanning.  You probably don't need to modify these


