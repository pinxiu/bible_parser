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
			if old_text != new_text:
				content = new_text
				content = re.subn('&nbsp;', '', content)[0]
				content = re.subn('— ', '—', content)[0]
				content = re.subn('God ,', 'GOD,', content)[0]
				content = re.subn('God \.', 'GOD.', content)[0]
				content = content.strip()
				# print("old text:")
				# print(new_text)
				# y = input("change?")
				# if y == '':
				with open('bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f2:
					f2.write(content)
				# 	print(content)
				# print()
