# main.py
# Простая программа: проверка, является ли слово палиндромом

def is_palindrome(word: str) -> bool:
    # Удаляем пробелы и приводим к нижнему регистру
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    word = input("Введите слово: ")
    print("Палиндром" if is_palindrome(word) else "Не палиндром")
