"""
	Scan the blockchain for contract creation transactions
	
	This will allow you build a list of *all* contract addresses on Ethereum
	You can then later filter these by contract type (e.g. all ERC-721 contracts)	

	Here's how we identify contract addresses:
	"If the target account is not set (the transaction does not have a recipient or the recipient is set to null), the transaction creates a new contract."
	https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html#index-8

	Write the data to data/contract_addresses.csv
"""
from web3 import Web3
import progressbar
import pandas as pd

#Change this to the endpoint you got from Infura/Alchemy or an Eth node you're running
url="http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(url))

cryptokitties_block_num = 4605167 

if w3.isConnected():
	pass
else:
	print( "Failed to connect to Ethereum node!" )

start_block = cryptokitties_block_num
end_block = w3.eth.block_number
start_block = end_block-50
#end_block = start_block + 20

contracts_df = pd.DataFrame(columns=['block_num','timestamp', 'tx_hash','contract_address'])

rows = []
with progressbar.ProgressBar(max_value=end_block-start_block) as bar:
	for block_num in range(start_block,end_block):
		block = w3.eth.get_block(block_num)
		for tx in block.transactions:
			tx_receipt = w3.eth.get_transaction_receipt(tx)
			if tx_receipt.to is None: #https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html#index-8
				print( f"{tx_receipt.contractAddress}" )
				#print( f"Contract {tx_receipt.contractAddress} deployed at {block_num}" )
				rows.append( { 'block_num': block_num, 'tx_hash': tx.hex(), 'timestamp': block.timestamp, 'contract_address': tx_receipt.contractAddress } )
			else:
				try:
					if int(tx_receipt.to,16) == 0:
						print( "Zero address" )
				except Exception as e:
					print( f"Error: {tx_receipt.to}" )
		if block_num % 1000 == 0:
			contracts_df = pd.concat( [contracts_df,pd.DataFrame(rows)], ignore_index=True )
			contracts_df.to_csv( "data/contract_addresses.csv", index=False )
			rows = []
		bar.update(block_num-start_block)

contracts_df = pd.concat( [contracts_df,pd.DataFrame(rows)], ignore_index=True )
contracts_df.to_csv( "data/contract_addresses.csv", index=False )


