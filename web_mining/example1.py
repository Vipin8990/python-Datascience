import requests

url = 'http://www.google.com'
response = requests.get(url)
if response.status_code == 200:
    print('Success!')
    print(response.text)      # collection of data
else:
    print('An error has occurred.')