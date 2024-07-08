def main():
    path_to_file = "books/frankenstein.txt"
    text = readtext(path_to_file)
    total_words = word_count(text)
    print(text)
    print(f"Total Words: {total_words}")

def word_count(text):
    count = 0
    words = text.split()
    return len(words)

def readtext(path_to_file):
    with open(path_to_file) as f:
        return f.read()



main()