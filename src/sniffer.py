import os
import signal
import subprocess

class Sniffer():

	def __init__(self, interface='wlan0'):
		self.interface = interface
		self.process = None

	def start_monitor_mode(self):
		try:
			os.system('airmon-ng check kill')
			os.system('airmon-ng start ' + self.interface)
		except Exception as e:
			print(e)
		return

	def stop_monitor_mode(self):
		try:
			os.system('airmon-ng stop ' + self.interface + 'mon')
			os.system('systemctl restart NetworkManager')
		except Exception as e:
			print(e)
		return

	def launch_monitoring(self, channel=None):
		try:
			if channel:
				cmd = ['airodump-ng', self.interface + 'mon', '-n', '1', '--channel', channel]
			else:
				cmd = ['airodump-ng', self.interface + 'mon', '-n', '1']
			print(cmd)
			self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
		except Exception as e:
			print(e)
		return

	def stop_monitoring(self):
		if self.process is not None:
			self.process.kill()
			print('Killed process')
		else:
			print('No process to kill')
		return

	def get_process(self):
		return self.process
