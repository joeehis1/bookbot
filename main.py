#! /home/katsura/anaconda3/bin/python
from stats import get_book_text,count_text,count_chars,create_report,display_report
from sys import argv,exit


def main():
    script,f = None, None
    if(len([*argv]) <= 1):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        return

    [script,f] = argv

    # print(get_book_text(filename))
    book_text = get_book_text(f)
    num_words = count_text(book_text)
    char_dictionary = count_chars(book_text)
    list_from_dict = create_report(char_dictionary)
    print(f"Found {num_words} total words")
    display_report(list_from_dict)

main()


