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
		except Exception as e:
			print(e)
		return

	def launch_monitoring(self, output):
		try:
			cmd = 'airodump-ng ' + self.interface + 'mon -w ' + output
			print(cmd)
			self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
		except Exception as e:
			print(e)
		return

	def stop_monitoring(self):
		if self.process is not None:
			os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
			print('Killed process')
		else:
			print('No process to kill')
		return


