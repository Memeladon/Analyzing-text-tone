from src.data_service import DataService
from src.text_service import TextService

if __name__ == "__main__":
    text = "I love programming. It's so much fun and exciting!"

    # Обработка текста
    text_service = TextService(text)
    processed_tokens = text_service.pre_processing()

    # Построение статистики и анализ тональности
    data_service = DataService(processed_tokens)
    statistics = data_service.build_statistics()
    sentiment = data_service.analyze_sentiment()

    print("Processed Tokens:", processed_tokens)
    print("Statistics:", statistics)
    print("Sentiment Analysis:", sentiment)
