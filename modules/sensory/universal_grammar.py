# UNIVERSAL GRAMMAR: Mitochondrial Translation Organelle
# Normalizes intent via local LibreTranslate to achieve linguistic homeostasis [Source 525, 920].
import requests

class UniversalGrammar:
    def __init__(self, endpoint='http://localhost:5000'):
        self.endpoint = endpoint

    def normalize_intent(self, raw_user_input, target_lang='en'):
        # Decouples intent capture from English-centric cloud models.
        # Preserves the 'Germline' intent across language boundaries [Source 920].
        print(f'Universal Grammar: Normalizing input to {target_lang}...')
        try:
            response = requests.post(
                f'{self.endpoint}/translate',
                json={'q': raw_user_input, 'source': 'auto', 'target': target_lang}
            )
            return response.json().get('translatedText')
        except Exception as e:
            print(f'Linguistic Anomaly: {e}. Falling back to raw input.')
            return raw_user_input
