import base58
import json
import os
import metaplex_api
from cryptography.fernet import Fernet

SERVER_DECRYPTION_KEY = Fernet.generate_key().decode("ascii")
TEST_PRIVATE_KEY = os.environ["TEST_PRIVATE_KEY"]
TEST_PUBLIC_KEY = "MsE5TofYuKtxgboqwzbLxjFbaNwK41b3YYfX6gyxfcD"
cfg = {"PRIVATE_KEY": TEST_PRIVATE_KEY, "PUBLIC_KEY": TEST_PUBLIC_KEY, "DECRYPTION_KEY": SERVER_DECRYPTION_KEY}
api = metaplex_api.MetaplexAPI(cfg)
account = metaplex_api.Account(list(base58.b58decode(cfg["PRIVATE_KEY"]))[:32])
api_endpoint = "https://api.devnet.solana.com/"

# requires a JSON file with metadata. best to publish on Arweave
divinity_json_file = "https://arweave.net/lafoms3egQiVeboVVSsgIXRH14DiyxmKLwzD_EWiKv8"
# deploy a contract. will return a contract key.
result = api.deploy(api_endpoint, contract_name, contract_symbol)
contract_key = json.loads(result).get("contract")
# conduct a mint, and send to a recipient, e.g. wallet_2
mint_res = api.mint(api_endpoint, contract_key, TEST_PUBLIC_KEY, divinity_json_file)
