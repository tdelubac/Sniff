#!/usr/bin/python3
import os
import time
from sniffer import Sniffer
from reader import Reader
import subprocess
from talk_to_leds import flash, rainbow_cycle


def main():
	flash((255,255,255))
	flash((255,255,255))
	flash((255,255,255))

	bssid = os.getenv('BSSID2')

	snif = Sniffer()
	snif.start_monitor_mode()
	snif.launch_monitoring()

	reader = Reader(snif.get_process(), bssid)

	# Try to identify wifi channel
	channel = None
	reader.start()
	i = 0
	while not channel:
		i += 1
		if i % 255 == 0:
			channel = reader.get_channel()
			i %= 255
		rainbow_cycle(0.001, i)

	reader.stop()
	reader.join()
	snif.stop_monitoring()
	snif.launch_monitoring(channel)
	# Reinstantiating reader
	reader = Reader(snif.get_process(), bssid, channel)
	reader.start()
	time.sleep(60)
	reader.stop()
	reader.join()
	snif.stop_monitoring()
	snif.stop_monitor_mode()
	return



if __name__=="__main__":
	main()

