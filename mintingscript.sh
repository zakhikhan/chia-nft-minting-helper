#! /bin/bash

total_num_to_mint=30

localdir="/home/USER/chia-nft-minting-helper/"
i=1
while (( $i <= $total_num_to_mint ))
do
	f= "${localdir}photos/smile${i}.jpg"
	# Make metadata files
	sed "s/Smile! #1/Smile! #${i}/" ${localdir}metadata/origin_metadata.json > ${localdir}metadata/metadata${i}.json
	# 2. Upload image and return CID as variable
	read -p "Image $i CID: " image_cid
	image_url="https://${image_cid}.ipfs.nftstorage.link"
	# 3. Check if hash of image locally and online match, then save hash as variable
	local_image_hash=$(sha256sum ${localdir}photos/smile${i}.jpg | head -c 64)
	remote_image_hash=$(curl -s $image_url | sha256sum | head -c 64)
	if [ $remote_image_hash == $local_image_hash ]
	then
		echo "we have a match"
		echo $image_url
	else
		echo "hashes don't match"
		echo "url: $image_url hash of local file: $local_image_hash hash of remote file: $remote_image_hash"
		exit
	fi
	# 4. Upload metadata and return CID as variable
	read -p "Metadata $i CID: " metadata_cid
	metadata_url="https://${metadata_cid}.ipfs.nftstorage.link"
	# 3. Check if hash of metadata locally and online match, then save hash as variable
	local_metadata_hash=$(sha256sum ${localdir}metadata/metadata${i}.json | head -c 64)
	remote_metadata_hash=$(curl -s $metadata_url | sha256sum | head -c 64)
	if [ $remote_metadata_hash == $local_metadata_hash ]
	then
		echo "we have a match"
		echo $metadata_url
	else
		echo "hashes don't match"
		echo "url: $metadata_url hash of local file: $local_metadata_hash hash of remote file: $remote_metadata_hash"
		exit
	fi

	# 6. Create command & Validate with user
	read -p "Please validate the minting details before execution: chia wallet nft mint -f 1731819744 -i 8 -ra xch103m57yshjuualzslespw4jgg4lgc5jufzmdtn77xkdt2erhtk9hqzp0ynr -ta xch103m57yshjuualzslespw4jgg4lgc5jufzmdtn77xkdt2erhtk9hqzp0ynr -u $image_url -nh $local_image_hash -mu $metadata_url -mh $local_metadata_hash -sn $i -st 30 -rp 800 -m 0.00005 Proceed with minting? (y/n)" response
       if [ $response == "y" ]
       then
		echo "proceeding to mint.... jk"
 	else
		echo "mint cancelled"
		exit
	fi		

       	

	# 7. Execute command
	cd ~/chia-blockchain
	. ./activate
	chia wallet nft mint -f 1731819744 -i 8 -ra xch103m57yshjuualzslespw4jgg4lgc5jufzmdtn77xkdt2erhtk9hqzp0ynr -ta xch103m57yshjuualzslespw4jgg4lgc5jufzmdtn77xkdt2erhtk9hqzp0ynr -u $image_url -nh $local_image_hash -mu $metadata_url -mh $local_metadata_hash -sn $i -st 30 -rp 800 -m 0.00005
	deactivate
	i=$((i+1))
done

# chia wallet nft mint -f 1731819744 -i 8 -ra xch103m57yshjuualzslespw4jgg4lgc5jufzmdtn77xkdt2erhtk9hqzp0ynr -ta xch103m57yshjuualzslespw4jgg4lgc5jufzmdtn77xkdt2erhtk9hqzp0ynr -u $image_url -nh $local_image_hash -mu $metadata_url -mh $local_metadata_hash -sn $i -st 30 -rp 800 -m 0.00005


