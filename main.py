import os
import sys
import re
import urllib2
from pytube import YouTube
reload(sys)  
sys.setdefaultencoding('utf8')
git_arguments = sys.argv[2:]
number = int(sys.argv[1])
url = "https://www.youtube.com/results?search_query="
filename = ""
for args in git_arguments:
	url = url + args + "+"
	filename = filename + args
url = url[:-1]
search_headers = urllib2.urlopen(url)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', search_headers.read().decode())
result = "https://www.youtube.com/watch?v=" + search_results[number]
print result
os.system("pytube " + result)
