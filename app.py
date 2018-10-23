from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

from json import load
import os
import re

# prefix = "test/"
prefix = ""

with open('ESV.json', 'r') as book:
	data = load(book)

import difflib
def show_diff(seqm):
    """Unify operations between two compared strings
seqm is a difflib.SequenceMatcher instance whose a & b are strings"""
    output1= []
    output2= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output1.append(seqm.a[a0:a1])
            output2.append(seqm.b[b0:b1])
        elif opcode == 'insert':
            output2.append("<ins style='color:red;'>[" + seqm.b[b0:b1] + "]</ins>")
        elif opcode == 'delete':
            output1.append("<del style='color:red;'>[" + seqm.a[a0:a1] + "]</del>")
        elif opcode == 'replace':
            output1.append("<mark style='color:red;'>[" + seqm.a[a0:a1] + "]</mark>")
            output2.append("<mark style='color:red;'>[" + seqm.b[b0:b1] + "]</mark>")
        else:
            pass
    return ''.join(output1), ''.join(output2)

from templates import index

with open('order.txt', 'r') as order:
	booklist = order.readlines()

@app.route("/compare")
def compare():

	for book in booklist:
	# for book in["Mark"]:
		book = book[:-1]
		for chapter in data[book]:
			for verse in data[book][chapter]:
				url = "https://www.biblegateway.com/passage/?search="+book+chapter+":"+verse+"&version=ESV"
				# print(url)
				try:
					with open(prefix+'old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f1:
						old_text = f1.read()
				except:
					continue
				try:
					with open(prefix+'bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f2:
						new_text = f2.read()
				except:
					new_text = ''
				
				if old_text != new_text:
					sm = difflib.SequenceMatcher(None, old_text, new_text)
					old_string, new_string = show_diff(sm)
					return index.html_string(old_text=old_string,
		new_text=new_string, book=book, chapter=chapter, verse=verse, url=url
		)
	return "You are done."

@app.route("/change_old/<book>/<chapter>/<verse>")
def change_old(book, chapter, verse):
	with open(prefix+'bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f2:
		new_text = f2.read()
	with open(prefix+'old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f1:
		f1.write(new_text)
	return redirect("/compare")

@app.route("/change_new/<book>/<chapter>/<verse>")
def change_new(book, chapter, verse):
	with open(prefix+'old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f1:
		old_text = f1.read()
	with open(prefix+'bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f2:
		f2.write(old_text)
	return redirect("/compare")

@app.route("/change_both/<book>/<chapter>/<verse>", methods=["POST"])
def change_both(book, chapter, verse):
	text = request.form['user_text']
	with open(prefix+'old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f1:
		f1.write(text)
	with open(prefix+'bible/'+book+'/'+chapter+'/'+verse+'.txt', 'w') as f2:
		f2.write(text)
	return redirect("/compare")
