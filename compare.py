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
				print("##########################")
				print(book+' '+chapter+':'+verse)
				print("old_text is:")
				print(old_text)
				print("new_text is:")
				print(new_text)
				change = input("which file do you want to change? (1=old, 2=new, 3=both): ")
				if change == '1':
					with open('old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f1:
						f1.write(new_text)
						print("updated old bible")
				elif change == '2':
					with open('bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f2:
						f2.write(old_text)
						print("updated new bible")
				elif change == '3':
					new_version = input("Enter the new version here: ")
					with open('old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f1:
						f1.write(new_version)
					with open('bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f2:
						f2.write(new_version)
						print("updated both old and new bibles")
				print("##########################")
				print()
				print()


