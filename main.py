import re
import urllib2
import HTMLParser

url = "http://google.com"

response = urllib2.urlopen(url)
output = response.read()

# remove style tags
output = re.sub(re.compile('<style.*?>.*?</style.*?>', re.DOTALL), '', output)

# remove script tags
output = re.sub(re.compile('<script.*?>.*?</script.*?>', re.DOTALL), '', output)

#convert common char codes to letters
parser = HTMLParser.HTMLParser()
output = parser.unescape(output)

# strip tags
output = re.sub('<.*?>', '\n', output)

# remove double spaces
output = re.sub(' +', ' ', output)

# remove double linebreaks
lines = output.split("\r")
lines = [x for x in lines if x != ""]
lines = [x for x in lines if x != " "]
output = " ".join(lines)

lines = output.split("\n")
lines = [x for x in lines if x != ""]
lines = [x for x in lines if x != " "]
output = " ".join(lines)

print output