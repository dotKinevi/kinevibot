from functions import *
from apscheduler.schedulers.blocking import BlockingScheduler

kinevion = Bot()

kinevion.get_img()
kinevion.post()
kinevion.delete_used()


def post():
	kinevion.get_img()
	kinevion.post()
	kinevion.delete_used()

posting = BlockingScheduler(timezone="Etc/GMT-3")
posting.add_job(post, 'interval', hours = 1)
posting.start()
