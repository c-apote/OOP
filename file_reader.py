#from pathlib import Path

#path = Path('pi_digits.txt')
#contents = path.read_text()
#print(contents)

with open('pi_digits.txt', 'rt') as f: # opens the file in to memory, named 'f'
    contents = f.read()                # using read 'method' to read the file and pass t to a variable called 'contents'
    print(contents)                    # use print function, to display the contents to the screen