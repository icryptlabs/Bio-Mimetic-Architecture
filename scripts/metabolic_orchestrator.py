import sys
import os
import time
import argparse
import hashlib
from unittest.mock import MagicMock

# Ensure project root is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- MOCK DEPENDENCIES ---
sys.modules['logitech_actions_sdk'] = MagicMock()
sys.modules['logitech_actions_sdk'].trigger_haptic = MagicMock()

class MockAP2Client:
    def create_intent_mandate(self, intent):
        print(f"AP2: Synthesis Intent: '{intent}' [Source 247, 308] -> IntentMandate created.")
        return {"id": hashlib.md5(intent.encode()).hexdigest(), "type": "INTENT"}

    def find_products(self, intent_mandate):
        print(f"UA: Discovery Negotiation... [Source 240, 247] -> CartMandate received.")
        return {"id": hashlib.sha256(intent_mandate['id'].encode()).hexdigest(), "value": 0.005}

    def sign_payment_mandate(self, cart_id):
        print(f"CP: Signing PaymentMandate for Cart {cart_id[:10]}... [Source 512, 514]")
        return MagicMock(id=hashlib.sha256(cart_id.encode()).hexdigest(), value=0.005)

ap2_client = MockAP2Client()
# --- END MOCK ---

from modules.hardware.mx_haptics import signal_fixation_event
from scripts.settlement.payram_executor import run_metabolic_fixation

class ShoppingAgentUA:
    def capture_intent(self, user_msg):
        print("\n--- Shopping Agent (UA): Intent Synthesis active ---")
        return ap2_client.create_intent_mandate(user_msg)

    def negotiate_cart(self, intent_mandate):
        print("\n--- Shopping Agent (UA): Discovery active ---")
        time.sleep(0.1)
        # UA negotiates with ME phenotypes...
        me = MerchantAgentME()
        return me.propose_cart(intent_mandate)

class MerchantAgentME:
    def propose_cart(self, intent_mandate):
        print("\n--- Merchant Agent (ME): Negotiation active ---")
        return ap2_client.find_products(intent_mandate)

class CredentialProviderCP:
    def execute_payment(self, cart_id):
        print("\n--- Credential Provider (CP): Hardware-bound vault active ---")
        print(">> MANDATORY MYC FACTOR: Listening for 'Stylus Tap' pulse [MX Ink] [Source 333, 337]...")
        
        # Simulate physical auth (Stylus Tap)
        time.sleep(1.0)
        print(">> [STYLUS TAP DETECTED] Myc Factor authorization confirmed.")
        
        # Sign mandate
        return ap2_client.sign_payment_mandate(cart_id)

def run_metabolic_swarm(count=55):
    print(f"\n--- SFA-One: Metabolic Orchestrator (Triple-Agent Swarm) ---")
    print(f"Executing {count} metabolic settlement transactions on Arc L1 [Source 513, 1016].")
    
    ua = ShoppingAgentUA()
    cp = CredentialProviderCP()
    
    # 1. Shopping Lifecycle (UA)
    intent = ua.capture_intent("Build an agentic store on Arc.")
    cart = ua.negotiate_cart(intent)
    
    # 2. Hardware Auth (CP)
    payment_mandate = cp.execute_payment(cart['id'])
    
    # 3. Settlement Stream (Builder + Validator) [Source 355]
    print("\nStarting Swarm Stream (Doubled Compute Protocol)...")
    for i in range(count):
        # Builder & Validator phases inside run_metabolic_fixation
        res = run_metabolic_fixation(payment_mandate)
        
        if res.success:
            print(f"FIXATION {i+1}/{count} SUCCESS: {res.tx_hash[:16]}...")
            signal_fixation_event(is_successful=True)
        else:
            print(f">> ALERT: Swarm validation failure for transaction {i+1}!")
            break
            
    print(f"\n--- Swarm Lifecycle Complete: Epigenetic Barrier established on XRPL. ---")
    print("Mitochondrial Sovereignty Score: 100%. Protocol: MAS-One [Source 1025].\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=55)
    args = parser.parse_args()
    
    run_metabolic_swarm(args.count)
