from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using TextBlob.
    Applies custom rules to better handle neutral sentiments.
    
    Parameters:
        text (str): The text to analyze.
    
    Returns:
        sentiment (str): 'Positive', 'Negative', or 'Neutral'
        polarity (float): Polarity score from TextBlob (-1 to 1)
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # List of keywords that often indicate neutral sentiment
    neutral_keywords = ["okay", "nothing special", "average", "alright", "fine"]
    
    # Check if any neutral keyword is present in the text (case-insensitive)
    if any(keyword in text.lower() for keyword in neutral_keywords):
        return "Neutral", polarity
    
    # Check for phrases that are usually negative (such as discomfort or frustration)
    negative_phrases = ["can't stand", "too hot", "uncomfortable", "hate", "terrible", "worst", "disappointed"]
    if any(phrase in text.lower() for phrase in negative_phrases):
        return "Negative", polarity
    
    # Set thresholds for sentiment classification
    if polarity > 0.05:
        return "Positive", polarity
    elif polarity < -0.05:
        return "Negative", polarity
    else:
        return "Neutral", polarity

# Sample texts for testing the function
sample_texts = [
    "I absolutely love this product! It exceeded all my expectations.",
    "The weather is amazing today, I feel so happy.",
    "This is the best movie I've seen in years.",
    "I had a great time at the concert. The band was incredible!",
    "I'm so grateful for all the support I’ve received. Feeling very positive.",
    "I hate waiting in long lines. It's so frustrating.",
    "The service here was terrible. I won’t be coming back.",
    "I am very disappointed with the product. It broke after one use.",
    "I can't stand this kind of weather. It's too hot and uncomfortable.",
    "This is the worst decision I’ve made. I regret it deeply.",
    "It’s okay, but nothing special.",
    "The book was alright. Some parts were interesting, others not so much.",
    "I’m not sure how I feel about it yet.",
    "It was an average experience. Neither good nor bad.",
    "The food was fine, nothing extraordinary."
]

# Analyze and print sentiment for each sample text
print("=== Sample Text Sentiment Analysis ===\n")
for text in sample_texts:
    sentiment, polarity = analyze_sentiment(text)
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment} (Polarity: {polarity})\n")