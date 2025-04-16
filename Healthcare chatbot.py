
# Step 1: Install required tools
!pip install googlesearch-python newspaper3k transformers sentencepiece
from googlesearch import search
from newspaper import Article
from transformers import pipeline
# Step 2: Define summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
# Step 3: Get medical info from the web
def search_medical_articles(query):
    print("Searching the web...")
    links = []
    for url in search(query + " site:mayoclinic.org OR site:webmd.com OR site:healthline.com", num=3, stop=3):
        links.append(url)
    return links
def extract_article_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except:
        return ""
def answer_health_question(question):
    urls = search_medical_articles(question)
    combined_text = ""
    for url in urls:
        content = extract_article_content(url)
        if content:
            combined_text += content[:3000]  # Avoid too long input for summarizer
    if not combined_text:
        return "Sorry Nuna, I couldn’t find enough info. Try rephrasing?"
    print("Summarizing content...")
    summary = summarizer(combined_text, max_length=200, min_length=60, do_sample=False)[0]['summary_text']
    return summary