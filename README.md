# Quickstart Guide

NFT deployment to Solana using arkb, metaplex, based on a medium [article](https://medium.com/cypher-game/how-to-create-a-solana-nft-with-python-68f6f775f742) by [Alex Tandy](https://medium.com/@alex.tandy)

## Installation

while having NodeJS and NPM installed

```bash
npm install -g arkb
```

check if instalation was successful with

```bash
arkb help
```

## get some faucet AR for deployment

go to [ARWEAVE](https://faucet.arweave.net/)'s official faucet site
....
save your test wallet to the root of the project for now

## Upload demo image to arweave

add your arweave wallet to the current working env

```bash
arkb wallet-save bRk6V3yIvyRLQvJ2uIhE7scHM03zAdHAZS59KSJCfM4.json
```

```bash
arkb deploy /path/to/my/divinity.jpg
```
