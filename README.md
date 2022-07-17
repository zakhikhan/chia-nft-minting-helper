# Chia NFT Minting Helper 

**NOTE: This script is still an alpha prototype. If you have tested it, please let me know, as your feedback will be immensely helpful.**

A bash script to help make the process of minting a series of NFTs on the Chia Blockchain easier. This allows you to put the images and metadata in their own directories and mints the NFTs on the Chia blockchain. There is also a tool for metadata generation. 

I also want to create another script to create the offer files and upload them to [dexie](https://dexie.space), but that is TBD.

Happy minting!


## INSTALL INSTRUCTIONS

Install on Linux using:

```shell
git clone https://github.com/zakhikhan/chia-nft-minting-helper.git
```

## UPDATE INSTRUCTIONS

Update using
```shell
cd chia-nft-minting-helper
git pull
```
## DEPENDENCIES

* Linux is the only OS that is supported at the moment. Not tested on MacOS, though I do have a Mac so I will test it soon.
* Chia wallet 1.4 or greater
* curl and jq packages (install instructions below)

## USAGE INSTRUCTIONS

#### 1. METADATA GENERATION

Each NFT minted on the Chia Blockchain needs to have an associated metadata file in addition to an NFT file. This tool will bulk generate custom metadata in seconds.

1. Make sure you are updated to version 0.4.0 and have python installed on your machine.

2. Create a config file named `metadata_config.py`. This file allows you to customize the common attributes that all metadata files you generate will share. An example can be found in the `metadata_config_example.py`. If you use this as a template, make sure to change the name to `metadata_config.py`.

3. Create a subdirectory called /metadata:

```shell
mkdir metadata
```

4. Create a `metadata_generation_csv.csv` file. This file will allow you to customize the attributes that vary with each NFT metadata. An example can be found at metadata_generation_csv_example.csv. Please follow the format of the example exactly without adding or removing fields. You can have as many rows as you want, with each
row representing 1 NFT.

5. Navigate to the chia-nft-minting-helper directory and run the following command:
```shell
python3 generate_metadata.py
```
-OR-
```shell
python generate_metadata.py
```

Your metadata will now be present in the /metadata directory. You can proceed to minting your new NFTs.

##### Advanced: Metadata individual attributes:

If you would like to create individual attributes, open the metadata_config.py file in a text editor and change the indvdl_attributes variable at the bottom from `False` to `True`. Then follow step 3 above, except create a metadata_generation_csv_with_attributes.csv. An example can be found in metadata_generation_csv_with_attributes_example.csv.
You can have as many attributes as you'd like—just add or delete columns to the CSV file. 

#### 2. NFT MINTING
 1. Follow instructions at https://devs.chia.net/guides/nft-intro to create a DID wallet and NFT wallet in the CLI. Make sure the wallet is funded with enough XCH to mint an NFT. If you don't have enough, you can get some from the Chia faucet.

 2. Make sure Chia installed and running and synced Chia wallet.

 3. Create /images in chia-nft-mint-helper and add all image files to the /images directory, saved in the format of 'image[x].jpg' (or other extension), with x representing the number in minting order. Do the same for metadata files in the /metadata directory.
	example: files must be saved as image1.jpg, image2.jpg, image3.jpg, etc. 
		metadata must be saved as metadata1.json, metadata2.json, metadata3.json, with the numbers on the images and metadata matching up for the same NFT.
	Note: If you used the metadata generation script the metadata will already be in the proper location for you. Just make sure the numbers on the metadata filenames match up with the image filenames.

4. Sign up for an account at nft.storage and get an API Key

5. Customize all variables in the script 'mintingscript.sh' by opening it with a text editor. Make sure you are clear on what they are all for. Many questions can be answered in the Chia NFT documentation, linked above.

6. Install the dependencies: curl and jq. If using Ubuntu with apt, run the following commands:

```shell
sudo apt update
sudo apt upgrade
sudo apt install curl
sudo apt install jq
```
6. Run the script by navigating to the directory of the script and executing the command './mintingscript.sh'. (You may need to change permissions on `mintingscript.sh` to executable with `sudo chmod +x mintingscript.sh`)

9. Before minting each NFT, the script will prompt you to review the minting command. Please review this command against the Chia documentation for minting a single NFL. Once you continue, the NFT will be created , final & permanent.

10. Continue through the process to mint all NFTs. If you have to stop the script, or get an error, you can open the script in a text editor and change the 'i' variable to resume wherever you left off.

[IMPORTANT NOTE: Please wait at least 1 minute in between minting each NFT. In the near future, we will add a function to delay minting automatically, but in the meantime, if you mint too quickly, the mint will fail.]

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
python upload_cli.py --help
``` 
 Otherwise:
 ```bash
 python upload_cli.py filename.jpg # The -s and -api are optional
 python upload_cli.py -s "https://api.nft.storage" -api "API_KEY" filename.jpg
```

I am happy to help with any questions anyone has.

Features currently not supported: multiple image urls, multiple metadata urls (however these can always be added later to existing NFTs)

