from modules.sensory.universal_grammar import UniversalGrammar
from ap2.types import IntentMandate

grammar = UniversalGrammar()

def process_multilingual_intent(raw_voice_input):
    # 1. Linguistic Homeostasis: Normalize the intent locally.
    normalized_intent = grammar.normalize_intent(raw_voice_input)
    
    # 2. Transcription: Generate the sequence-specific Small RNA (Intent Mandate) [Source 902].
    # This ensures the core intent survives the Sox2 context flush regardless of input language.
    return IntentMandate(natural_language_description=normalized_intent, max_per_action_usdc=0.01)
