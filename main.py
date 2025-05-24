from stats import get_book_text
from stats import char_count

import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def sort(dict):
    return dict

def count_words(book_path):
    words = get_book_text(book_path).split()
    return len(words)

def main():
    book = sys.argv[1]
    total_words = count_words(book)
    print(f"============ BOOKBOT ============ \n Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    stats = char_count(book)
    for letter in stats:
        print(letter + ": " + str(stats[letter]))

    print("============= END ===============")

if __name__ == "__main__":
    main()