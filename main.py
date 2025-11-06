import sys
from stats import get_num_words, each_char_count, sorted_char_num

def get_book_test(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_test(f"{book_path}")


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")

    word_count = get_num_words(book)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_count = each_char_count(book)
    sorted_char_count_list = sorted_char_num(char_count)
    for char_count in sorted_char_count_list:
        if char_count["char"].isalpha() == True:
            char = char_count["char"]
            count = char_count["num"]
            print(f"{char}: {count}")
    print("============= END ===============")

main()