#!/usr/bin/env python3

import requests
import re

from htmldom import htmldom

import argparse

parser = argparse.ArgumentParser(description='Get a verse.')
parser.add_argument('book', type=str, nargs='?',
                    help='book name')
parser.add_argument('chapter', type=str, nargs='?',
                    help='chapter number')
parser.add_argument('verse', type=str, nargs='?',
                    help='verse number')
parser.add_argument('--resume', action='store_true',
                    help='resume switch')

args = parser.parse_args()

if args.book:
	hit = False
	if args.chapter:
		args.chapter = int(args.chapter)
	if args.verse:
		args.verse = int(args.verse)
else:
	args.resume = True
	hit = True

import os

if not os.path.exists('bible'):
	os.mkdir('bible')

with open('order.txt', 'r') as order:
	booklist = order.readlines()


for book_index in range(len(booklist)):
	book = booklist[book_index]
	book = book[:-1]

	if not hit:
		hit = book == args.book
		if not hit:
			continue

	if not os.path.exists('bible/'+book):
		os.mkdir('bible/'+book)
	chapter = 1
	if args.chapter:
		if book == args.book:
			chapter = args.chapter
	while True:
		if not os.path.exists('bible/'+book+'/'+str(chapter)):
			os.mkdir('bible/'+book+'/'+str(chapter))
		verse = 1
		if args.verse:
			if book == args.book:
				if args.chapter == chapter:
					verse = args.verse
		while True:
			try:
				url = "https://www.biblegateway.com/passage/?search="+book+str(chapter)+":"+str(verse)+"&version=ESV"
				response = requests.request("GET", url)
				html_string = response.text

				html_string = re.sub(r'<span style="font-variant: small-caps" class="small-caps">([\w\s]+)<\/span>', lambda m:m.group(1).upper(), html_string)
				
				index = html_string.find('<h3')
				while index != -1:
					end_index = html_string.find('</h3>')
					html_string = html_string[:index] + html_string[end_index+5:]
					index = html_string.find('<h3')

				index = html_string.find('<sup')
				while index != -1:
					end_index = html_string.find('</sup>')
					html_string = html_string[:index] + html_string[end_index+6:]
					index = html_string.find('<sup')

				index = html_string.find('<span class="chapternum">')
				while index != -1:
					end_index = html_string.find('</span>', index)
					html_string = html_string[:index] + html_string[end_index+7:]
					index = html_string.find('<span class="chapternum">')
				dom = htmldom.HtmlDom().createDom(html_string)
				spans = dom.find("span.text")[:-1]
				content = ""
				for span in spans:
					content += span.text()
					content += ' '
				content = re.sub('&nbsp;', '', content)
				content = re.sub('\n', ' ', content)
				content = re.sub(' —', '—', content)
				content = re.sub('— ', '—', content)
				content = re.sub('“', '"', content)
				content = re.sub('”', '"', content)
				content = re.sub('‘', "'", content)
				content = re.sub('’', "'", content)
				content = re.sub(' +', ' ', content)
				content = content.strip()
				if not content:
					break
				output = open('bible/'+book+'/'+str(chapter)+'/'+str(verse)+'.txt', 'w')
				output.write(content)
				output.close()
				print(url)
				if not args.resume and args.verse:
					break
				verse += 1
			except Exception as e:
				try:
					with open('old_bible/'+book+'/'+chapter+'/'+verse+'.txt', 'r') as f1:
						old_text = f1.read()
				except:
					break
		if not args.resume and args.chapter:
			break
		if verse == 1:
			os.rmdir('bible/'+book+'/'+str(chapter))
			break
		if book == "Obadiah" or book == "Philemon" or book == "2 John" or book == "3 John" or book == "Jude":
			break
		chapter += 1
	if not args.resume:
		break

