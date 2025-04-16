
!pip install wikipedia
import wikipedia
topic = input("Enter brief topic")
summary = wikipedia.summary(topic, sentences=5)
print("Summary for", topic, ":\n", summary)