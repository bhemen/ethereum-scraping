from web3 import Web3
from web3.contract import Contract
from web3.providers.rpc import HTTPProvider
import json

#When you want to interact with a contract, you need to know its Application Binary Interface (ABI).
#The ABI is *not* provided on the chain, and you need to get it from somewhere else
#In this example, we'll only use two contract functions 'totalSupply', 'symbol' and 'decimals' so we only specify those in the ABI
ERC20_ABI = json.loads('[{ "constant": true, "inputs": [], "name": "totalSupply", "outputs": [ { "name": "", "type": "uint256" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "stateMutability": "view", "type": "function" },{ "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "stateMutability": "view", "type": "function" } ]' )

#If you want to call other functions, you can find an example of the complete ABI at https://gist.github.com/veox/8800debbf56e24718f9f483e1e40c35c
#ERC20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]') 

#Here are a collection of addresses of ERC20 tokens that you can find on etherscan 
#contract_address = "0x6b175474e89094c44da98b954eedeac495271d0f" #DAI
address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2" #WETH

############################
#Connect to an Ethereum node
api_url = f"http://127.0.0.1:8545" #Replace this with your API URL (e.g. the an Infura/Alchemy/Quicknode RPC endpoint)
provider = HTTPProvider(api_url)
web3 = Web3(provider)

############################
#Read from the ERC20 contract

#If you copy an address from etherscan, you need to convert that to a checksum address before you can use it in python web3
address = Web3.toChecksumAddress(address)

#Note that we need to provide *both* the on-chain address and the abi of the contract we want to interact with
contract = web3.eth.contract(address=address,abi=ERC20_ABI)

#In order for a function "sampleFunction" to be available through contract.functions.sampleFunction() it needs to be specified in the ABI
#Even if the function is in the contract, you cannot call it if you did not specify it in the ABI
supply = contract.functions.totalSupply().call() #Compare to https://etherscan.io/address/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2#readContract#F2
decimals = contract.functions.decimals().call() #Compare to https://etherscan.io/address/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2#readContract#F3
symbol = contract.functions.symbol().call() #Compare to https://etherscan.io/address/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2#readContract#F5

print( f"The circulating supply of {symbol} is {supply/(10**decimals)}" )
	
