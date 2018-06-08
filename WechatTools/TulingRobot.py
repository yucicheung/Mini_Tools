import itchat
import requests

# calling tulingRobot
def getTulingResponse(msg):
	'''
	Input:
		message sent from user
	Return:
		reply text from tuling robot
	'''
	# for all vars defined below, it works in this function scope only
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key'	:'bd4ad1f69a2841629c3244b58d545416',
		'info'	:msg['Text'],
		'userid':"yuci",
	}
	r = requests.post(apiUrl, data=data).json()
	return r['text']

@itchat.msg_register(itchat.content.TEXT)
def tulingReply(msg):
	'''
	Input:
		message sent from user
	Output:
		reply from tuling robot
	Function:
		calling getTulingResponse() to reply message
	'''
	defaultResponse="Robot is now absent."
	fullResponse = "Tuling Robot replying:"+getTulingResponse(msg)
	return fullResponse or defaultResponse

itchat.auto_login(hotReload=True)
itchat.run()#for auto replying
