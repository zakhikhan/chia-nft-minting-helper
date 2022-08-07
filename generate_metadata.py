#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import os
import json
import csv
from pathlib import Path

cwd_path = Path.cwd()

if os.path.exists(cwd_path / "metadata_config.py"):
    try:
        from metadata_config import *
    except ModuleNotFoundError:
        print("Please make sure to create a file called metadata_config.py.")
else:
        sys.exit("Please create a file called metadata_config.py.")


def main_function():   
    jsondata = {}
    collection = {}
    collection['name'] = collection_name
    collection['id'] = collection_uuid

    collection['attributes'] = [{'type':'description','value':collection_description}]
    if collection_twitter_account:
        collection['attributes'].append({'type':'twitter','value':collection_twitter_account})
    if collection_website:
        collection['attributes'].append({'type':'website','value':collection_website})
    if collection_discord:
        collection['attributes'].append({'type':'discord','value':collection_discord})
    if collection_icon:
        collection['attributes'].append({'type':'icon','value':collection_icon})


    n_format = "CHIP-0007"

    if indvdl_attributes == True:
        mtdcsv = 'metadata_generation_csv_with_attributes.csv'
    else:
        mtdcsv = 'metadata_generation_csv.csv'

    with open(mtdcsv,'r') as csvfile:
        csvreader = list(csv.reader(csvfile))
        for i in range(len(csvreader)):
            attributes_list = []
            if i == 0:
                if indvdl_attributes == True:
                    attribute_names = csvreader[0][4:]
                    num_attributes=len(attribute_names)
                    print (f"Detected {num_attributes} attributes")
            else:
                name = csvreader[i][1]
                description = csvreader[i][2]
                sensitive_content = False
                if indvdl_attributes == True:
                    for j in range(num_attributes):
                        k = j + 4
                        attributes_list.append({"trait_type":attribute_names[j],"value":csvreader[i][k]})
                jsondata['format'] = n_format
                jsondata['name'] = name
                jsondata['description'] = description
                jsondata['sensitive_content'] = sensitive_content
                jsondata['collection'] = collection
                if indvdl_attributes == True:
                    jsondata['attributes'] = attributes_list

                with open(f"metadata/metadata{i}.json","w") as f:
                    f.write(json.dumps(jsondata, indent=4))
    print("Metadata generation complete! You can find it in the /metadata folder. Thanks for using this tool.")
    
if __name__ == "__main__":
    main_function()

