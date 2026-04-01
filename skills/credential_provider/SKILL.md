--- 
name: credential-provider
description: Secure vault for payment credentials with hardware-bound signing (The Myc Factor) [Source 511, 515].
--- 
# Credential Provider Protocol
1. **Vault Management:** Hold user payment methods (CARD, BANK_ACCOUNT, DIGITAL_WALLET) in a non-reactive, isolated context [Source 251, 515].
2. **Hardware Locking:** Do NOT release cryptographic signatures autonomously [Source 515].
3. **Myc Factor Trigger:** Wait for a physical haptic pulse from the Logitech MX Ink via the Actions SDK [Source 333, 337].
4. **Signature Release:** Once physically authorized, sign the AP2 `PaymentMandate` and route to the Settlement Layer [Source 241, 515].
