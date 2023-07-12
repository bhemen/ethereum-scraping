"""
Scan the chain for all events from the Curve 3Pool
"""

api_url = 'http://127.0.0.1:8545' #The URL of your RPC endpoint
start_block = 10809473 #The block where the contract was created -- if you set this too low, you may waste some time scanning blocks with no events, if you set this too high, you may miss some events
contract_address = "0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7" #The address of the contract you want to scan
outfile = "data/curve_3pool.csv" #The location where you want to save the data
scanned_events = ["TokenExchange","AddLiquidity","RemoveLiquidity","RemoveLiquidityOne","RemoveLiquidityImbalance"]  #The events you want to record

from tools.get_contract_events import getContractEvents

getContractEvents(api_url,start_block,contract_address,outfile,scanned_events) #Run the scanner

