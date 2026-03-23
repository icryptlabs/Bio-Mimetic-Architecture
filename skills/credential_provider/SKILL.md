---
name: arc-credential-provider
description: Secure vault for USDC wallets and cryptographic signing on Arc.
---
# Instructions
1. Hold private keys for Arc/Circle wallets in an isolated environment [3].
2. Do NOT release Payment Mandate signatures autonomously.
3. **Myc Factor Verification:** Only execute `sign_mandate()` upon receiving a physical haptic signal from the MX Ink stylus [7, 9].
4. Write the resulting transaction hash to the Arc Block Explorer to create the Epigenetic Barrier [10].
