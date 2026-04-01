# SFA-One Evolution, Survival & Execution Launchpad [Source 706, 724, 1067, 813, 831]

# Activate the Peripheral Nervous System
init-pns:
	uv run scripts/sensory/vision_bridge.py
	uv run scripts/sensory/tts_vocalizer.py

# Trigger Mitochondrial Sovereignty (Local Gemma 3n Inference)
run-sovereign:
	just init-pns
	uv run python -m gemma_3n_sdk.server --device cuda

# Initialize the ERC-8004 Identity Registry
init-identity:
	uv run python scripts/identity/mint_erc8004.py --config specs/identity/erc8004_registration.json

# Fixate an agent-generated IP asset as an NFT on XRPL + Arc L1 [Source 319, 755, 838]
# Usage: just fixate-ip ASSET=path/to/asset.py LICENSE=proprietary
fixate-ip ASSET='.' LICENSE='proprietary':
	uv run python modules/ledger/mint_ip_nft.py fixate --asset {{ASSET}} --license {{LICENSE}}

# Audit the full IP Lineage graph (verify all Methylation Marks on all chains)
audit-lineage:
	uv run python modules/ledger/mint_ip_nft.py audit

# Activate the Verifiable Kraken Trader [Source 905]
run-trader:
	kraken-cli mcp serve &
	uv run python scripts/trading/swarm_trader.py --risk-router 0x...

# Orchestrate Aerodrome Liquidity
manage-liquidity:
	uv run python scripts/liquidity/aerodrome_manager.py

# Execute a Physical Payment Mandate [Source 945]
authorize-payout:
	uv run python scripts/hardware/mx_ink_auth.py --intent 'Authorize Agent-to-Agent Payout'

# Audit the Financial Phenotype [Source 496]
audit-execution:
	uv run scripts/compliance/check_ledger_fixation.py --network xrpl

# Audit the integrated organism (Audit Trail Mandate)
audit-trail:
	uv run python scripts/compliance/check_ledger_fixation.py --network xrpl

# Deploy the Innate Immunity agents [Source 905]
deploy-immunity:
	bash scripts/security/setup_wazuh_agent.sh

# Trigger an Immune response simulation [Source 905, 1067]
test-immunity:
	uv run scripts/security/simulate_pathogen.py --type prompt_injection

# Perform a weekly 'Therapy Session' to audit security health [Source 905]
audit-immunity:
	uv run python scripts/compliance/check_allostatic_load.py --security-only

# Run a full metabolic audit to check token burn [Source 1067]
audit-metabolism:
	uv run scripts/compliance/check_allostatic_load.py

# Execute an E13 Context Flush (Reprogramming) [Source 335, 1015]
flush-context:
	uv run scripts/recovery/yamanaka_reset.py --factor sox2
