def main():
    with open("./books/book.txt") as f:
        word_counter = 0
        file_contents = f.read()
        print(file_contents)
        for word in file_contents.split():
            word_counter += 1
        return word_counter
def letter_counter():
    letter_dict = {}
    with open("./books/book.txt") as f:
        file_contents = f.read()
        for letter in str(file_contents).lower():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict

def letter_printer():
    letter_dict = letter_counter()
    for letter in letter_dict:
        if letter.isalpha() == True:
            print("The '" + letter + "' character was found " + str(letter_dict[letter]) + " times")

letter_printer()
main()
