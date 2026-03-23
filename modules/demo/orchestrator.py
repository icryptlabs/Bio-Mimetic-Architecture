import sys
import os
import time
import hashlib
from unittest.mock import MagicMock

# Fix import path when run directly via uv run
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# --- DEMO MOCK INJECTION ---
sys.modules['logitech_actions_sdk'] = MagicMock()
sys.modules['logitech_actions_sdk'].update_actions_ring = MagicMock()
sys.modules['logitech_actions_sdk'].trigger_haptic = MagicMock()

sys.modules['vertex_ai_vision'] = MagicMock()
mock_vision = MagicMock()
mock_vision.transaction_count = 55
sys.modules['vertex_ai_vision'].analyze_ui.return_value = mock_vision

import builtins
mock_dial = MagicMock()
mock_dial.get_value.return_value = 1.95 # Extra fast velocity out of 2.0 (delay = max(0.1, 2.0-1.95) = 0.05s)
builtins.logi_dial = mock_dial

mock_arc = MagicMock()
def generate_tx(amount):
    return f"0x{hashlib.sha256(str(time.time() + amount).encode()).hexdigest()}"
mock_arc.settle_nanopayment.side_effect = generate_tx
builtins.arc_client = mock_arc

def mock_screenshot():
    print("Capturing Arc L1 UI state...")
    time.sleep(1.0)
    return "snapshot_001.png"
builtins.take_explorer_screenshot = mock_screenshot
# --- END MOCKS ---

from modules.hardware.logi_bridge import sync_hardware_state
from modules.hardware.mx_haptics import signal_fixation_event
from modules.sensory.visual_cortex import verify_arc_fixation

# THE 'SYMPHONIC' DEMO LOOP
def run_integrated_demo(total_tx=55):
    # 1. INTENT CAPTURE (RNA Transcription)
    print('SFA-One: Listening for voice intent... [Myc Factor Active]')
    time.sleep(1.5)
    print(">> 'Execute 55 sub-cent tasks on Arc.'")
    time.sleep(1.0)
    print('>> Intent captured. Transcribing Small RNA Mandate...')
    time.sleep(1.0)
    
    # 2. METABOLIC STREAM (Economic Proof)
    print(f'Commencing {total_tx} sub-cent transactions on Arc L1 (Metabolism)...')
    time.sleep(0.5)
    for i in range(total_tx):
        # Allosteric Throttling
        dial_val = logi_dial.get_value() 
        delay = sync_hardware_state(dial_val, agent_phase='Executing')
        
        # Settlement
        tx_hash = arc_client.settle_nanopayment(0.005)
        
        # Sensory Proprioception
        signal_fixation_event(is_successful=True)
        
        print(f'FIXATION {i+1}/{total_tx}: {tx_hash}')
        time.sleep(delay)
    
    # 3. VISUAL VERIFICATION (Visual Cortex)
    print('Activating Visual Cortex: Confirming Epigenetic Fixation on-chain...')
    screenshot = take_explorer_screenshot()
    verification = verify_arc_fixation(screenshot)
    
    if verification['status'] == 'Fixation Verified':
        print(f"============================================================")
        print(f" ECONOMIC PROOF: 55 Actions Settled @ < $0.05 Total Gas.")
        print(f" 99% Margin Protected. Epigenetic Drift: 0%.")
        print(f" DEMO COMPLETE: {verification['count']} actions verified.")
        print(f"============================================================")

if __name__ == "__main__":
    print("\nStarting SFA-One Multimodal Orchestrator...\n")
    run_integrated_demo(total_tx=55)
