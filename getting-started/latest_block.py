from web3 import Web3
import random
import json

url="http://127.0.0.1:8545"#Change this to the endpoint you got from Infura/Alchemy or an Eth node you're running
w3 = Web3(Web3.HTTPProvider(url))

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

latest_block = w3.eth.get_block_number()

print( f"Latest block = {latest_block}" )

#print( toString( w3.eth.get_block('latest') ) )
