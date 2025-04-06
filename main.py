from stats import count_words

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = len(count_words(book_text))
    print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()