from stats import get_words_count, get_characters_count

def main():
    # context = get_book_text("books/frankenstein.txt")
    # print(context)
    word_count = get_words_count("books/frankenstein.txt")
    print(f"{word_count} words found in the document")

    char_count = get_characters_count("books/frankenstein.txt")
    print(char_count)
    return

main()