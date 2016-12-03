import urllib.request
from requests import get
import time

def push():
	client_token = ''
	subdomain = ''
	ip = get('https://api.ipify.org').text

	urllib.request.urlopen('http://104.131.201.115:5000/updatehost?subdomain=' + subdomain + '&ip=' + ip +
'&client_token=' +
client_token)
time.sleep(1800)

while True:
	push()
