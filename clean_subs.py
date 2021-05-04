import os

dir = 'Subs/'

for filename in os.listdir(dir):
  with open(dir + filename, 'r', encoding='utf-8') as file:
    lines = []
    for idx, line in enumerate(file):
      if (idx > 7):
        if (idx % 8 == 0):
          split = line.split(' ')
          begin = split[0] if len(split) > 0 else ''
          end = split[2] if len(split) > 2 else ''
        if (idx % 8 == 1) and begin and end and len(line[:-1]) > 0:
          lines.append(begin + ',' + end + ',"' + line[:-1] + '"\n')
  with open('CleanSubs/' + filename, 'w', encoding='utf-8') as file:
    file.write(''.join(lines))