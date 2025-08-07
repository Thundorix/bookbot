from stats import count_words, count_characters, sort_dict

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    #print(count_characters(text))
    sort_dict(text)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()

