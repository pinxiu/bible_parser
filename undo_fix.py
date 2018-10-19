from json import load
import os
import re

with open('ESV.json', 'r') as book:
	data = load(book)

for book in data:
	for chapter in data[book]:
		for verse in data[book][chapter]:
			try:
				with open('old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f1:
					old_text = f1.read()
				with open('bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f2:
					new_text = f2.read()
			except:
				continue
			# content = new_text
			if 'GOD.' in new_text:
				print("old text:")
				print(old_text)
				print("new_text")
				print(new_text)
				y = input("change?")
				# new_text =  re.sub('GOD\.', '', new_text, 1)
				if y:
					content = re.sub('GOD\.', y, new_text, 1)
					with open('bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f2:
						f2.write(content)
					print(content)
				print()
				# new_text = content

