from stats import get_book_text,  get_word_count, get_char_count, sort_dict

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    words_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    print("============= BOOKBOT ============= ")
    print("Analyzing book found at books/frankenstein")
    print("------------ Word count -----------")
    print(f"{words_count} words found in the document")
    print("-------- Characters count ---------")

main()
