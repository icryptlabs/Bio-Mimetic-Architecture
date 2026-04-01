--- 
name: ip-lineage
description: Use this skill to track agent-generated IP via SHA-256 hashing, XRPL/Arc NFT fixation, and licensing through smart contracts [Source 798, 855]. 
--- 
# IP Lineage Protocol

## 🧬 Purpose
Establishes verifiable legal lineage for all agent-generated "Offspring" (code, content, UI specifications). Ensures the **Parent** (User/Operator) retains immutable, auditable ownership on Layer 1. This skill implements the **Epigenetic Barrier** — once written to the ledger, the lineage record cannot be altered or hallucinated away [Source 319, 755].

---

## 🛠️ Instructions

### Step 1 — Hash Generation (Cryptographic Fingerprinting)
Before fixating any asset, compute its **SHA-256 digest**:
```python
import hashlib

def compute_asset_hash(file_path: str) -> str:
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    return sha256.hexdigest()
```
- Every finalized code file, content document, or UI specification MUST be hashed before proceeding.
- For in-memory payloads (e.g., JSON dicts), serialize deterministically with `json.dumps(payload, sort_keys=True)` before hashing.

### Step 2 — Identity Verification (Klf4 Factor Check)
Before writing any record, confirm the active agent's on-chain ERC-8004 identity [Source 321, 429]:
```python
from modules.ledger.mint_ip_nft import get_active_agent_id
agent_id = get_active_agent_id()  # Raises IdentityError if not minted
```
- If no identity exists, run `just init-identity` before proceeding.
- The `agent_id` binds the Offspring to its Parent in the lineage graph.

### Step 3 — Epigenetic Fixation (Layer 1 Write)
Call `modules/ledger/mint_ip_nft.py` to write the **Methylation Mark** to both XRPL and Arc simultaneously [Source 319, 755, 838]:
```python
from modules.ledger.mint_ip_nft import fixate_generated_ip

metadata = {
    "asset_name": "my_module.py",
    "asset_type": "code",
    "creator": agent_id,
    "timestamp_utc": "2026-04-01T00:00:00Z",
    "license": "proprietary",   # or "MIT", "CC-BY-4.0", etc.
    "parent_entity": "icryptlabs/Bio-Mimetic-Architecture",
}

result = fixate_generated_ip(asset_hash=asset_hash, metadata=metadata)
print(f"XRPL TX: {result['xrpl_tx_hash']}")
print(f"Arc TX:  {result['arc_tx_hash']}")
```
- Both hashes must be logged to `logs/ip_lineage.log` (append-only).
- A failed write MUST NOT be silently swallowed — raise and surface the error.

### Step 4 — Lineage Mapping (Graph Registration)
After fixation, associate the IP NFT with the active ERC-8004 identity:
```python
from scripts.identity.mint_agent import register_ip_offspring
register_ip_offspring(agent_id=agent_id, ip_nft_hash=result["xrpl_tx_hash"])
```
- This creates an auditable parent-child edge: `User ──owns──> Agent ──authored──> Offspring` [Source 431, 798].
- Run `just audit-lineage` to verify the graph at any time.

### Step 5 — Licensing Setup (x402 Smart Contract)
If the Offspring requires commercial licensing [Source 855, 859]:
1. Define terms in `specs/ip/license_<asset_name>.json` (royalty %, geographic limits, expiry).
2. Publish the license terms to IPFS and record the CID alongside the XRPL NFT.
3. Configure the `x402` payment gate endpoint to redirect revenue to the Parent wallet.
```bash
just fixate-ip --asset path/to/asset.py --license commercial
```

---

## 🔒 Invariants
- **Immutability**: Once a Methylation Mark is written, it CANNOT be deleted. Any attempt to overwrite must mint a NEW NFT linking to the previous version (chain of custody).
- **Dual-Chain Fixation**: Every IP record MUST be written to BOTH XRPL (primary) and Arc L1 (secondary) for redundancy [Source 755, 838].
- **Agent Accountability**: An IP record without a valid `agent_id` is invalid and will be rejected by the `mint_ip_nft.py` module.

---

## 📋 Audit Commands
| Command | Purpose |
|---|---|
| `just fixate-ip` | Hash and mint an IP NFT for a given asset |
| `just audit-lineage` | Verify all IP records on XRPL and Arc |
| `just init-identity` | Mint the ERC-8004 agent identity (prerequisite) |
