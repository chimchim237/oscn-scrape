#html-to-list1.py
import urllib2, obo

url = 'file:///Users/Carlos/Desktop/OSCN%20Case%20Details.html'

response = urllib2.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)

print(wordlist)
