import os
from circle_titanoboa_sdk import Client

# Securely load keys from environment [1]
api_key = os.getenv('CIRCLE_API_KEY')
kit_key = os.getenv('CIRCLE_KIT_KEY')

def initialize_arc_vault():
    # Use the KIT_KEY to bridge the Vyper contracts with Arc L1 [4]
    client = Client(api_key=api_key, kit_key=kit_key, network='arc')
    print('Vault Initialized on Arc L1 with USDC metabolism.')
    return client
