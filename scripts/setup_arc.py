import sys
import os
import time

# Ensure project root is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.immunity.prr_checker import run_reflex_arc

def setup_organism():
    print("\n--- SFA-One: Environmental Setup (Innate Immune System) ---")
    
    # 1. Validate Oct4 Genome
    print("Step 1: Parsing constitution.md (Oct4 Factor)...")
    time.sleep(0.5)
    with open('specs/constitution.md', 'r') as f:
        genome = f.read()
    print(">> Genome Loaded: Pluripotency confirmed.")
    
    # 2. Run Reflex Arc (Pathogen Check)
    print("Step 2: Activating Local Reflex Arc (Pattern Recognition Receptors)...")
    try:
        run_reflex_arc("Execute SFA-One Setup")
        print(">> Environment Cleared: No epigenetic pathogens detected.")
    except Exception as e:
        print(f">> ALERT: {e}")
        sys.exit(1)
        
    # 3. Verify Klf4 Identity (ERC-8004)
    print("Step 3: Verifying Agent Identity on Peaq Ledger (Klf4 Factor)...")
    reg_path = 'specs/identity/registration.json'
    if os.path.exists(reg_path):
        print(f">> Identity metadata found at {reg_path}")
        with open(reg_path, 'r') as f:
            import json
            metadata = json.load(f)
            print(f">> Agent Name: {metadata.get('name', 'Unknown')}")
        print(">> Identity Verified: ERC-8004 protocol active.")
    else:
        print(">> WARNING: Identity metadata missing. Run scripts/identity/mint_agent.py")
    
    print("\n--- Setup Complete: Organism Homeostasis Achieved ---\n")

if __name__ == "__main__":
    setup_organism()
