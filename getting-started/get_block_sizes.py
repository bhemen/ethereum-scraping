"""
	Extract block sizes and write the data to data/eth_block_sizes.csv
"""

from web3 import Web3
import progressbar
import pandas as pd

#Change this to the endpoint you got from Infura/Alchemy or an Eth node you're running
url="http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(url))

london_hard_fork_block_num = 12965000

if w3.isConnected():
	pass
else:
	print( "Failed to connect to Ethereum node!" )


#Ethereum block gas limit has increased dramatically over the years
#https://blog.mycrypto.com/the-history-of-ethereums-block-size-block-gas-limit

#After the London Hard Fork (August 2021) the target limit is 15M gas
#https://ethereum.org/en/developers/docs/gas/

start_block = 1
end_block = w3.eth.block_number
start_block = end_block - 50

block_sizes = {}
block_size_df = pd.DataFrame(columns=['block_num','block_size','miner','timestamp','num_txes'])

rows = []
with progressbar.ProgressBar(max_value=end_block-start_block) as bar:
	for block_num in range(start_block,end_block):
		block = w3.eth.get_block(block_num)
		rows.append( { 'block_num': block_num, 'block_size': block.gasUsed, 'miner': block.miner, 'timestamp': block.timestamp, 'num_txes': len(block.transactions) } )
		if block_num % 100000 == 0:
			block_size_df = pd.concat( [block_size_df,pd.DataFrame(rows)], ignore_index=True )
			block_size_df.to_csv( "../data/eth_block_sizes.csv", index=False )
		bar.update(block_num-start_block)

block_size_df = pd.concat( [block_size_df,pd.DataFrame(rows)], ignore_index=True )
block_size_df.to_csv( "data/eth_block_sizes.csv", index=False )


