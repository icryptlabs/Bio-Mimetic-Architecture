--- 
name: shopping-agent
description: Interface for capturing user intent and coordinating the discovery of Cart Mandates [Source 511, 512].
--- 
# Shopping Agent Protocol
1. **Intent Synthesis:** Convert natural language prompts into structured AP2 `IntentMandate` objects [Source 247, 308].
2. **Discovery Negotiation:** Call `find_products` to receive cryptographically signed `CartMandate` offers from merchants [Source 240, 247].
3. **Selection:** Present options to the user and call `update_chosen_cart_mandate` upon confirmation [Source 248].
4. **Handoff:** Transition the specific Intent and Cart data to the Credential Provider for hardware-bound execution [Source 240, 511].
