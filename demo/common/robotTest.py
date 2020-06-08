import requests
import json
import time
import re

# url = 'http://api.dangdang.com/shopim/user/getCustInfo?tenantId=1&custId=30236317'
# r = requests.get(url)
# result = json.loads(r.text)
# print(result)


# posturl = 'http://10.7.41.191:9009/msgcenter/qualityCheck/querySessionForQc'
headers = {'Content-Type': 'application/json;charset=UTF-8'}
# a = {"tenantId":1,"startTime":1562342400000,"endTime":1565020799000,"pageNum":1,"pageSize":10,"shopId":"0"}
# res = requests.post(posturl,json=a,headers=headers)
# print(res.text)


def getSession(roomId, sessionId):
    try:
        posturl = 'http://10.7.41.191:9009/msgcenter/session/querySessionDetail'
        b = {"tenantId": 1, "pageNum": 1, "pageSize": 1, "roomId": roomId, "sessionId": sessionId}
        res = requests.post(posturl, json=b, headers=headers)
        # print(res.text)
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
        if (transDate is None or time.mktime(date_time) < transDate / 1000) and item['senderType'] == 1 and item[
            'contentType'] == 1:
            cList.append(item['content'])
    if len(cList) == 0:
        return None
    l = cList[:3]
    l.reverse()
    return ",".join(i for i in l)


def invokeAi(question):
    aiurl = 'http://10.255.242.225:9000/question/matchVerbose'
    #aiurl = 'http://localhost:9000/question/matchVerbose'
    p = {"companyId": 1, "question": question}
    aires = requests.post(aiurl, json=p, headers=headers)
    printTop3(aires.text)


def printTop3(result):
    data = json.loads(result)['data']
    print(data)
    print('lucene')
    for i in range(3):
        item = data['luceneHits'][i]
        print('qid=' + str(item['qid']) + ',similarid=' + str(item['similarId']) + ',question=' + item['question'] + ',score=' + str(item['score']))
    print('word2vec')
    for i in range(3):
        item = data['w2vHits'][i]
        print('qid=' + str(item['qid']) + ',similarid=' + str(item['similarId']) + ',question=' + item[
            'question'] + ',score=' + str(item['score']))


def main():
    txt = open("H:\\qaList.txt", 'r', encoding='utf8')
    content = '这个换货为啥变成自行邮寄的'
    invokeAi(content)
    #for line in txt:
     #   if content and len(content) > 3:
     #       invokeAi(roomId, custId, sessionId, content)
     #       print(content)
        # time.sleep( 0.5 )
    txt.close()


if __name__ == '__main__':
    main()
