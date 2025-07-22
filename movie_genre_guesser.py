genre_keywords = {
    "action": ["explosion", "chase", "fight", "battle", "war", "gun"],
    "comedy": ["funny", "hilarious", "joke", "laugh", "prank", "comedy"],
    "horror": ["ghost", "haunted", "murder", "killer", "zombie", "nightmare"],
    "romance": ["love", "relationship", "kiss", "affair", "heart", "romantic"],
    "sci-fi": ["space", "alien", "future", "robot", "AI", "technology"],
    "drama": ["family", "life", "struggle", "emotion", "serious", "relationship"]
}

def guess_genre(description: str) -> str:
    genre_keywords = {
        "Action": ["explosion", "chase", "fight", "battle", "war", "gun"],
        "Comedy": ["funny", "hilarious", "joke", "laugh", "prank", "comedy"],
        "Horror": ["ghost", "haunted", "murder", "killer", "zombie", "nightmare"],
        "Romance": ["love", "relationship", "kiss", "affair", "heart", "romantic"],
        "Sci-Fi": ["space", "alien", "future", "robot", "AI", "technology"],
        "Drama": ["family", "life", "struggle", "emotion", "serious", "relationship"]
    }
 
    description_lower = description.lower()
    scores = {genre: 0 for genre in genre_keywords}
 
    for genre, keywords in genre_keywords.items():
        for keyword in keywords:
            if keyword in description_lower:
                scores[genre] += 1
 
    best_genre = max(scores, key=scores.get)
    if scores[best_genre] == 0:
        return "❓ Genre not identified"
    return f"🎬 Predicted Genre: {best_genre}"
 
# 🧪 Test Cases
print(guess_genre("In the distant future, a robot gains consciousness and challenges humanity."))  # Sci-Fi
print(guess_genre("A young couple falls in love in Paris during spring."))                         # Romance
print(guess_genre("A haunted house terrorizes a family during the night."))                        # Horror

from langchain_community.llms import Ollama
llm = Ollama(model="mistral")

def guess_with_llm(message: str) -> str:
    prompt = f"Guess the genre of this movie based on this line:\n\nMessage: {message}"
    return llm.invoke(prompt)

print(guess_with_llm("Sandy and Derrick lived happily together for a long time."))