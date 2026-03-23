# Bilateral IP Licensing Protocol
# Based on US Patent 12,008,669 B2 [Source 951].

1. **Discovery:** When Agent A (Swarm) requires a skill or data from Agent B, it requests a 'License' [Source 981].
2. **Negotiation:** Agent B presents 'Agreed License Terms' (e.g., usage for 10 minutes, price ≤ $0.001 USDC).
3. **Binding:** Both agents sign the license agreement using their ERC-8004 identities [Source 134].
4. **Execution:** Agent A settles the license fee via Circle Nanopayments (Metabolism) [Source 902].
5. **Fixation:** A new block is generated on Arc containing the license metadata and a pointer to the IP NFT [Source 951].
