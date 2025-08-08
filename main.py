import sys
from stats import count_words, sort_dict


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict_list = sort_dict(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in char_dict_list:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")



def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


main()

