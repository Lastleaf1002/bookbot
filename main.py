def get_book_text(file_path):
    with open(file_path) as f:
          file_contents = f.read()
    return file_contents

def get_words_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    words = file_contents.split()

    return len(words)


def main():
    # context = get_book_text("books/frankenstein.txt")
    # print(context)
    word_count = get_words_count("books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    return

main()