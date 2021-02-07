import threading

class Reader(threading.Thread):

	def __init__(self, file, bssid):
		threading.Thread.__init__(self)
		self.file = file
		self.bssid = bssid
		self.stop_signal = False

	def run(self):
		while not self.stop_signal:
			print('Reading ' + self.file)

	def stop(self):
		self.stop_signal = True
