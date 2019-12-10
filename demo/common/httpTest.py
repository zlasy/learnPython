#import nltk
import requests
import json

url = 'http://api.dangdang.com/shopim/user/getCustInfo?tenantId=1&custId=30236317'

r = requests.get(url)
result = json.loads(r.text)
print(result)