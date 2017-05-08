import urllib.request
from requests import get
import time

def push():
	try:
		print ('Ok, preparing...')
		client_token = ''
		subdomain = ''
		ip = get('https://api.ipify.org').text
		print ('Updating:\n' + '- host: ' + '"' + subdomain+ '"\n'+ '- addr: ' + ip)

		urllib.request.urlopen('http://dynip.space/update?hostname=' + subdomain + '&myip=' + ip +
	'&token=' + client_token)
		print ('Successful\nSleep for 30 min')
		time.sleep(1800)
	except Exception as e:
		print ('Oh shi...')

while True:
	push()
