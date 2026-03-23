from erc_8004_vyper import ValidationRegistry

# THE 'VALIDATION ORGANELLE'
class ArcValidationClient:
    def __init__(self, registry_address):
        self.registry = ValidationRegistry(registry_address)

    def submit_artifact(self, agent_id, request_hash, proof_uri):
        # Emits a ValidationRequest event to the Arc L1 [Source 459].
        # Satisfies the 'Validation Quality' requirement for verifiable agents [Source 819].
        # Proof can include TEE oracles or zkML execution proofs [Source 824].
        print(f'Submitting Validation Artifact for Agent {agent_id}...')
        return self.registry.request_validation(agent_id, proof_uri, request_hash)
