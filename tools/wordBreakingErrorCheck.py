from itertools import islice
import subprocess

# command line options
prompt_string = 'Yes (y) | No (n) | Maybe (m) | Quit (q)?\n'
yes_option = ['yes', 'y']
no_option = ['no', 'n']
maybe_option = ['maybe', 'm']
quit_option = ['quit', 'q']
acceptable_answers = yes_option + no_option + maybe_option + quit_option

# files
input_filename = "../stats/wordBreakingErrors"
replacements_filename = '../scripts/Sources/stringReplacer/replacements'
approvelist_filename = '../scripts/Sources/wordBreakingValidator/approveList'

# utility methods
def next_n_lines(file_opened, N = 4):
    return [x.strip() for x in islice(file_opened, N)]

def do_yes_things(text, suggestion):
  with open(replacements_filename, "a") as file_obj:
    file_obj.write(f"{text}\t{suggestion}\n")
    print('word: {} added to file: {}'.format(suggestion, replacements_filename))

def do_no_things(text):
  with open(approvelist_filename, "a") as file_obj:
    file_obj.write(f"{text}\n")
    print('word: {} added to file: {}'.format(suggestion, approvelist_filename))

def do_maybe_things():
  pass

# run command line script
with open(input_filename) as file_obj:

    # ignore first two lines of wordBreakingErrors
    next_n_lines(file_obj, 2)

    # read one wordBreakingError object from the file and show options
    arr = next_n_lines(file_obj)
    while len(arr) == 4:
      empty_line = arr[0]
      text = arr[1].split(': ')
      suggestion = arr[2].split(': ')
      frequency = arr[3].split(': ')
      
      print('Text: {}, Suggestion: {}, Frequency {}'.format(text[1], suggestion[1], frequency[1]))
      
      answer = input(prompt_string)
      while answer not in acceptable_answers:
        answer = input(prompt_string)
      
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
