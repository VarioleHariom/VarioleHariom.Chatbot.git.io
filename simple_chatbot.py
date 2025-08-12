import random
import time

def slow_print(text, delay=0.02):
    """Optional: prints text slowly for nicer UX."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def respond(user):
    u = user.lower().strip()
    if any(g in u for g in ("hello", "hi", "hey", "good morning", "good afternoon", "good evening")):
        return random.choice([
            "Hi there! How can I help you today?",
            "Hello! What would you like to talk about?",
            "Hey! Need anything?"
        ])

    elif "your name" in u or "who are you" in u or "what is your name" in u:
        return "I'm ChatPy, a small rule-based chatbot built using if-else."
    
    elif "time" in u and "date" not in u:
        from datetime import datetime
        return "Current time: " + datetime.now().strftime("%H:%M:%S")

    elif "date" in u or "day" in u:
        from datetime import datetime
        return "Today's date: " + datetime.now().strftime("%Y-%m-%d")


    elif "how are you" in u or "how do you do" in u:
        return random.choice(["I'm just code, but I'm doing great! Thanks for asking.", "Feeling helpful — how about you?"])

    
    elif any(tok in u for tok in ("+", "plus", "add", "sum", "-", "minus", "subtract", "*", "times", "multiply", "/", "divide")):
    
        try:
            
            allowed = set("0123456789+-*/.() ")
            expr = "".join(ch for ch in u if ch in allowed)
            result = eval(expr, {"__builtins__": None}, {})
            return f"The result is {result}"
        except Exception:
            return "I couldn't parse that math expression. Try something like '2 + 3 * (4 - 1)'."

    
    elif any(x in u for x in ("bye", "goodbye", "see you", "exit", "quit")):
        return "Goodbye! Have a great day!"

    
    elif "help" in u or "what can you do" in u:
        return ("I can: greet you, tell time/date, do simple math, and answer a few questions. "
                "Try: 'hello', 'what time is it', '2+2', or 'what is your name'.")

    
    else:
        return "Sorry, I didn't understand that. Can you rephrase or ask for 'help'?"

def chat():
    slow_print("ChatPy: Hello! (type 'exit' or 'bye' to end)\n", delay=0.01)
    while True:
        user = input("You: ")
        if not user.strip():
            print("ChatPy: Please type something.")
            continue

        reply = respond(user)
        print("ChatPy:", reply)

        if any(x in user.lower() for x in ("bye", "goodbye", "exit", "quit", "see you")):
            break

if __name__ == "__main__":
    chat()
