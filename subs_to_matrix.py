import os
import numpy as np
import json
import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')
stopwords = stopwords.words('spanish')

dir = 'CleanSubs/'
dest = 'data/'

file_texts = {}
tokens_freq = {}
tokens_idx = {}
files_idx = {}

for filename in os.listdir(dir):
  files_idx[filename] = files_idx.get(filename, len(files_idx.items()))
  with open(dir + filename, 'r', encoding='utf-8') as file:
    words = ' '.join([line.split('"')[1] for line in file if len(line.split('"')) > 1]).split(' ')
    words = [word for word in words if word not in stopwords]
    for word in words:
      tokens_freq[word] = tokens_freq.get(word,0) + 1
      tokens_idx[word] = tokens_idx.get(word, len(tokens_idx))
    file_texts[filename] = Counter(words)

with open(dest + 'file_texts.json', 'w', encoding='utf-8') as file_texts_file:
  json.dump(file_texts, file_texts_file)
with open(dest + 'tokens_freq.json', 'w', encoding='utf-8') as tokens_file:
  json.dump(tokens_freq, tokens_file)
with open(dest + 'tokens_idx.json', 'w', encoding='utf-8') as tokens_idx_file:
  json.dump(tokens_idx, tokens_idx_file)
with open(dest + 'files_idx.json', 'w', encoding='utf-8') as files_idx_file:
  json.dump(files_idx, files_idx_file)


print(len(files_idx), len(tokens_idx))
occurrences = np.zeros((len(files_idx), len(tokens_idx)))
for title, counter in file_texts.items():
  print(str(files_idx[title]) + '/' + str(len(files_idx)))
  for word in counter:
    occurrences[files_idx[title], tokens_idx[word]] = counter[word]

np.savetxt(dest + "matrix.txt", occurrences, fmt="%s")
