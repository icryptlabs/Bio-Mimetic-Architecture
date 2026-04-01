from sfa_core import ledger_client

def register_agent_identity(metadata_path):
    # Klf4 Factor: Establish the on-chain barrier [Source 320]
    # Uploading registration to IPFS and minting ERC-721 NFT [Source 431]
    uri = ledger_client.upload_to_ipfs(metadata_path)
    agent_id = ledger_client.mint_erc8004_nft(agent_uri=uri)
    print(f'Agent minted as NFT with ID: {agent_id}')
    
    # Reserve the agent wallet with EIP-712 signature [Source 436]
    ledger_client.set_agent_wallet(agent_id, wallet_address='0x...')
    return agent_id
