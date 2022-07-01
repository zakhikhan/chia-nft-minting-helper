import requests
headers = {'Authorization': 'Bearer API_KEY_HERE'}, \
{'Content-Type': 'multipart/form-data'}
payload = {'file' : open('/home/zack/smile/photos/smile3.jpg','rb')}
r = requests.post("https://api.nft.storage", files=payload, headers=headers)
print(r.text)
