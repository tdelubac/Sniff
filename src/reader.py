import threading
import pandas as pd
import time

class Reader(threading.Thread):

	def __init__(self, file, bssid):
		threading.Thread.__init__(self)
		self.file = file
		self.bssid = bssid
		self.stop_signal = False

	def run(self):
		while not self.stop_signal:
			try:
				with open(self.file) as f:
					lines = list(reversed(list(f)))
					for line in lines:
						if self.bssid in line:
							print(line.split(',')[4])
							break
			except Exception as e:
				print(e)
			time.sleep(1)

	def stop(self):
		self.stop_signal = True
