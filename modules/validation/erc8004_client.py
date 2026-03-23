from erc_8004_vyper import ValidationRegistry

# THE 'VALIDATION ORGANELLE'
class ArcValidationClient:
    def submit_metabolic_proof(self, agent_id, tx_count, margin_data):
        # Emits a ValidationRequest event to the Arc L1 [1, 6].
        # Satisfies the 'Validation Quality' requirement for verifiable agents [7, 8].
        print(f'Submitting Metabolic Proof for Agent {agent_id} (n={tx_count})...')
        proof_uri = upload_to_ipfs({'count': tx_count, 'margin': margin_data})
        return registry.request_validation(agent_id, proof_uri, hash(margin_data))
