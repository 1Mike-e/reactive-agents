def spam_detector(message: str) -> str:
    spam_keywords = [
        "buy now", "click here", "free", "congratulations",
        "limited offer", "winner", "earn money", "make $$$"
    ]
 
    message_lower = message.lower()
    
    if any(keyword in message_lower for keyword in spam_keywords):
        return "🚨 Spam detected"
    else:
        return "✅ Message is clean"
 
# 🧪 Test Cases
print(spam_detector("Click here to claim your FREE prize!"))  # 🚨 Spam detected
print(spam_detector("Don't forget our meeting at 3 PM."))     # ✅ Message is clean
print(spam_detector("Buy now and save 50%! Limited offer!"))  # 🚨 Spam detected

#Using an LLM (Ollama + LangChain)
from langchain_community.llms import Ollama
#from langchain.llms import Ollama
llm = Ollama(model="llama3")

def detect_with_llm(message: str) -> str:
    prompt = f"Detect if this statement is a spam or not:\n\nMessage: {message}"
    return llm.invoke(prompt)

print(detect_with_llm("Buy two and get 5 free items."))