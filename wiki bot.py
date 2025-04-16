
import wikipedia
def wikipedia_chatbot():
    print("Hi princess! Ask me anything and I'll fetch it from Wikipedia.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bye sweetheart!")
            break
        try:
            summary = wikipedia.summary(user_input, sentences=2)
            print(f"Bot: {summary}")
        except wikipedia.DisambiguationError as e:
            print(f"Bot: Your query is too broad, honey. Did you mean: {e.options}?")
        except wikipedia.PageError:
            print("Bot: Sorry babe, I couldn't find anything about that.")
        except Exception as e:
            print(f"Bot: Oops! Something went wrong: {e}")
if name == "__main__":
    wikipedia_chatbot()