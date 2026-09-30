# when given a text file, extract text and simulate typing like a human would, with a customiziable delay 

# Easy

# [x] Add input validation back — a bad file path currently crashes with an ugly error
# [x] Let the user set their own base typing speed instead of the hardcoded 0.05–0.09 range
# [x] Add a --help message using argparse so the program is easier to use

# Medium

# [] Random hesitation pauses — with ~5% probability, inject a random long pause mid-sentence regardless of character, as discussed earlier
# [] Typing speed bursts — occasionally shift the base range faster or slower for a stretch of characters to simulate natural rhythm changes
# [] Word-level awareness — pause slightly longer at the start of long words, since people tend to hesitate before complex words

# Harder

# [] Typos — randomly insert a wrong character, then "backspace" and correct it using terminal escape codes
# [x] argparse CLI — replace the input() prompts with proper command line arguments so you can run it like python typewriter.py file.txt --delay 0.07
# [] Colored output — use a library like rich or colorama to add terminal colors




import time
import random
import argparse

parser = argparse.ArgumentParser(description="Simulates human typing from a text file")
parser.add_argument("path", help="path to a .txt file to type out")
parser.add_argument("--delay", type=float, nargs=2, metavar=("MIN", "MAX"), default=[0.05, 0.09], help="min and max delay per character in seconds (default: 0.05 0.09)")
args = parser.parse_args()
min_delay, max_delay = args.delay

if min_delay < 0 or max_delay < 0:
    parser.error("delay values must be non negative")
elif min_delay > max_delay:
    parser.error("The lower delay can not be higher than the upper delay")

def read_file(path):
    """reads the file inputed by the user"""
   
    try:
        if not path.endswith(".txt"):
            parser.error("Please enter a file that ends in .txt")

        with open(path) as f:
            return f.read()
        
    except FileNotFoundError:
        parser.error("Please enter a valid file path")
  
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
text = read_file(args.path)

# types each character with random delay based on character type
for c in text:
    typing_delay = random.uniform(min_delay, max_delay)
    print(c, end='', flush=True)
    time.sleep(get_delay(c, typing_delay))
