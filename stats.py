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
        