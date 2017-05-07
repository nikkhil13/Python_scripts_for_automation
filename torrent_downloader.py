from __future__ import unicode_literals
import os
import requests
import re
from bs4 import BeautifulSoup
from tabulate import tabulate
import re
import sys
import urllib
import urllib2
import subprocess

import win_unicode_console as wp
wp.enable()

download_url = 'https://ukpirateproxy.xyz'

def ask_user():
	movie_name = raw_input("What do you want to search?\n")
	movie_name = movie_name.replace(" ","+")
	url = 'https://ukpirateproxy.xyz/s/?q='
	url = url + movie_name +'&page=0&orderby=99'
	return url


def start_download(torrent_no):

	final_url = download_url + torrent_no
	
	try:
		dconn = requests.get(final_url)
		if(dconn.status_code == 200):
			print 'Proceeding to download!!'
		else:
			print 'Please check your internet connection!'

	except Exception, e:
		print str(e)

	soup = BeautifulSoup(dconn.content, 'html.parser')

	link = soup.find('a', attrs = {'title':'Get this torrent'})['href']

	with open('test.txt','w') as output:
	 	output.write(link)

	'''In the text.txt file, you will find a magnet link. 
	   Copy the entire link and paste in your bittorent client to start the download. 
	   However, this process can also be automated using selenium which I\'ll be trying in the future.'''


	print 'Done !'
	# # res = urllib.request.urlretrieve(link,"demo.torrent")
	# # print res

	# info_hash = link[20:60]
	# print info_hash

	# download_link = 'http://thetorrent.org/' + info_hash + '.torrent'
	# print download_link
	# #fname = download_torrent(download_link)
	# fconn = requests.get(download_link)
	# print fconn.status_code
	# final_soup = BeautifulSoup(fconn.content, 'html.parser')

	# k = final_soup.find('div', attrs = {'class':'well text-center'})
	# print k
	# res = urllib.urlretrieve(k,"demo.torrent")
	# print res
	# #fname = download_torrent(k)
	# mp3file = urllib2.urlopen(k)
	# with open('test.torrent','wb') as output:
	# 	output.write(mp3file.read())

	# fname = os.getcwd() + '\\test.torrent' 
	# subprocess.Popen(['xdg-open', fname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
def begin_here(url):
	try:
		conn = requests.get(url)
		if(conn.status_code == 200):
			print 'Connected....Searching for torrent!!'
		else:
			print 'Please check your internet connection!'
	except Exception as e:
		print str(e)

	if re.findall(r'No hits',str(conn.content)):
		print 'No torrents found. Check your query. Please do not make spelling mistakes.'
	else:
		print 'Searching..'
		soup = BeautifulSoup(conn.content, 'html.parser')

		titles = [s.text for s in soup.find_all('div',attrs = {'class':'detName'})]

		href = []

		for s in soup.find_all('a', attrs = {'title':'Download this torrent using magnet'}):
			href.append(s['href'])


		details = [s.text for s in soup.find_all('font', attrs = {'class':'detDesc'})]

		seed_and_leech = [s.text for s in soup.find_all('td',attrs = {'align':'right'})]
			
		seeders = seed_and_leech[::2]

		leechers = seed_and_leech[1::2]

		final_table = [[i+1,titles[i],details[i],seeders[i],leechers[i]] for i in range(len(titles))]

		headers = ["No", "Title","Details","Seeders","Leechers"]
		print(tabulate(final_table,headers))

		torrent_no = raw_input("Enter the torrent number that you wish to download or 'Q' to search again -- ")
		if torrent_no == 'Q' or torrent_no == 'q':
			url = ask_user()
			begin_here(url)
		elif int(torrent_no) < 1 or int(torrent_no) > len(href):
			print "Don't try to be a smartass"
		else:
			start_download(href[int(torrent_no)-1])

if __name__ == '__main__':
	url = ask_user()
	begin_here(url)


