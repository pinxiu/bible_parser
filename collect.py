import os
import json

data = dict()

path = "bible/"

for book in os.listdir(path):
	data[book] = dict()
	for chapter in os.listdir(path + book + '/'):
		data[book][chapter] = dict()
		for verse in os.listdir(path + book + '/' + chapter + '/'):
			with open(path + book + '/' + chapter + '/' + verse, 'r') as v:
				data[book][chapter][verse[:-4]] = v.read()

output = json.dumps(data)

with open('ESV_updated.json', 'w') as f:
	f.write(output)


# for book in booklist:
# # for book in["Mark"]:
# 	book = book[:-1]
# 	for chapter in data[book]:
# 		for verse in data[book][chapter]:
# 			url = "https://www.biblegateway.com/passage/?search="+book+chapter+":"+verse+"&version=ESV"
# 			# print(url)
# 			try:
# 				with open(prefix+'old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f1:
# 					old_text = f1.read()
# 			except:
# 				continue
# 			try:
# 				with open(prefix+'bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f2:
# 					new_text = f2.read()
# 			except:
# 				new_text = ''
			
# 			if old_text != new_text:
# 				sm = difflib.SequenceMatcher(None, old_text, new_text)
# 				old_string, new_string = show_diff(sm)
# 				return index.html_string(old_text=old_string,
# 	new_text=new_string, book=book, chapter=chapter, verse=verse, url=url
# 	)
