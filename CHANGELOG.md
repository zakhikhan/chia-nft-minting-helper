
# Change Log
All notable changes to this project will be documented in this file.
 
## [0.4.1] - 2022-07-05
Removed the `-st` and `-sn` flags, as Chia Network pointed out that they do not represent series number and series total, but edition number and edition total. If you wish to include series number and series total, I recommend putting it in the NFT name or metadata.

## [0.4.0] HOTFIX - 2022-07-03
Changed metadata generation script to change sensitive content value from string to bool to be in line with Chia official schema. For the time being, the sensitive content value will always be set to false, regardless of what is entered in the CSV.

## [0.4.0] - 2022-07-03
Added a Python script for automatic metadata generation

## [0.3.0] - 2022-07-02
Added automatic image and metadata uploading. Thanks to @steppsr. Also removed the target address option from minting and changed the deault fee to 0, thanks to scrutinous for the tip. Also added Python script to do the same by @Rosko. More documentation coming