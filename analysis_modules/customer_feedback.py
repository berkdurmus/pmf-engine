import pandas as pd
from textblob import TextBlob

def analyze_feedback(data):
    """
    Analyze customer feedback for sentiment.

    :param data: DataFrame with a 'feedback' column containing text of customer feedback
    :return: Average sentiment score of the feedback
    """
    # Ensure that the feedback column exists
    if 'feedback' not in data.columns:
        raise ValueError("Data must contain a 'feedback' column.")

    # Function to apply sentiment analysis on each piece of feedback
    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity

    # Apply sentiment analysis
    data['sentiment'] = data['feedback'].apply(get_sentiment)

    # Calculate average sentiment score
    average_sentiment = data['sentiment'].mean()
    return average_sentiment

# Example usage
# data = pd.DataFrame({'feedback': ['I love this product!', 'Not what I expected.', ...]})
# avg_sentiment = analyze_feedback(data)
# print("Average Sentiment Score:", avg_sentiment)
