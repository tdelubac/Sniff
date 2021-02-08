#!/usr/bin/python3
import os
import time
from sniffer import Sniffer
from reader import Reader

def main():
	output = '/home/kali/dev/sniffer/data/airodump-output'
	file = output + '-01.csv'
	bssid = os.getenv('BSSID2')
	snif = Sniffer()
	reader = Reader(file, bssid)

	#snif.start_monitor_mode()
	#snif.launch_monitoring(output)
	reader.start()
	time.sleep(200)
	reader.stop()
	#snif.stop_monitoring()
	#snif.stop_monitor_mode()
	return



if __name__=="__main__":
	main()

