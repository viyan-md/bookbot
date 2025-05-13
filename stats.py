def sort_on(dict, key):
    return dict[key]

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def get_book_wordcount(text):
    return len(text.split())
    
def get_char_count(text):
    char_count = dict()
    output_lines = []
    
    for char in text:
        if char.isalpha():
            char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    sorted_by_values = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    for key in sorted_by_values:
        output_lines.append(f"{key}: {sorted_by_values[key]}")
    
    output_string = "\n".join(output_lines)

    return output_string

def print_report(path):

    text = get_book_text(path)
    word_count = get_book_wordcount(text)
    char_count = get_char_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(char_count)
