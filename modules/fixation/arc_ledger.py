from circle_titanoboa_sdk import LedgerClient

class ArcEpigeneticBarrier:
    def __init__(self, kit_key):
        self.ledger = LedgerClient(kit_key=kit_key, network='arc')

    def fix_transaction(self, payment_mandate_hash):
        # CREATES THE EPIGENETIC BARRIER
        # Once written to the Arc Block Explorer, the transaction is immutable.
        # This prevents 'hallucinating a refund' or altering history [4, 5].
        print(f'Writing Hash {payment_mandate_hash} to Arc Block Explorer...')
        return self.ledger.write_record(payment_mandate_hash)
