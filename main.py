from stats import get_words_count, get_characters_count

def main():
    text = get_book_text("books/frankenstein.txt")
    # print(context)
    word_count = get_words_count(text)
    print(f"{word_count} words found in the document")

    char_count = get_characters_count(text)
    print(char_count)
    return

def get_book_text(file_path):
    with open(file_path) as f:
          file_contents = f.read()
    return file_contents

main()