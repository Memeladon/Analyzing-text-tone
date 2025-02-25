from textblob import TextBlob
from collections import Counter
import numpy as np

class DataService:
    def __init__(self, tokens):

        self.tokens = tokens

    def build_statistics(self):
        """Построение многомерной статистики"""
        word_counts = Counter(self.tokens)
        total_words = len(self.tokens)
        unique_words = len(word_counts)
        avg_word_length = np.mean([len(word) for word in self.tokens])
        return {
            'word_counts': word_counts,
            'total_words': total_words,
            'unique_words': unique_words,
            'avg_word_length': avg_word_length
        }

    def analyze_sentiment(self):
        """Анализ тональности текста"""
        text = ' '.join(self.tokens)
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return {
            'polarity': sentiment.polarity,
            'subjectivity': sentiment.subjectivity
        }