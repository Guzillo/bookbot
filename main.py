from stats import get_book_text,  get_word_count, get_char_count, sort_dict
def print_char_count_dict(char_count_dict):
    for entry in char_count_dict:
        if(f"{entry["char"]}".isalpha()):
            print(f"{entry["char"]}: {entry["num"]}")

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    words_count = get_word_count(book_text)
    char_count_dict = get_char_count(book_text)
    char_count_dict = sort_dict(char_count_dict)
    print("============= BOOKBOT =============")
    print("Analyzing book found at books/frankenstein...")
    print("------------ Word count -----------")
    print(f"Found {words_count} total words")
    print("-------- Characters count ---------")
    print_char_count_dict(char_count_dict)
    print("=============== END ===============")
main()
