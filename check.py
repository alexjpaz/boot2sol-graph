import json
import sys
import os

class Expando(object):
      pass

data = Expando()

os.chdir('boot2sol')
os.system('git clean -fd')
os.system('git reset --hard origin/master')

p = os.popen('git log --format=%H', "r")

data.commits = []

while 1:
  line = p.readline()
  if not line: break
  commit = Expando()
  commit.sha = line.strip()


  os.system('git clean -fd')
  os.system('git reset --hard ' + commit.sha)

  commit.message = os.popen("git log --format=%B", "r").read()


  try:

    os.system('head -n $(($(wc -l < "boot.asm") - 2)) "boot.asm"')

    os.system('make')

    commit.size = os.path.getsize('boot.bin')

  except Exception, e:
    commit.error = str(e)

  data.commits.append(commit.__dict__)





with open('../data.json', 'w') as outfile:
  json.dump(data.__dict__, outfile, sort_keys = True, indent = 4, ensure_ascii=False)
