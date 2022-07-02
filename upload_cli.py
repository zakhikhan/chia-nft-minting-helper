import requests
import os, sys
from pathlib import Path
import click

cwd_path = Path.cwd()
# If API_KEY is in a file config.py
if os.path.exists(cwd_path / "config.py"):
    try:
        from config import *
    except ModuleNotFoundError:
        print("Please make sure a file called config.py contains variables")
else:
    sys.exit("Please create a file called config.py to insert your env variable")

# Run `python upload_cli.py -h` for help
# Ex: `python upload_cli.py filename.jpg` The -s and -api are optional
# Ex: `python upload_cli.py -s "https://api.nft.storage" -api "API_KEY" filename.jpg`

@click.command()
@click.argument(
    "file_path", type=click.Path(exists=True, resolve_path=True), required=1
)
@click.option(
    "--storage_url",
    "-s",
    default="https://api.nft.storage",
    help="URL to post image",
    show_default=True,
    required=True,
)
@click.option("--api_key", "-api", help="The path to file you want to upload")
def main_func(file_path, storage_url, api_key):
    if not api_key:
        api_key = os.environ["NFT_API_KEY"]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "multipart/form-data",
    }
    payload = {"file": open(file_path, "rb")}
    r = requests.post(storage_url, files=payload, headers=headers)
    print(r.text)
    print(r.status_code)


if __name__ == "__main__":
    main_func()
