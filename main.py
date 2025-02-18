def main():
    with open("./books/book.txt") as f:
        word_counter = 0
        file_contents = f.read()
        print(file_contents)
        for word in file_contents.split():
            word_counter += 1
        print(word_counter)
        return word_counter











main()