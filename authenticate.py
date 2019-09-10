import requests

payload = {'client_id': '77bf03d75ce441e38287e089b1cb4e4c', 'response_type': 'code', 'redirect_uri': 'http://thinkdavid.xyz/#/store', 'scope': 'user-read-private%20user-read-email&state=34fFs29kd09'}
resp = requests.get("https://accounts.spotify.com/authorize", params=payload)
if resp.status_code != 200:
	print("error")
else:
	try:
		resp.json()
		print(resp.json())
	except:
		responses = resp.text
		print(responses)
