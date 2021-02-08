#!/usr/bin/python3
import os
import time
from sniffer import Sniffer
from reader import Reader
import subprocess

def main():
	bssid = os.getenv('BSSID2')

	snif = Sniffer()
	snif.start_monitor_mode()
	snif.launch_monitoring()

	reader = Reader(snif.get_process(), bssid)
	reader.start()
	time.sleep(60)
	reader.stop()
	reader.join()
	snif.stop_monitoring()
	snif.stop_monitor_mode()
	return



if __name__=="__main__":
	main()

