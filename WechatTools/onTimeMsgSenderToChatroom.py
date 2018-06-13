# -*- coding:utf-8 -*-

import itchat
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


class onTimeSender(object):
	'''
	Automatically send message to chatroom on time according to user's predefinition.
	params:
		`roomName`: The name of chatroom you want to send message to;
		`context`: The message you want to send to chatroom;
		`time`: Time to send out message, in form of a dict.
	Usage:
		Please refer to the __main__ function part.
	'''
	def __init__(self,roomName='',context='',time={}):
		self.roomName=roomName
		self.context=context
		self.time=time	
		itchat.auto_login(hotReload=True,loginCallback=self.loginCallback,exitCallback=self.exitCallback)
		self.schedulerForSender()

	def sendChatroomMsg(self,roomName,context):
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
			sendtime = datetime.now().strftime('%A %B %d,%Y')#Tue June 08,2018
			sendtime = datetime.now().strftime('%m-%d-%Y %H:%M:%S,%A')
			msg = context + "Sending in "+sendtime
			print "Ready to send message to group %s,message as follows : \n%s"%(roomName,msg)
			itchat.send_msg(msg=msg,toUserName=username)

	def loginCallback(self):
		print "Successfully logged in."
				
	def exitCallback(self):
		print "Successfully logged out."


	def sendMsgToChatRoom(self):
		self.sendChatroomMsg(self.roomName,self.context)

	def schedulerForSender(self):
		# scheduler setup
		scheduler = BlockingScheduler()
		scheduler.add_job(self.sendMsgToChatRoom,'cron',day_of_week=self.time['day_of_week'],hour=self.time['hour'],minute=self.time['minute'],second=self.time['second'])# sending takes 4 seconds behind
		scheduler.start()

if __name__=='__main__':
	
	roomName = 'DVS_Group'
	context = u'通知上传日志'
	time = {'day_of_week':'tue,thu,sat','hour':22,'minute':24,'second':56}
	'''for testing
	roomName = u'两张王'
	context=u'该消息由程序自动发送'
	time = {'day_of_week':'*','hour':12,'minute':34,'second':26}
	'''
	onTimeSender(roomName,context,time)
