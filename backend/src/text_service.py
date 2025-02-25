import re
import string

import nltk
# nltk.download()

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

class TextService:
    def __init__(self, text: str = None):
        self.text = text

    def tokenizer(self):
        """Токенизация текста"""
        return word_tokenize(self.text)

    def pre_processing(self):
        """Предварительная обработка текста"""
        tokens = self.tokenizer()
        tokens = self.__removal_of_punctuations(tokens)
        tokens = self.__removal_of_stop_words(tokens)
        tokens = self.__stemming(tokens)
        tokens = self.__lemming(tokens)
        return tokens

    def __removal_of_punctuations(self, tokens):
        """Удаление пунктуации"""
        return [token for token in tokens if token not in string.punctuation]

    def __removal_of_stop_words(self, tokens):
        """Удаление стоп-слов"""
        stop_words = set(stopwords.words('english'))
        return [token for token in tokens if token.lower() not in stop_words]

    def __stemming(self, tokens):
        """Стемминг"""
        stemmer = PorterStemmer()
        return [stemmer.stem(token) for token in tokens]

    def __lemming(self, tokens):
        """Лемматизация"""
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(token) for token in tokens]