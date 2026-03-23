# Listener for the Myc Factor (Haptic Authorization)
import logitech_actions_sdk

def on_mx_ink_tap():
    # Triggered by physical haptic tap
    print('Myc Factor Detected: Releasing Payment Mandate Signature')
    return credential_provider.sign_mandate(payment_mandate)
