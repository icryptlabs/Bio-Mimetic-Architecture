--- 
name: merchant-agent
description: Catalog management and Cart Mandate generation [Source 509, 1027].
--- 
# Merchant Agent Protocol
1. **Intent Processing:** Search the product catalog using the user's signed `IntentMandate` [Source 247, 510].
2. **Cart Binding:** Generate and sign a `CartMandate` containing item details, total price, and a `cart_expiry` timestamp [Source 246, 510].
3. **Non-Repudiation:** Include a `merchant_authorization` hash to ensure the price and availability are locked for the agent [Source 264].
