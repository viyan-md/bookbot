import sys
import stats

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = stats.get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    
    stats.get_book_wordcount(text)
    stats.get_char_count(text)

    sys.exit(0)

main()
