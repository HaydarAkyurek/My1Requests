import requests
url = 'http://10.0.0.4/dvwa/login.php'
headers = {'user-agent': 'btk-akademi/1.1.1'}

data = {'username':'admin','password':'password','Login':'Login'}

try:
	r = requests.post(url, data=data, allow_redirect=True)#https>https geçişini engellliyo. Ayrıca buraya timeout=2 eklenebilir cevap süresi için.
	print(r.status_code)
	print(r.text)
	#print(r.headers)
	#print(r.headers).get('Date')#istediğimiz değeri alabiliriz.r içerisinde headers=headers olucak.
except Exception as e:
	print(e)
	pass



#status_code
#text
#headers
