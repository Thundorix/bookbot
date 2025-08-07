def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_text = text.lower()
    char_dict = {}
    for ch in lower_text:
        if ch not in char_dict:
            char_dict[ch] = 1
        else:
            char_dict[ch] += 1
    return char_dict


def sort_on(items):
    return items["num"]

def sort_dict(text):
    char_dict = count_characters(text)
    char_dict_list = []
    for k in char_dict:
        if k.isalpha():
            key_dict = {"char": k, "num": char_dict[k]}
            char_dict_list.append(key_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    print(char_dict_list)
