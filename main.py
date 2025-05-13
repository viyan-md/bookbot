import sys
import stats

def main():
    path = sys.argv[1]

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    stats.print_report(path)

main()
