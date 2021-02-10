import threading
import pandas as pd
import time
import os
from talk_to_leds import set_color, stop_leds

class Reader(threading.Thread):

	def __init__(self, process, bssid):
		threading.Thread.__init__(self)
		self.process = process
		self.bssid = bssid
		self.stop_signal = False
		self.wifi_mac = None
		self.wifi_channel = None

	def run(self):
		while not self.stop_signal:
			try:
				toc = 0
				tic = time.time()
				while toc - tic < 10:
					toc = time.time()
					print(self.process.stdout.read())
					line = self.process.stdout.readline()
					if not line:
						break
					if self.wifi_mac:
						if (self.wifi_mac in line) and (self.bssid not in line):
							params = line.split(' ')
							params = [el for el in params if el]
							params = [el for el in params if el.startswith('\x1b') == False]
							self.wifi_channel = params[5]
							print('channel', self.wifi_channel)
					if self.bssid in line:
						line = line.replace('(not associated)', '(not_associated)')
						params = line.split(' ')
						params = [el for el in params if el]
						params = [el for el in params if el.startswith('\x1b') == False]
						self.wifi_mac = params[0]
						set_color(int(params[2]))
						print('power',params[2])
						break
			except Exception as e:
				print(e)
			#time.sleep(1)



	def stop(self):
		set_color((0,0,0))
		self.stop_signal = True

	def get_channel(self):
		return self.wifi_channel
