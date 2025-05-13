def sort_on(dict, key):
    return dict[key]

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def get_book_wordcount(text):
    num_words = len(text.split())
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def get_char_count(text):
    char_count = dict()
    
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    sorted_by_values = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    print("--------- Character Count -------")
    for key in sorted_by_values:
        print(f"{key}: {sorted_by_values[key]}")

