from banner.banner import *
from arguments.checker import Checker
from attacks.linux import LinuxLFI
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-t','--target',  help="Target", required=True)
parse.add_argument('-wc', '--walkcount', help="Number of directories to walk up", required=True)
parse.add_argument('-os', '--operatingsystem', help="Specify the operating system to check", required=True)
parse = parse.parse_args()

if parse.target and parse.walkcount:
	banner()
	print("\nURL target ->> {}\n".format(parse.target))
	file_paths = Checker.get_payload_file(parse)
	if parse.operatingsystem == 'linux':
		LinuxLFI.execute_linux_attack(file_paths, parse)
else:
	print(f"{RED_NORMAL}[ERR0R]{END} Argument invalid\nRequest help : python3 LFIscanner.py --help\nExit the script...")
	time.sleep(2)
	exit(0)	
