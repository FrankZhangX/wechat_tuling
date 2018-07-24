# -*- coding=utf-8 -*-
import itchat
import requests

KEY = 'apikey'	#图灵机器人的apikey

def get_response(msg):		#接收图灵回复
	apiURL = 'http://www.tuling123.com/openapi/api'
	data = {
		'key' : KEY,	#apikey
		'info' : msg,		#发送的消息
		'userid' : 'Tuling123'	#发送给图灵机器人的用户名，内容随意
	}
	try:
		rsp = requests.post(apiURL, data=data).json()
		return rsp.get('text')
	except Exception as e:
		print(e)
		return
'''
@itchat.msg_register(itchat.content.TEXT)	#重复消息
def repeat_message(msg):
	print(msg['Text'])
	return msg['Text']
'''
@itchat.msg_register(itchat.content.TEXT)	#私聊
def auto_reply(msg):
	print(get_response(msg['Text']))
	default_reply = '我已经接收到你的消息：\n'+msg['Text']+'\n但我不知道说什么好了'
	reply = get_response(msg['Text'])
	return reply or default_reply

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)	#群聊
def auto_reply(msg):
	print(get_response(msg['Text']))
	return get_response(msg['Text'])

itchat.auto_login(hotReload=True)
itchat.run()
