def main():
    path_to_file = "books/frankenstein.txt"
    text = readtext(path_to_file)
    total_words = word_count(text)
    char_dict = count_char(text)
    letter_count = count_letters(char_dict)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{total_words} words found in the document")
    print("")
    for i in letter_count:
        print(f"The '{i['ch']}' character was found {i['count']} times")
    print("--- End report ---")


def word_count(text):
    words = text.split()
    return len(words)

def readtext(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_char(text):
    char_dict = {}
    for ch in text.lower():
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    return char_dict

def count_letters(char_dict):
    letter_count = []
    for i in char_dict:
        if i.isalpha():
            letter_count.append({"ch": i, "count": char_dict[i]})
    letter_count.sort(reverse=True, key=lambda x: x["count"])
    return letter_count


main()