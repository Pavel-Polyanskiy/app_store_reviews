import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


df = pd.read_csv('data.csv')
df.drop('Unnamed: 0', axis = 1, inplace = True)


df['sentiment_score_textblob'] = df['review'].apply(lambda sentiment: TextBlob(sentiment).sentiment.polarity)

SIA = SentimentIntensityAnalyzer()
SIA.polarity_scores(text = 'i love you')['compound']
df['sentiment_score_vader'] = df['review'].apply(lambda sentiment: SIA.polarity_scores(sentiment)['compound'])

df.to_csv('data_with_sentiments.csv')
