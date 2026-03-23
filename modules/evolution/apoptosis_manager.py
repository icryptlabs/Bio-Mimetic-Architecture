# APOPTOTIC SELF-REPAIR: Metabolic Health Monitor
# Monitors ERC-8004 Reputation to prevent systemic failure [Source 453, 911].

def check_metabolic_health(agent_id, reputation_client):
    # Fetches the 'successRate' tag from the Arc L1 Reputation Registry [Source 451].
    health_score = reputation_client.get_score(agent_id, tag='successRate')
    
    if health_score < 85:
        # TRIGGERS APOPTOSIS: Programmed Context Death.
        # Prevents 'Heritable Hallucinations' from poisoning the Arc Ledger [Source 658].
        print(f'Apoptosis Triggered: Health {health_score}%. Initiating Sox2 Context Flush...')
        return trigger_yamanaka_reset()
    return {'status': 'Homeostasis', 'health': health_score}
