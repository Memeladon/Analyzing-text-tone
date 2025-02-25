import matplotlib
matplotlib.use('Agg')  # Установка неинтерактивного режима
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Пример данных
russian_sentence_lengths = np.random.normal(20, 5, 100)  # Средняя длина 20 слов
english_sentence_lengths = np.random.normal(15, 4, 100)  # Средняя длина 15 слов

# Построение графика
sns.kdeplot(russian_sentence_lengths, label='Русские тексты', shade=True)
sns.kdeplot(english_sentence_lengths, label='Английские тексты', shade=True)
plt.title('Распределение длины предложений')
plt.xlabel('Длина предложений (слова)')
plt.ylabel('Плотность')
plt.legend()
# Сохранение графика в файл
plt.savefig('f2.png')