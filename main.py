import sys
from stats import character_sort, count_words, repetition_count


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    location = sys.argv[1]

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {location}")
    frankenstein_book = get_book_text(location)

    print("----------- Word Count ----------")
    word_count = count_words(frankenstein_book)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    repetitions = repetition_count(frankenstein_book)
    sorted_count = character_sort(repetitions)
    for char_count in sorted_count:
        if not char_count['char'].isalpha():
            continue
        else:
            print(f"{char_count['char']}: {char_count['num']}")

    print("============= END ===============")

main()
