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
		self.power = None


	def run(self):
		while not self.stop_signal:
			try:
				tic = time.time()
				for line in iter(self.process.stdout.readline, ""):
					toc = time.time()
					if toc - tic > 5:
						break
					if self.wifi_mac:
						if (self.wifi_mac in line) and (self.bssid not in line):
							params = line.split(' ')
							params = [el for el in params if el]
							params = [el for el in params if el.startswith('\x1b') == False]
							if params[5]!=self.wifi_channel:
								self.wifi_channel = params[5]
								print('channel', self.wifi_channel)
					if self.bssid in line:
						line = line.replace('(not associated)', '(not_associated)')
						params = line.split(' ')
						params = [el for el in params if el]
						params = [el for el in params if el.startswith('\x1b') == False]
						self.wifi_mac = params[0]
						if params[2] != self.power:
							self.power = params[2]
							set_color(int(self.power))
							print('power ',params[2])
						break
			except Exception as e:
				print(e)
			#time.sleep(1)



	def stop(self):
		stop_leds()
		self.stop_signal = True

	def get_channel(self):
		return self.wifi_channel
