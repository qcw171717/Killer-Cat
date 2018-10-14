from listen_processes import *
from Cats import Cat
import time
from os import popen

def exit(stat):
	with open('./apps_stats.txt' , 'w') as f:
		f.write('\n'.join(stat))


def yangmao(apps, cat, stat):
	process_info = running_process_during_interval(1)
	t = time.time()
	# kill app first
	for p in process_info:
		for app in apps:
			if app == p.app_name:
				cmd = 'kill ' + p.pid
				output = popen(cmd).read()
			else:
				stat.append(str(t) + '\t' + p.app_name)



if __name__ == '__main__':
	apps_to_kill = []
	with open('./apps_to_kill.txt') as f:
		for l in f.readlines():
			apps_to_kill.append(l.strip() + '.app')

	stats = []

	try:
		name = input('What name do you want to give to your killer cat? ')
		cat = Cat(name)
		cat.sound()
		start_time = time.time()
		check_point = start_time
		while True:
			yangmao(apps_to_kill, cat, stats)
			if time.time() - check_point >= 10:
				check_point = time.time()
				cat.sound()
				cat.grow()


	except KeyboardInterrupt:
		exit(stats)


	# s = input('Do you want to stop growing your cat?')