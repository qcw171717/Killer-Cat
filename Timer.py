import time

class CatTimer:
	""" A timer """

	# the current time that updates itself
	start_time: float
	timer_stopped: bool

	def __init__(self):
		self.start_time = -1 # just to check if the timer is ever started
		self.timer_stopped = False


	def start_timer(self):
		print("Timer started!")
		self.start_time = time.time()


	def stop_timer(self) -> float:
		print('Timer stopped')
		self.timer_stopped = True
		return time.time() - self.start_time


if __name__ == '__main__':
	cat_timer = CatTimer()
	cat_timer.start_timer()
	time.sleep(3)
	print(cat_timer.stop_timer(), 's')

