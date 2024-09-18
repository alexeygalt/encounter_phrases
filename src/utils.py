from aiogram.exceptions import TelegramBadRequest


def search_word_in_phraseological_list(data_list, word):
    """
    Ищет слово в списке строк и возвращает список строк, содержащих это слово.

    :param data_list: Список строк для поиска
    :param word: Слово для поиска
    :return: Список строк, содержащих слово
    """

    word = word.lower()

    result = [item for item in data_list if word in item.lower()]

    return result


async def send_long_message(answer_func, text: str, **kwargs):
    max_length = 4096
    for i in range(0, len(text), max_length):
        try:
            await answer_func(text[i:i + max_length], **kwargs)
        except TelegramBadRequest:
            print("Ошибка: сообщение слишком длинное для отправки.")
            break