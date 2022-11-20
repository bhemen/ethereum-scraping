# Getting started with web3

* The script [latest_block](latest_bock.py) just connects to an Ethereum node and gets the latest block number.  It's useful for checking whether your Ethereum node has synced

* The script [get_block_info](get_block_info.py) shows how to grab a single block from the Ethereum blockchain, and print some of the data in it

* The script [block_sizes](block_sizes.py) shows how to get a sequence of blocks from the Ethereum blockchain, and store specific statistics about these blocks in a [pandas](https://pandas.pydata.org/docs/user_guide/index.html) dataframe

* The script [read_erc20](read_erc20.py) shows how to read data from an [ERC20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) smart contract.

* The script [get_contract_creations](get_contract_creations.py) shows how to scan the Ethereum blockchain for contract creation transactions in order to build up a list of *all* smart contracts on Ethereum

