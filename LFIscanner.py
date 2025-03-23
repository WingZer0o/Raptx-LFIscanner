from banner.banner import *
from attacks.linux import LinuxLFI
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-t","--target",  help="Target of the host example: http://94.237.61.133:39139/index.php?language=", required=True)
parse.add_argument("-wc", "--walkcount", help="Number of directories to walk up", required=True)
parse.add_argument("-w", "--wordlist", help="Specify path to your wordlist you want", required=True)
parse = parse.parse_args()

if parse.target and parse.walkcount and parse.wordlist:
	banner()
	print("\nURL target ->> {}\n".format(parse.target))
	file_paths = open(parse.wordlist, "r")
	LinuxLFI.execute_attack(file_paths, parse)
else:
	print(f"{RED_NORMAL}[ERR0R]{END} Argument invalid\nRequest help : python3 LFIscanner.py --help\nExit the script...")
	time.sleep(2)
	exit(0)	
