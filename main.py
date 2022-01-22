from functions import *
from apscheduler.schedulers.blocking import BlockingScheduler

class Main:
	def __init__(self):
		self.catusbot = Bot()

	def post(self):
		self.catusbot.get_img()
		self.catusbot.post()
		self.catusbot.delete_used()

	def run(self):
		posting = BlockingScheduler(timezone="Etc/GMT-3")
		posting.add_job(self.post, 'interval', hours = 1)
		posting.start()

if __name__ == "__main__":
	main = Main()
	main.post()
	main.run()
