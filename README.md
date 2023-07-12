# Scraping blockchain data

## General resources

General tutorials on how blockchains work can be found in the [wiki](../../wiki/)

## Getting started

Most of these scripts connect to a blockchain node (validator) and request information through their API.  There are a number of services that provide (limited) free access to nodes.

Before you get started, sign up for free accounts at 

* [Alchemy](https://www.alchemy.com/pricing)
* [Infura](https://infura.io)
* [NowNodes](https://nownodes.io/pricing)

When you sign up, they'll give you an endpoint that you can copy/paste into the scripts.

Alternatively, you can run your own Ethereum node.  I recommend [Erigon](https://github.com/ledgerwatch/erigon) as your execution client, and I've used [Lighthouse](https://github.com/sigp/lighthouse) as a consensus client.  Lighthouse works well, but I haven't tried any other consensus clients.
[Here's a good tutorial on installing Erigon](https://chasewright.com/getting-started-with-turbo-geth-on-ubuntu/).

## web3.py

The [web3](https://web3py.readthedocs.io/en/stable/) library is a great tool for scraping data from Ethereum.

[EatTheBlocks has a good tutorial](https://www.youtube.com/playlist?list=PLbbtODcOYIoFs0PDlTdxpEsZiyDR2q9aA) on the Javascript Web3 library (although we use the Python Web3 library, the concepts are very similar).  

## Fungible and non-fungible tokens

The ERC20 standard governs how most "fungible" tokens behave.  Read the documentation for [ERC20 tokens](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/)

The ERC721 standard governs how most "non-fungible" tokens behave.  Read the documentation for [ERC721 tokens](https://ethereum.org/en/developers/docs/standards/tokens/erc-721/)

The ['Tokens' Tutorial on EatTheBlocks](https://www.youtube.com/playlist?list=PLbbtODcOYIoGOvl0KH57_nfvEKOYV6qdT) is another good place to learn about interacting with Ethereum Tokens

## eventscanner

The web3 library provides a tool "[eventscanner](https://web3py.readthedocs.io/en/stable/examples.html#advanced-token-fetch)" that can scan the blockchain for events from a specific contract.
The script [get_contract_events.py](eventscanner/get_contract_events.py) provides a modified version of the web3 event scanner that can scan the Ethereum blockchain for all events emitted by a specific contract
This performs alright for contracts that don't emit too many events (e.g. Compound governance) but performs badly for contracts that emit a lot of events (e.g. all USDC transfers).
If you're interested in the web3 eventscanner more generally, [here's a walkthrough](https://coinsbench.com/web3-py-fetching-all-transfer-events-on-single-tokens-from-a-given-timestamp-90bd6ec08e33) of how it works.

## event-scraper

The script [get_contract_logs.py](event-scraper/get_contract_logs.py) allows you to scrape the Ethereum blockchain for events emitted by a specific contract and write the results to a csv.
The functionality is very similar to eventscanner, but get_contract_logs.py is much simpler
Ethereum nodes are very finicky, and the different scripts 
