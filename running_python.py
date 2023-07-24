import psutil
import time
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('log_dir')
args = parser.parse_args()
log_dir = Path(args.log_dir)

last_num_pythons = 0

while True:
	procs = [p.name() for p in psutil.process_iter()]
	pys = [i for i in procs if i=='pythonw.exe']
	num_pythons = len(pys)
	if num_pythons == 0:
		print('no pythons running...')
		break
	else:
		if num_pythons != last_num_pythons:
			print(f'{num_pythons} instances of python is running...')
			with open(log_dir.joinpath('python_status.txt'),mode='a+',encoding='utf-8') as file:
				file.write(f'{num_pythons} instances of python is running ...')
				file.write('\n')
			os.system(f'git -C "{log_dir.absolute()}" add .')
			os.system(f'git -C "{log_dir.absolute()}" commit -m "status update"')
			os.system(f'git -C "{log_dir.absolute()}" push')
			last_num_pythons = num_pythons
		else:
			last_num_pythons = num_pythons
	time.sleep(2)