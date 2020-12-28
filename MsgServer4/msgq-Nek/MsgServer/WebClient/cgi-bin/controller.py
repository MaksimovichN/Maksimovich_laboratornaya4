import requests
import json


def DoRequest(method, cmd="", data=""):
	try:
		url = 'http://localhost:8080/cgi-bin/WEBClient.py'
		header = {"Content-type": 'text/html'}
		res = method(url+cmd, headers=header, data=json.dumps(data))
		if res.status_code == 200:
			return json.loads(res.content)
	except Exception as ex:
		print(ex)


def GetMsg(id):
	q = '?isRest=1&isPost=0&ClientID=' + str(id)
	res = DoRequest(requests.get, q)
	return res

def SendMsg(clientId, message, id):
	q = '?' + 'id='+ str(id) + '&isPost=1&message='+ message + '&isRest=' + '1' + '&ClientID=' + str(clientId)
	res = DoRequest(requests.get, q)
	return None
