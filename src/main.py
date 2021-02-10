#!/usr/bin/python3
import os
import time
from sniffer import Sniffer
from reader import Reader
import subprocess
from talk_to_leds import flash


def main():
	flash((255,255,255))
	flash((255,255,255))
	flash((255,255,255))

	bssid = os.getenv('BSSID1')

	snif = Sniffer()
	snif.start_monitor_mode()
	snif.launch_monitoring()

	reader = Reader(snif.get_process(), bssid)

	# Try to identify wifi channel
	channel = None
	reader.start()
	for i in range(6):
		time.sleep(5)
		channel = reader.get_channel()
		if channel:
			break

	if channel:
		flash((0,255,0))
		flash((0,255,0))
		flash((0,255,0))
		flash((0,255,0))
		flash((0,255,0))
		reader.stop()
		reader.join()
		snif.stop_monitoring()
		snif.launch_monitoring(channel)
		# Reinstantiating reader
		reader = Reader(snif.get_process(), bssid)
		reader.start()
	else:
		flash((255,0,0))
		flash((255,0,0))
		flash((255,0,0))
		flash((255,0,0))
		flash((255,0,0))
		flash((255,0,0))

	time.sleep(300)
	reader.stop()
	reader.join()
	snif.stop_monitoring()
	snif.stop_monitor_mode()
	return



if __name__=="__main__":
	main()

