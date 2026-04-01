--- 
name: triple-agent-commerce
description: Implement the AP2 'Triple-Agent' architecture for secure, auditable commerce [Source 491, 1004]. 
--- 
# Triple-Agent Protocol
1. **Separation of Duties:** Ensure distinct roles for the **Shopping Agent** (User intent), **Merchant Agent** (Catalog/Cart), and **Credential Provider** (Secure Vault) to maintain privacy and compliance [Source 491, 1004].
2. **Mandate Lifecycle:** Generate cryptographically signed **Intent Mandates** (User instructions), **Cart Mandates** (Merchant offers), and **Payment Mandates** (Authorization) [Source 493, 298].
3. **Synthetic Small RNAs:** Treat mandates as the only data allowed to survive an **E13 Context Flush**, guiding the re-establishment of the agent's purpose after a security reset [Source 491, 954].
4. **Mullet Economy Settlement:** Use AP2 for compliant governance (front-end) and route settlement through **PayRam** using **MNEE** or **USDC** for instant finality (back-end) [Source 494, 58].
