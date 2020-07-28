import subprocess as cmd

def commitWord(filename, word):
  message = 'Adding word: {}'.format(word)
  makeCommitAndPush(filename, message)
  print('commit created and pushed to remote')

def makeCommitAndPush(filename, message):
  command = f"git add {filename} && git commit -m '{message}' && git push"
  cp = cmd.run(command, check=True, shell=True)