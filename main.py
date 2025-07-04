from stats import get_words_count, get_characters_count, get_sorted_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(context)
    word_count = get_words_count(text)
    # print(f"{word_count} words found in the document")

    char_count = get_characters_count(text)
    # print(char_count)

    sorted_dicts = get_sorted_dict(char_count)
    # print(sorted_dicts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_dicts:
         if d["name"].isalpha():
             print(f"{d["name"]}: {d["num"]}")
    print("============= END ===============")

    return

def get_book_text(file_path):
    with open(file_path) as f:
          file_contents = f.read()
    return file_contents

main()