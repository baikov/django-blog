ignor_chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
cyr_to_lat = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
              'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
              'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
              'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
              'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'i', 'ь': '',
              'э': 'e', 'ю': 'yu', 'я': 'ya'
              }


def custom_slugify(model, string):
    result = string.lower()
    for char in set(result):
        if char not in set(cyr_to_lat.keys()) | ignor_chars:
            result = result.replace(char, ' ')
        elif char in cyr_to_lat.keys():
            result = result.replace(char, cyr_to_lat[char])

    result = '-'.join(word for word in result.split(' ') if len(word) > 0)

    slug_text = result
    count = 1
    while(model._default_manager.filter(slug=result).exists()):
        result = '{0}-{1}'.format(slug_text, count)
        count += 1

    return result
