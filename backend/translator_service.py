from typing import List

import deepl

from config import Settings

settings = Settings()
translator = deepl.Translator(settings.deepl_auth_key)

def translate_text(text: List[str], src: str, dest: str) -> List[str]:
    results = translator.translate_text(text, source_lang=src, target_lang=dest)
    return [result.text for result in results]
