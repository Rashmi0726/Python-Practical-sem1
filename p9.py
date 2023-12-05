'''WAP to read a file 
a. Print the total number of characters, words and lines in the file.
b. Calculate the frequency of each character in the file.
Use a variable of dicti type to maintain the count.
c. Print the words in reverse order.
d. Copy even lines of the file to a file named 'File1' and 
odd lines to another 1 named 'File2'.'''


def fun1(Myfile):
    # a. Print the total number of characters, words, and lines in the file.
    with open(Myfile, 'r') as file:
        content = file.read()
        char_count = len(content)
        word_count = len(content.split())
        line_count = content.count('\n') + 1

        print(f"Total Characters: {char_count}")
        print(f"Total Words: {word_count}")
        print(f"Total Lines: {line_count}")

        # b. Calculate the frequency of each character in the file.
        char_frequency = {}
        for char in content:
            if char.isalnum():
                char_frequency[char] = char_frequency.get(char, 0) + 1

        print("\nCharacter Frequencies:")
        for char, freq in char_frequency.items():
            print(f"{char}: {freq}")

        # c. Print the words in reverse order.
        words = content.split()
        reversed_words = ' '.join(reversed(words))
        print("\nWords in Reverse Order:")
        print(reversed_words)

        # d. Copy even lines to 'File1' and odd lines to 'File2'.
        with open('File1', 'w') as file1, open('File2', 'w') as file2:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    file1.write(line + '\n')
                else:
                    file2.write(line + '\n')

Myfile=input("Enter your text file:")
fun1(Myfile)
