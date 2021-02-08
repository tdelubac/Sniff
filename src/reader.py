import threading
import pandas as pd
import time
import os

class Reader(threading.Thread):

	def __init__(self, file, bssid):
		threading.Thread.__init__(self)
		self.file = file
		self.bssid = bssid
		self.stop_signal = False

	def run(self):
		while not self.stop_signal:
			try:
				if os.path.isfile(self.file):
					with open(self.file) as f:
						lines = f.readlines()
						for line in lines:
							if self.bssid in line:
								print(line.split(',')[3])
								break

			except Exception as e:
				print(e)
			time.sleep(1)

	def stop(self):
		self.stop_signal = True
