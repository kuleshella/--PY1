def get_count_char(string):
    string_alphas = (it.lower() for it in string if it.isalpha())
    result = dict()
    for alpha in string_alphas:
        if alpha in result:
            result[alpha] += 1
        else:
            result[alpha] = 1
    return result


def to_percent(chars):
    total = sum(chars.values())
    return dict(((k, round(v / total * 100, 2)) for k, v in chars.items()))


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
