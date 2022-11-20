from web3 import Web3
import random
import json

#Change this to the endpoint you got from Infura/Alchemy/Quicknode or an Eth node you're running
url="http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(url))

london_hard_fork_block_num = 12965000

if w3.isConnected():
	pass
else:
	print( "Failed to connect to Ethereum node!" )

def toString(obj):
	#If you want to print the block nicely, you need to take a circuitous route
	obj_string = Web3.toJSON(obj) #most objects returned by eth calls are AttributeDicts that contain HexBytes objects that cannot be JSON serialized with the standard json library
	obj_dict = json.loads(obj_string) #Now we have a dict, where the HexBytes objects have been stringified
	obj_string = json.dumps( obj_dict, indent=2 ) #Now we can turn the whole object back into a string with nice indentation
	return obj_string

block_num = random.randint( 1, london_hard_fork_block_num-100 )

#https://web3py.readthedocs.io/en/stable/web3.eth.html?highlight=get_block#web3.eth.Eth.get_block
block = w3.eth.get_block(block_num)

#You can directly access fields in the block
miner_address = block.miner
print( f"Block was mined by {miner_address}" )

print( toString( block ) )

print( f"There were {len(block.transactions)} in block number {block.number}" )
for tx_hash in block.transactions[:3]: #Only print the first 3 txes -- there can be lots
	tx = w3.eth.get_transaction(tx_hash)
	print( toString( tx ) )


