"""
<< Какую букву написать?> m
*      *
**    **
* *  * *
*  **  *
*      *
*      *
*      *
*      *

hardconfig -- передача в коде числовых данных или данных отображения (например буквы в нашем случае)
mvp        -- minial viable product (минимальный функционал программы которую можно показать и проверить соответствие требованиям)
validation -- проверка различных сценариев использования
"""
from symbol_builders import get_symbol_builder
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Функция '{func.__name__}' выполнена  за {elapsed_time:.6f} second.")
        return result
    return wrapper

def main():
    while True:
        requested_text = input("Введи текст который нужно напечатать(или 'exit' для выхода):")
        if requested_text.lower() == "exit":
            break
        print_text(requested_text)

@timeit
def print_text(text: str) -> None:
    text_rows = get_text_rows(text)
    print('\n'.join(text_rows))


def print_letter(letter: str) -> None:
    letter_rows = get_letter_rows(letter)
    print('\n'.join(letter_rows))


def get_text_rows(text: str) -> list[str]:
    text_rows: list[str] = []
    for letter in text:
        if len(text_rows) == 0:
            text_rows = get_letter_rows(letter)
        else:
            text_rows = merge_letter_rows(text_rows, get_letter_rows(letter))
    return text_rows


def merge_letter_rows(letter_rows1: list[str], letter_rows2: list[str]) -> list[str]:
    merged_rows: list[str] = []
    for row_ind in range(len(letter_rows1)):
        merged_rows.append(
            letter_rows1[row_ind] + ' ' + letter_rows2[row_ind]
        )
    return merged_rows


def get_letter_rows(letter: str) -> list[str]:
    letter_builder = get_symbol_builder(letter)
    letter_rows = letter_builder()
    return letter_rows


if __name__ == '__main__':
    main()