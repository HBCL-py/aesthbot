import urllib.request
import urllib.parse
import re

def ytsearch(q):
    query_string = urllib.parse.urlencode(q)
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return search_results
