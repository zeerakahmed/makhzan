from itertools import islice
import subprocess
import sys
import tty
import termios

# command line options
yes_option = ['y']
no_option = ['n']
maybe_option = ['m']
quit_option = ['q']
acceptable_keys = yes_option + no_option + maybe_option + quit_option

# files
input_filename = "../stats/wordBreakingErrors"
replacements_filename = '../scripts/Sources/stringReplacer/replacements'
approvelist_filename = '../scripts/Sources/wordBreakingValidator/approveList'

# utility methods
def next_n_lines(file_opened, N = 4):
    return [x.strip() for x in islice(file_opened, N)]

def read_single_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def clear_lines(n):
    for _ in range(n):
        sys.stdout.write('\x1b[1A\x1b[2K')

def do_yes_things(text, suggestion):
  with open(replacements_filename, "a") as file_obj:
    file_obj.write(f"{text}\t{suggestion}\n")

def do_no_things(text):
  with open(approvelist_filename, "a") as file_obj:
    file_obj.write(f"{text}\n")

def do_maybe_things():
  pass

# run command line script
DISPLAY_LINES = 2  # "Text/Suggestion/Frequency" line + prompt line

with open(input_filename) as file_obj:

    # ignore first two lines of wordBreakingErrors
    next_n_lines(file_obj, 2)

    first = True
    arr = next_n_lines(file_obj)
    while len(arr) == 4:
      empty_line = arr[0]
      text = arr[1].split(': ')
      suggestion = arr[2].split(': ')
      frequency = arr[3].split(': ')

      if not first:
          clear_lines(DISPLAY_LINES)
      first = False

      print('Text: {}, Suggestion: {}, Frequency: {}'.format(text[1], suggestion[1], frequency[1]))
      print('Yes (y) | No (n) | Maybe (m) | Quit (q)? ', end='', flush=True)

      answer = read_single_key().lower()
      while answer not in acceptable_keys:
          answer = read_single_key().lower()

      print(answer)

      if answer in quit_option:
        break

      if answer in yes_option:
        do_yes_things(text[1], suggestion[1])

      if answer in no_option:
        do_no_things(text[1])

      if answer in maybe_option:
        do_maybe_things()

      arr = next_n_lines(file_obj)

# These next two methods are to automatically commit everytime a decision is made using the command line tools.
# At the moment we are not using them. All changes require a manual commit.

def commitWord(filename, word):
  message = 'Adding word: {}'.format(word)
  makeCommitAndPush(filename, message)
  print('commit created and pushed to remote')

def makeCommitAndPush(filename, message):
  command = f"git add {filename} && git commit -m '{message}' && git push"
  cp = subprocess.run(command, check=True, shell=True)
