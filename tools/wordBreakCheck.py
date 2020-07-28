from itertools import islice
from commit import commitWord

prompt_string = 'Yes(y) | No(n) | Maybe(m) | Quit (q)?\n'

yes_option = ['yes', 'y']
no_option = ['no', 'n']
maybe_option = ['maybe', 'm']
quit_option = ['quit', 'q']

input_filename = "tst"
replacements_filename = '../scripts/Sources/stringReplacer/replacements'
approvelist_filename = '../scripts/Sources/wordBreakingValidator/approveList'

acceptable_answers = yes_option + no_option + maybe_option + quit_option

def next_n_lines(file_opened, N = 4):
    return [x.strip() for x in islice(file_opened, N)]

def do_yes_things(word, suggestion):
  with open(replacements_filename, "a") as file_obj:
    file_obj.write(f"{suggestion}{word} ")
    file_obj.write('\n')
    print('word: {} added to file: {}'.format(suggestion, replacements_filename))

  with open(approvelist_filename, "a") as file_obj:
    file_obj.write(suggestion)
    file_obj.write('\n')
    print('word: {} added to file: {}'.format(suggestion, approvelist_filename))

def do_no_things():
  pass

def do_maybe_things():
  pass


with open(input_filename) as file_obj:
    next_n_lines(file_obj, 2)
   
    arr = next_n_lines(file_obj)
    while len(arr) == 4:
      empty_line = arr[0]
      text = arr[1].split(':')
      suggestion = arr[2].split(':')
      frequency = arr[3].split(':')
      
      print('Text: {}, Suggestion: {}, Frequency {}'.format(text[1], suggestion[1], frequency[1]))
      print('\n\n')
      
      answer = input(prompt_string)
      while answer not in acceptable_answers:
        answer = input(prompt_string)
      
      if answer in quit_option:
        break
      
      if answer in yes_option:
        do_yes_things(text[1], suggestion[1])
      
      if answer in no_option:
        do_no_things()
      
      if answer in maybe_option:
        do_maybe_things()
      
      arr = next_n_lines(file_obj)
