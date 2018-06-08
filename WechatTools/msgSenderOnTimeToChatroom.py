# -*- coding:utf-8 -*-

import itchat
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def sendChatroomMsg(roomName,context):
	itchat.get_chatrooms(update=True)
	roomNickName = roomName
	candidates = itchat.search_chatrooms(roomNickName)
	print candidates
	username = ''
	for candidate in candidates:
		if candidate['NickName'] == roomNickName:
			username = candidate['UserName']
			break
	if username:
		#sendtime = datetime.now().strftime('%A %B %d,%Y')#Tue June 08,2018
		sendtime = datetime.now().strftime('%m-%d-%Y %H:%M:%S,%A')
		msg = context + "Sending in "+sendtime
		print "Ready to send message to group %s,message as follows : \n%s"%(roomName,msg)
		#itchat.send_msg(msg=msg,toUserName=username)

def loginCallback():
	print "Successfully logged in."

def exitCallback():
	print "Successfully logged out."

itchat.auto_login(hotReload=True,loginCallback=loginCallback,exitCallback=exitCallback)

# for formal information
#roomName = 'DVS'+u'吴老师组'
#context = u'通知上传日志'
# for testing
roomName = u'两张王'
context = u'此条为程序测试自动发送信息'
sendChatroomMsg(roomName,context)

'''
scheduler = BackgroundScheduler()
@scheduler.cron_schedule(second='*',day_of_week=['2','4','6'],hour='22')
def schedularControl():
	scheduler.add_job(sendChatroomMsg,'date',id='sendMsg',
					kwargs={roomName=roomName,context=context})
	scheduler.remove_job('sendMsg')
scheduler.start()
'''
#itchat.logout()#comment to make reload work

