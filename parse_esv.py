from json import load
import os
import re

with open('ESV.json', 'r') as book:
	data = load(book)

if not os.path.exists('old_bible'):
	os.mkdir('old_bible')

for book in data:
	if not os.path.exists('old_bible/'+book):
		os.mkdir('old_bible/'+book)
	for chapter in data[book]:
		if not os.path.exists('old_bible/'+book+'/'+chapter):
			os.mkdir('old_bible/'+book+'/'+chapter)
		for verse in data[book][chapter]:
			with open('old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as output:
				content = data[book][chapter][verse]
				content = re.sub('--', '—', content)
				output.write(content)

