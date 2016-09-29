
import requests

r = requests.get('https://api.github.com/user', auth=('danieltoo', 'deadpool200388'))
r.status_code
r.headers['content-type']
r.encoding
r.text
print (r.json())

