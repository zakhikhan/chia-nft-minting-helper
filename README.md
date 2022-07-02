# chia-nft-minting-helper

Version 0.3: Added automatic image and metadata uploading. Thanks to @steppsr. Also removed the target address option from minting and changed the deault fee to 0, thanks to scrutinous for the tip. 

NOTE: THIS SCRIPT IS IN ALPHA, PLEASE USE AT YOUR OWN RISK! ONLY COMPATIBLE WITH LINUX, DO NOT USE ON MACOS! I SUGGEST YOU TRY ON TESTNET FIRST

a bash script to help make the process of minting a series of NFTs on the Chia Blockchain easier.

This script is in ALPHA, so please use at your own risk. I welcome anyone working on this to improve it. This is the first bash script I've ever written. 

I also want to create another script to create the offer files and upload them to Dexie, but that is TBD.

Happy minting!


### INSTRUCTIONS

 1. Follow instructions at https://devs.chia.net/guides/nft-intro to create a DID wallet and NFT wallet in the CLI. Make sure the wallet is funded with enough XCH to mint an NFT. If you don't have enough, you can get some from
	the Chia faucet.

 2. Download this git repository to your machine with Chia installed and running and synced Chia wallet.

 3. Add all image files to the /images directory, saved in the format of 'image[x].jpg' (or other extension), with x representing the number in minting order. Do the same for metadata files in the /metadata directory.
	example: files must be saved as image1.jpg, image2.jpg, image3.jpg, etc. 
		metadata must be saved as metadata1.json, metadata2.json, metadata3.json, with the numbers on the images and metadata matching up for the same NFT.
	NOTE: I will soon release a tool for metadata file generation to make the process easier.

4. Sign up for an account at nft.storage and get an API Key

5. Customize all variables in the script 'mintingscript.sh' by opening it with a text editor. Make sure you are clear on what they are all for. Many questions can be answered in the Chia NFT documentation, linked above.

6. Install the dependencies: curl and jq. example: if using Ubuntu with apt, run the following commands:
		sudo apt update
		sudo apt upgrade
		sudo apt install curl
		sudo apt install jq

6. Run the script by navigating to the directory of the script and executing the command './mintingscript.sh'

9. Before minting each NFT, the script will prompt you to review the minting command. Please review this command against the Chia documentation for minting a single NFL. Once you continue, the NFT will be created , final & permanent.

10. Continue through the process to mint all NFTs. If you have to stop the script, or get an error, you can open the script in a text editor and change the 'i' variable to resume wherever you left off.

### PYTHON UPLOAD INSTRUCTIONS
#### For both `upload.py` and `upload_cli.py`:
1. Set up your python environment, install required modules (only `click` as of right now):

	```bash
	pip install -r requirements.txt
	```
2. Change name of the `config_example.py` to `config.py` and supply your apikey. `config.py` is in the `.gitignore`
3. Run the script
- If running `upload.py` modify the file name/file path then run 
	```bash 
	python upload.py
	```
- If using `upload_cli.py` for help you can run:
```bash
python upload_cli.py -h
``` 
 Otherwise:
 ```bash
 python upload_cli.py filename.jpg # The -s and -api are optional
 python upload_cli.py -s "https://api.nft.storage" -api "API_KEY" filename.jpg
```

I am happy to help with any questions anyone has.

Features currently not supported: multiple image urls, multiple metadata urls (however these can always be added later to existing NFTs)

NOTE: THIS SCRIPT IS IN ALPHA, PLEASE USE AT YOUR OWN RISK! ONLY COMPATIBLE WITH LINUX, DO NOT USE ON MACOS! I SUGGEST YOU TRY ON TESTNET FIRST
