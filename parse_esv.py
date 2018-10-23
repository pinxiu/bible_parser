from json import load
import os

with open('ESV_updated.json', 'r') as book:
	data = load(book)

if not os.path.exists('esv_bible'):
	os.mkdir('esv_bible')

for book in data:
	with open('esv_bible/'+book + '.txt', 'w') as output:
		output.write(book)
		output.write('\n\n\n')
		for chapter in sorted(data[book], key=lambda x:int(x)):
			output.write('Chapter ')
			output.write(chapter)
			output.write('\n\n')
			for verse in sorted(data[book][chapter], key=lambda x:int(x)):
				content = data[book][chapter][verse]
				output.write(verse)
				output.write(' ')
				output.write(content)
				output.write('\n')
			output.write('\n')
			output.write('\n')
		output.write('\n')
