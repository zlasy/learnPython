import requests
import json
import time
import re

#url = 'http://api.dangdang.com/shopim/user/getCustInfo?tenantId=1&custId=30236317'
#r = requests.get(url)
#result = json.loads(r.text)
# print(result)


#posturl = 'http://10.7.41.191:9009/msgcenter/qualityCheck/querySessionForQc'
headers = {'Content-Type': 'application/json;charset=UTF-8'}
#a = {"tenantId":1,"startTime":1562342400000,"endTime":1565020799000,"pageNum":1,"pageSize":10,"shopId":"0"}
#res = requests.post(posturl,json=a,headers=headers)
# print(res.text)

stopWords = ["亲，在吗","转人工","人工","人工客服"]

def getSession(roomId, sessionId):
    try:
        posturl = 'http://10.7.41.191:9009/msgcenter/session/querySessionDetail'
        b = {"tenantId": 1, "pageNum": 1, "pageSize": 1, "roomId": roomId, "sessionId": sessionId}
        res = requests.post(posturl, json=b, headers=headers)
        #print(res.text)
        j = json.loads(res.text)
        if (j['data']['session']['isTransManual'] == 1 and j['data']['session']['shopId'] == "0"):
            return j['data']['session']['transManualStartDate']
        return None
    except Exception as error:
        print("error:" + roomId, error)


def getMessage(roomId, sessionId, transDate):
    msgurl = 'http://10.7.41.191:9009/msgcenter/message/queryBySession'
    p = {"tenantId": 1, "pageNum": 1, "pageSize": 100, "roomId": roomId, "sessionId": sessionId}
    msgres = requests.post(msgurl, json=p, headers=headers)
    msgList = json.loads(msgres.text)['data']['list']
    cList = []
    for item in msgList:
        date_time = time.strptime(item['sendTime'], "%Y-%m-%d %H:%M:%S")
        if (transDate == None or time.mktime(date_time) < transDate/1000) and item['senderType'] == 1 and item['contentType'] == 1:
            cList.append(item['content'])
    if len(cList) == 0:
        return None
    l = cList[:3]
    l.reverse()
    return ",".join(i for i in l)

def invokeAi(roomId,custId,sessionId,content):
    aiurl = 'http://10.255.242.225:9000/classify/get'
    p = {"tenantId": 1, "roomId": roomId, "custId": custId, "sessionId": sessionId, "companyId": 1,"content": content}
    aires = requests.post(aiurl, json=p, headers=headers)
    print(aires.text)

def main():
    txt=open("H:\\分类语料.txt", 'r', encoding='utf8')
    file = open("H:\\fen.txt", 'w', encoding='utf8')
    for line in txt:
        line = re.sub(r'[^A-Za-z0-9\t]+',' ',line)
        s = line.split('\t')
        roomId = s[0]
        sessionId = s[1]
        custId = s[2]
        tDate = getSession(roomId, sessionId)
        if tDate == None:
            continue
        content = getMessage(roomId, sessionId, tDate)
        if (content and len(content) > 3 and content not in stopWords):
            #invokeAi(roomId,custId,sessionId,content)
            file.write(roomId + "\t" + custId + "\t" + sessionId + "\t" + content + "\n")
            print(content)
        # time.sleep( 0.5 )
    file.close()
    txt.close()

if __name__ == '__main__':
    main()