def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letter_count_list = convert_dict_to_list(letter_count)
    letter_count_list.sort(reverse=True, key=sort_on)
    #print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    #print(f"Character count: {letter_count}")  
    for letter in letter_count_list:
        print(f"The letter '{letter['char']}' was found {letter['num']} times")
    print(f"--- End report of {book_path} ---")    


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

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "num": dict[key]})
    return list

main()