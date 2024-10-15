from transformers import pipeline

# English to French Translation
def translate_text_t5(prompt):
    translator = pipeline('translation_en_to_fr', model='t5-small')
    translated_text = translator(prompt, max_length=100)[0]['translation_text']
    print("Translated Text (English to French):", translated_text)

# English to Hindi Translation
def translate_text_english_to_hindi(prompt):
    translator = pipeline('translation_en_to_hi', model='Helsinki-NLP/opus-mt-en-hi')
    translated_text = translator(prompt, max_length=100)[0]['translation_text']
    print("Translated Text (English to Hindi):", translated_text)

# Hindi to English Translation
def translate_text_hindi_to_english(prompt):
    translator = pipeline('translation_hi_to_en', model='Helsinki-NLP/opus-mt-hi-en')
    translated_text = translator(prompt, max_length=100)[0]['translation_text']
    print("Translated Text (Hindi to English):", translated_text)

# Spanish to English Translation
def translate_text_spanish_to_english(prompt):
    translator = pipeline('translation_es_to_en', model='Helsinki-NLP/opus-mt-es-en')
    translated_text = translator(prompt, max_length=100)[0]['translation_text']
    print("Translated Text (Spanish to English):", translated_text)

# German to English Translation
def translate_text_german_to_english(prompt):
    translator = pipeline('translation_de_to_en', model='Helsinki-NLP/opus-mt-de-en')
    translated_text = translator(prompt, max_length=100)[0]['translation_text']
    print("Translated Text (German to English):", translated_text)

# French to English Translation
def translate_text_french_to_english(prompt):
    translator = pipeline('translation_fr_to_en', model='Helsinki-NLP/opus-mt-fr-en')
    translated_text = translator(prompt, max_length=100)[0]['translation_text']
    print("Translated Text (French to English):", translated_text)

# Chinese to English Translation
def translate_text_chinese_to_english(prompt):
    translator = pipeline('translation_zh_to_en', model='Helsinki-NLP/opus-mt-zh-en')
    translated_text = translator(prompt, max_length=100)[0]['translation_text']
    print("Translated Text (Chinese to English):", translated_text)

# Example Usage
if __name__ == "__main__":
    prompt_text = "Translate the following sentence into French: Hello, how are you?"
    translate_text_t5(prompt_text)

    english_text = "Hello, how are you?"
    translate_text_english_to_hindi(english_text)

    hindi_text = "नमस्ते, आप कैसे हैं?"
    translate_text_hindi_to_english(hindi_text)

    spanish_text = "Hola, ¿cómo estás?"
    translate_text_spanish_to_english(spanish_text)

    german_text = "Guten Tag, wie geht es Ihnen?"
    translate_text_german_to_english(german_text)

    french_text = "Bonjour, comment ça va?"
    translate_text_french_to_english(french_text)

    chinese_text = "我爱你"
    translate_text_chinese_to_english(chinese_text)
