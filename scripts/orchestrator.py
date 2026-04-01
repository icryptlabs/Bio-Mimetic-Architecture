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
        print(f"AP2: Transcription intent: '{intent}' -> IntentMandate created.")
        return {"id": hashlib.md5(intent.encode()).hexdigest(), "type": "INTENT"}

    def sign_cart_mandate(self, intent_id, selection):
        print(f"Merchant Agent: Binding {selection} to Intent {intent_id[:10]}... -> CartMandate signed.")
        return {"id": hashlib.sha256(intent_id.encode()).hexdigest(), "items": [selection], "price": 49.99}

    def sign_payment_mandate(self, cart_id):
        print(f"Credential Provider: Signing PaymentMandate for Cart {cart_id[:10]}...")
        return {"id": hashlib.sha256(cart_id.encode()).hexdigest(), "status": "SIGNED"}

ap2_client = MockAP2Client()
# --- END MOCK ---

from modules.hardware.mx_haptics import signal_fixation_event
from scripts.settlement.payram_bridge import execute_settlement

class ShoppingAgent:
    def capture_intent(self, user_msg):
        print("\n--- Shopping Agent: Differentiated phenotype active ---")
        time.sleep(0.5)
        print(f">> Capturing Intent: {user_msg}")
        return ap2_client.create_intent_mandate(user_msg)

class MerchantAgent:
    def discovery(self, intent_mandate):
        print("\n--- Merchant Agent: Differentiated phenotype active ---")
        time.sleep(0.8)
        print(">> Discovering products with AP2 compliance...")
        return ap2_client.sign_cart_mandate(intent_mandate['id'], "Arc Developer Kit v2")

class CredentialProvider:
    def execute_payment(self, cart_mandate):
        print("\n--- Credential Provider: Hardware-locked vault active ---")
        print(">> Vault holds credentials: [Visa **** 1234].")
        print(">> MANDATORY MYC FACTOR: Waiting for physical haptic tap [MX_INK]...")
        
        # Simulate physical auth
        time.sleep(1.5)
        print(">> [HAPTIC TAP DETECTED] Myc Factor authorization confirmed.")
        
        # Sign mandate
        payment_mandate = ap2_client.sign_payment_mandate(cart_mandate['id'])
        
        # Settle via PayRam (Mullet Economy)
        print(">> Routing to PayRam Bridge Settlement Layer...")
        result = execute_settlement(payment_mandate)
        
        if result.success:
            print(f"--- ECONOMY: Instant stablecoin settlement achieved. Finality: {result.tx_hash[:16]}... ---")
            signal_fixation_event(is_successful=True)
            return True
        return False

def run_triple_agent_swarm():
    print("\nStarting SFA-One Differentiated Triple-Agent Swarm...")
    print("Orchestrating Shopper, Merchant, and Provider phenotypes.")
    
    shopper = ShoppingAgent()
    merchant = MerchantAgent()
    provider = CredentialProvider()
    
    # 1. Shopping (Shopper)
    intent = shopper.capture_intent("I want to build an agentic store on Arc.")
    
    # 2. Merchant (Merchant)
    cart = merchant.discovery(intent)
    
    # 3. Settlement (Provider)
    provider.execute_payment(cart)
    
    print("\nSwarm Lifecycle Complete: Accountability established on the XRP Ledger.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", type=str, help="Comma-separated list of phenotypes")
    args = parser.parse_args()
    
    run_triple_agent_swarm()
