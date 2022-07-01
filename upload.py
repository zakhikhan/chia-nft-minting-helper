import requests
headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDc2YjQ1ZTEzMjJmNzFCYzFDYWVkYUY4'}, \
{'Content-Type': 'multipart/form-data'}
payload = {'file' : open('/home/zack/smile/photos/smile3.jpg','rb')}
r = requests.post("https://api.nft.storage", files=payload, headers=headers)
print(r.text)
