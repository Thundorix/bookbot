def main():
    path_to_file = "books/frankenstein.txt"
    text = readtext(path_to_file)
    total_words = word_count(text)
    char_dict = count_char(text)
    #print(text)
    #print(f"Total Words: {total_words}")
    print(char_dict)

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

main()