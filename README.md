# 🤖 Reactive AI Agents Collection

Welcome to a curated collection of **Reactive AI Agents** — lightweight, stateless agents that respond instantly to environmental inputs without memory or planning. This repository is ideal for anyone looking to understand or implement basic intelligent behavior in a rule-based or prompt-driven manner.

---

## 🧠 What is a Reactive Agent?

A **Reactive Agent** is the simplest form of an intelligent agent. It immediately responds to input using predefined rules or direct mappings, without storing any internal state or memory.

### 🔑 Key Characteristics
- No internal memory or history
- No goal setting or planning
- Stateless and deterministic
- Fast response time
- Behavior based solely on current input

### 💡 Analogy

A motion-activated light:
- **Input:** Detect motion  
- **Output:** Turn on  
- No memory or reasoning—just a direct reaction.

### 🧪 Example

```python
def reactive_agent(input_text):
    if "hello" in input_text.lower():
        return "Hi there!"
    elif "bye" in input_text.lower():
        return "Goodbye!"
    else:
        return "I didn't understand that."

```

### 📂 Project List
Each project below is a self-contained reactive agent performing a unique task using minimal logic and no memory.


### 1. 🎭 Instant Sentiment Classifier
Classifies a single message as Positive, Negative, or Neutral on-the-fly using keyword matching or an optional LLM.

✅ Highlights
Stateless classification

Rule-based or LLM-based

Ideal for quick feedback systems

🔧 Code (Rule-Based)
```
def classify_sentiment(message: str) -> str:
    positive_keywords = ["good", "great", "love", "amazing", "happy", "fantastic"]
    negative_keywords = ["bad", "hate", "terrible", "sad", "awful", "angry"]

    message_lower = message.lower()

    if any(word in message_lower for word in positive_keywords):
        return "😊 Positive"
    elif any(word in message_lower for word in negative_keywords):
        return "😠 Negative"
    else:
        return "😐 Neutral"
```

###  💡 Use Cases
Real-time chat moderation

Customer feedback labeling

Sentiment flagging in comments


### 2. 🌦️ Weather Responder Bot
Answers questions about weather using a local static dataset. No APIs or memory involved.

✅ Highlights
Stateless, keyword-triggered

Uses local dictionary

Quick and simple responses

### 3. 🚫 Spam Detection Bot
Flags spam messages based on common keywords—no learning or past message tracking.

✅ Highlights
Stateless, rule-based

Uses spam-indicator keywords

Good for basic message filtering

### 4. 🎬 Movie Genre Guesser
Guesses a movie genre based on its plot description using keyword matches.

✅ Highlights
Keyword-based genre prediction

Fully offline, no ML

Reacts instantly to input



