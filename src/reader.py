import threading
import pandas as pd
import time
import os

class Reader(threading.Thread):

	def __init__(self, process, bssid):
		threading.Thread.__init__(self)
		self.process = process
		self.bssid = bssid
		self.stop_signal = False

	def run(self):
		while not self.stop_signal:
			try:
				for i in range(1000):
					line = self.process.stdout.readline()
					if not line:
						print('breaking')
						break
					if self.bssid in line:
						line = line.replace('(not associated)', '(not_associated)')
						params = line.split(' ')
						params = [el for el in params if el]
						params = [el for el in params if el.startswith('\x1b') == False]
						print(params[2])
						break
			except Exception as e:
				print(e)
			time.sleep(1)




	def stop(self):
		self.stop_signal = True
