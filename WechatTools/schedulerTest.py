from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime

scheduler = BlockingScheduler()

#@scheduler.cron_scheduler(second='*',day_of_week='2-6',hour='10-22')
def testSendingMsg():
	print datetime.now()
scheduler.add_job(sendchatroomMsg,'date',rundate=date_value,
					kwargs={"name":name,"context":context})
scheduler.start()

