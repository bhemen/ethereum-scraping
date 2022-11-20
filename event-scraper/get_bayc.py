"""
Scan the chain for all events from a specific Curve Pool
"""

api_url = 'http://127.0.0.1:8545'
start_block = 12287507 
contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D" #Bored Ape Yacht Club
outfile = "data/bayc_transfers.csv"
#db_columns=["from","to","tokenId","owner","approved","operator"] #Note, the scraper is stupid, so these must match exactly the variable names in the smart contract
#abi = get_cached_abi(contract_address)
#contract = web3.eth.contract(abi=abi)
#scanned_events = [contract.events.TokenExchange,contract.events.AddLiquidity,contract.events.RemoveLiquidity,contract.events.RemoveLiquidityOne,contract.events.RemoveLiquidityImbalance] 
scanned_events = ["Transfer","Approval","ApprovalForAll"] 

from tools.get_contract_events import getContractEvents

getContractEvents(api_url,start_block,contract_address,outfile,scanned_events)

