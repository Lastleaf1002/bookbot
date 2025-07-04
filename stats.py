def get_book_text(file_path):
    with open(file_path) as f:
          file_contents = f.read()
    return file_contents

def get_words_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    words = file_contents.split()

    return len(words)

def get_characters_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    characters = {}
    for c in file_contents:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters

