def get_words_count(text):
    words = text.split()
    return len(words)

def get_characters_count(text):
    characters = {}
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters

