from bs4 import BeautifulSoup
import urllib.request
response = urllib.request.urlopen('http://c.biancheng.net/view/1317.html')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
print (text)