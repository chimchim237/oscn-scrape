#html-to-list1.py
import urllib2, obo

url = 'http://www.oscn.net/dockets/GetCaseInformation.aspx?db=cleveland&number=CM-2009-1168&cmid=2016678'

response = urllib2.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower() #add the string method here.
wordlist = text.split()

print(wordlist)