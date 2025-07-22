def detect_language(text: str) -> str:
    language_keywords = {
        "English": ["the", "and", "is", "hello", "how", "you"],
        "Spanish": ["el", "la", "es", "hola", "cómo", "usted"],
        "French": ["le", "la", "est", "bonjour", "comment", "vous"],
        "German": ["der", "die", "ist", "hallo", "wie", "sie"],
        "Italian": ["il", "ciao", "come", "sei", "tu", "è"]
    }
 
    text_lower = text.lower()
    scores = {lang: 0 for lang in language_keywords}
 
    for lang, keywords in language_keywords.items():
        for word in keywords:
            if word in text_lower:
                scores[lang] += 1
 
    best_match = max(scores, key=scores.get)
    if scores[best_match] == 0:
        return "❓ Language not recognized"
    return f"🈶 Detected Language: {best_match}"
 
# 🧪 Test Cases
print(detect_language("Bonjour, comment allez-vous?"))          # French
print(detect_language("Hola, cómo estás?"))                     # Spanish
print(detect_language("Ciao, come stai?"))                      # Italian
print(detect_language("Hallo, wie geht es dir?"))               # German
print(detect_language("Hello, how are you?"))                   # English