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

def sort_on(items):
    return items["num"]

def get_sorted_dict(flat_dict):
    sorted_dicts = []
    for c in flat_dict:
        dict = {"name":c, "num":flat_dict[c]}
        sorted_dicts.append(dict)

    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts
