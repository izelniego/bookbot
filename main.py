def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letter_count_list = convert_dict_to_list(letter_count)
    sorted_letter_count_list = sort_list(letter_count_list)
    print_report(book_path, word_count, sorted_letter_count_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    text = text.lower()
    letter_counts = {}
    for char in text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts

def convert_dict_to_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    return list

def sort_list(list):
    return sorted(list, key=lambda x: x['num'], reverse=True)

def print_report(book_path, word_count, sorted_letter_count_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for letter in sorted_letter_count_list:
        print(f"The letter '{letter['char']}' was found {letter['num']} times")
    print(f"--- End report of {book_path} ---")

if __name__ == "__main__":
    main()