import requests
import os, sys
from pathlib import Path


cwd_path = Path.cwd()
# If API_KEY is in a file config.py
if os.path.exists(cwd_path / "config.py"):
    try:
        from config import *
    except ModuleNotFoundError:
        print("Please make sure a file called config.py contains variables")
else:
     sys.exit("Please create a file called config.py to insert your env variable")
    

def main_func():
    file_path = "path/to/file.jpg"
    storage_url = "https://api.nft.storage"
    NFT_API_KEY = os.environ["NFT_API_KEY"]

    headers = {
        "Authorization": f"Bearer {NFT_API_KEY}",
        "Content-Type": "multipart/form-data",
    }
    payload = {"file": open(file_path, "rb")}

    r = requests.post(storage_url, files=payload, headers=headers)
    print(r.text)
    print(r.status_code)


if __name__ == "__main__":
    main_func()
