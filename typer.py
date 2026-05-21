# when given a text file, extract text and simulate typing like a human would, with a customiziable delay 

# Easy

# [x] Add input validation back — a bad file path currently crashes with an ugly error
# [x] Let the user set their own base typing speed instead of the hardcoded 0.05–0.09 range
# [] Add a --help message using argparse so the program is easier to use

# Medium

# [] Random hesitation pauses — with ~5% probability, inject a random long pause mid-sentence regardless of character, as discussed earlier
# [] Typing speed bursts — occasionally shift the base range faster or slower for a stretch of characters to simulate natural rhythm changes
# [] Word-level awareness — pause slightly longer at the start of long words, since people tend to hesitate before complex words

# Harder

# [] Typos — randomly insert a wrong character, then "backspace" and correct it using terminal escape codes
# [] argparse CLI — replace the input() prompts with proper command line arguments so you can run it like python typewriter.py file.txt --delay 0.07
# [] Colored output — use a library like rich or colorama to add terminal colors

#C:\Users\gsher\Desktop\abcd.txt


import time
import random

def read_file():
    """reads the file inpurted by the user"""
    while True:
        try:
            path = input("Enter the text file path: ")
            if not path.endswith(".txt"):
                print("Please enter a .txt file")
                continue
            with open(path) as f:
                return f.read()
            
        except FileNotFoundError:
            print("Please enter a valid path")
  
def get_delay(char_type, delay):
    """Gets delay depending on character being read"""
    if char_type == " ":
        return delay / 2
    elif char_type == ";" or char_type == ",":
        return 3 * (delay + random.uniform(0, 0.3))
    elif char_type == "." or char_type == "!" or char_type == "?":
        return 7 * (delay + random.uniform(0, 0.2))
    elif char_type == "\n":
        return random.uniform(0.7, 1.4)
    else:
        return delay

# opens the text file and reads it
text = read_file()

# user chooses typing delay
while True:
    try:
        user_typing_delay = input("Choose a typing delay range separated by a comma (example: '0.05, 0.09') ")
        if user_typing_delay == "default":
            min_delay = 0.05
            max_delay = 0.09
        else:
            user_typing_delay = user_typing_delay.split(", ")
            min_delay = float(user_typing_delay[0])
            max_delay = float(user_typing_delay[1])
        try:
            if input("Enable random typos? (y/n)") == "y".strip():
                typo_check = True
            else:
                typo_check = False
        except (ValueError):
            print("Please enter 'y' or 'n'")
        break
    except (ValueError, IndexError):
        print("Please enter two valid numbers separated by a comma")




# types each character with random delay based on character type
for c in text:
    typing_delay = random.uniform(min_delay, max_delay)
    print(c, end='', flush=True)
    time.sleep(get_delay(c, typing_delay))
