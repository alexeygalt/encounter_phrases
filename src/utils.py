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
