#Rule-based Version
def classify_sentiment(message: str) -> str:
    # Very simple keyword-based sentiment classifier
    positive_keywords = ["good", "great", "love", "amazing", "happy", "fantastic"]
    negative_keywords = ["bad", "hate", "terrible", "sad", "awful", "angry"]
 
    message_lower = message.lower()
 
    if any(word in message_lower for word in positive_keywords):
        return "😊 Positive"
    elif any(word in message_lower for word in negative_keywords):
        return "😠 Negative"
    else:
        return "😐 Neutral"
 
# 🧪 Test cases
print(classify_sentiment("I love this new feature!"))     # 😊 Positive
print(classify_sentiment("This is awful, I hate it."))    # 😠 Negative
print(classify_sentiment("It’s okay, I guess."))          # 😐 Neutral


#Using an LLM (Ollama + LangChain)
from langchain.llms import Ollama
llm = Ollama(model="llama3")

 
def classify_with_llm(message: str) -> str:
    prompt = f"Classify the sentiment of this message as Positive, Negative, or Neutral:\n\nMessage: {message}"
    return llm.invoke(prompt)
 
# Example
print(classify_with_llm("I'm feeling a bit down today."))