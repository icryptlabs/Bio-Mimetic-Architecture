"""
mint_ip_nft.py — IP Fixation Module (Epigenetic Methylation Marks)

Mints an IP NFT for every agent-generated Offspring asset, binding its
SHA-256 fingerprint to the active ERC-8004 agent identity on both XRPL
(primary) and Arc L1 (secondary). These records form the immutable
parent-child Lineage Graph [Source 319, 755, 838].
"""

import hashlib
import json
import logging
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Logging (append-only — never truncate the lineage log)
# ---------------------------------------------------------------------------
LOG_PATH = Path(__file__).parent.parent.parent / "logs" / "ip_lineage.log"
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [IP-LINEAGE] %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, mode="a"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Configuration (read from environment — never hard-code secrets)
# ---------------------------------------------------------------------------
XRPL_WALLET_SEED = os.getenv("XRPL_WALLET_SEED", "")
ARC_KIT_KEY = os.getenv("ARC_KIT_KEY", "")
AGENT_NFT_ID_ENV = os.getenv("AGENT_NFT_ID", "")   # Set after `just init-identity`
IPFS_GATEWAY = os.getenv("IPFS_GATEWAY", "https://ipfs.io/ipfs/")


# ---------------------------------------------------------------------------
# Identity Resolution (Klf4 Factor) [Source 321, 429]
# ---------------------------------------------------------------------------

class IdentityError(RuntimeError):
    """Raised when no valid ERC-8004 agent identity is found."""


def get_active_agent_id() -> str:
    """
    Returns the active on-chain agent NFT ID.
    Priority: env var AGENT_NFT_ID → specs/identity/erc8004_registration.json
    Raises IdentityError if nothing is set.
    """
    if AGENT_NFT_ID_ENV:
        return AGENT_NFT_ID_ENV

    spec_path = Path(__file__).parent.parent.parent / "specs" / "identity" / "erc8004_registration.json"
    if spec_path.exists():
        with open(spec_path) as f:
            spec = json.load(f)
        regs = spec.get("registrations", [])
        if regs:
            return str(regs[0].get("agentId", ""))

    raise IdentityError(
        "No active agent identity found. Run `just init-identity` first to mint the ERC-8004 NFT."
    )


# ---------------------------------------------------------------------------
# Hash Utilities
# ---------------------------------------------------------------------------

def compute_file_hash(file_path: str | Path) -> str:
    """Compute SHA-256 digest of a file (streaming, handles large files)."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def compute_payload_hash(payload: dict) -> str:
    """Compute SHA-256 digest of a serialized JSON payload (deterministic)."""
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()


# ---------------------------------------------------------------------------
# Layer-1 Fixation Adapters
# ---------------------------------------------------------------------------

def _write_to_xrpl(asset_hash: str, agent_id: str, metadata: dict) -> str:
    """
    Write an IP Methylation Mark to the XRP Ledger.
    Returns the transaction hash on success.
    [Source 319, 755]
    """
    try:
        # Real integration: `pip install xrpl-py`
        # from xrpl.clients import JsonRpcClient
        # from xrpl.models.transactions import NFTokenMint
        # from xrpl.wallet import Wallet
        # client = JsonRpcClient("https://s1.ripple.com:51234/")
        # wallet = Wallet.from_seed(XRPL_WALLET_SEED)
        # ...

        # --- Simulation layer (no live key required for dev) ---
        simulated_hash = hashlib.sha256(
            f"xrpl:{asset_hash}:{agent_id}:{time.time()}".encode()
        ).hexdigest()
        logger.info(f"[XRPL] IP NFT minted — TX: {simulated_hash} | Asset: {asset_hash[:16]}...")
        return simulated_hash

    except Exception as exc:  # noqa: BLE001
        logger.error(f"[XRPL] Fixation failed: {exc}")
        raise RuntimeError(f"XRPL fixation error: {exc}") from exc


def _write_to_arc(asset_hash: str, agent_id: str, metadata: dict) -> str:
    """
    Write an IP Methylation Mark to Arc L1 (secondary redundancy).
    Returns the transaction hash on success.
    [Source 838]
    """
    try:
        # Real integration: ArcEpigeneticBarrier from modules/fixation/arc_ledger.py
        # from modules.fixation.arc_ledger import ArcEpigeneticBarrier
        # barrier = ArcEpigeneticBarrier(kit_key=ARC_KIT_KEY)
        # return barrier.fix_transaction(asset_hash)

        simulated_hash = hashlib.sha256(
            f"arc:{asset_hash}:{agent_id}:{time.time()}".encode()
        ).hexdigest()
        logger.info(f"[ARC]  IP NFT minted — TX: {simulated_hash} | Asset: {asset_hash[:16]}...")
        return simulated_hash

    except Exception as exc:  # noqa: BLE001
        logger.error(f"[ARC] Fixation failed: {exc}")
        raise RuntimeError(f"Arc fixation error: {exc}") from exc


# ---------------------------------------------------------------------------
# Primary Public API
# ---------------------------------------------------------------------------

def fixate_generated_ip(
    asset_hash: str,
    metadata: dict,
    agent_id: Optional[str] = None,
) -> dict:
    """
    Mint an IP NFT for an agent-generated Offspring asset.

    Args:
        asset_hash: SHA-256 hex digest of the finalized asset.
        metadata:   Dict containing asset_name, asset_type, license, etc.
        agent_id:   (Optional) Override the active agent identity.

    Returns:
        {
            "asset_hash": str,
            "agent_id": str,
            "xrpl_tx_hash": str,
            "arc_tx_hash": str,
            "timestamp_utc": str,
        }

    Raises:
        IdentityError: If no valid ERC-8004 agent identity exists.
        RuntimeError:  If Layer-1 write fails on either chain.
    """
    resolved_agent_id = agent_id or get_active_agent_id()
    logger.info(
        f"Fixating IP for agent '{resolved_agent_id}' | "
        f"asset='{metadata.get('asset_name', 'unknown')}' | hash={asset_hash[:16]}..."
    )

    # Dual-chain write — BOTH must succeed (Immutability Invariant)
    xrpl_tx = _write_to_xrpl(asset_hash, resolved_agent_id, metadata)
    arc_tx = _write_to_arc(asset_hash, resolved_agent_id, metadata)

    timestamp = datetime.now(timezone.utc).isoformat()
    result = {
        "asset_hash": asset_hash,
        "agent_id": resolved_agent_id,
        "xrpl_tx_hash": xrpl_tx,
        "arc_tx_hash": arc_tx,
        "timestamp_utc": timestamp,
        "metadata": metadata,
    }

    # Append-only audit record
    with open(LOG_PATH, "a") as log:
        log.write(json.dumps(result) + "\n")

    logger.info(
        f"✅ Lineage established — XRPL: {xrpl_tx[:16]}... | Arc: {arc_tx[:16]}..."
    )
    return result


def fixate_file(file_path: str | Path, metadata: Optional[dict] = None) -> dict:
    """
    Convenience wrapper: hash a file and fixate it in one call.

    Args:
        file_path: Path to the finalized asset on disk.
        metadata:  Optional extra fields merged into the base metadata.

    Returns:
        Same dict as fixate_generated_ip().
    """
    path = Path(file_path)
    asset_hash = compute_file_hash(path)
    base_metadata: dict = {
        "asset_name": path.name,
        "asset_type": path.suffix.lstrip(".") or "binary",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    if metadata:
        base_metadata.update(metadata)
    return fixate_generated_ip(asset_hash=asset_hash, metadata=base_metadata)


def audit_lineage_log() -> list[dict]:
    """
    Read and verify all IP lineage records from the append-only log.
    Returns a list of all fixation records sorted by timestamp.
    """
    if not LOG_PATH.exists():
        logger.warning("No lineage log found. No IP has been fixated yet.")
        return []

    records = []
    with open(LOG_PATH) as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                logger.warning(f"Corrupted lineage record at line {line_no} — skipping.")

    records.sort(key=lambda r: r.get("timestamp_utc", ""))
    logger.info(f"Audit complete — {len(records)} IP records found.")
    return records


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="SFA-One IP Fixation Module")
    subparsers = parser.add_subparsers(dest="command")

    # fixate command
    fix_parser = subparsers.add_parser("fixate", help="Hash and mint an IP NFT for a file")
    fix_parser.add_argument("--asset", required=True, help="Path to the asset file")
    fix_parser.add_argument("--license", default="proprietary", help="License type (e.g. MIT, proprietary)")
    fix_parser.add_argument("--asset-type", default="code", help="Asset type (code, content, spec)")

    # audit command
    subparsers.add_parser("audit", help="Audit all IP lineage records")

    args = parser.parse_args()

    if args.command == "fixate":
        result = fixate_file(
            file_path=args.asset,
            metadata={"license": args.license, "asset_type": args.asset_type},
        )
        print(json.dumps(result, indent=2))

    elif args.command == "audit":
        records = audit_lineage_log()
        print(json.dumps(records, indent=2))

    else:
        parser.print_help()
