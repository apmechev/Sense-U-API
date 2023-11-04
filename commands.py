import requests
import json
import os

USERNAME = os.environ.get('SENSE_U_USERNAME')
PASSWORD = os.environ.get('SENSE_U_PASSWORD')

url = "http://v2.sense-u.com/login"

payload = json.dumps({
  "device_time_zone": "Europe/Rome",
  "device_name": "Google Pixel 7",
  "device_lang": "en",
  "user_code": PASSWORD,
  "app_version": "3.5.4",
  "package_name": "com.senseu.baby",
  "device_os": "Android 11",
#  "device_uuid": "",
  "username": USERNAME,
})
headers = {
  'count': '2',
  'os': 'android',
  'version': '3.5.4',
  'build': '818',
#  'device-uuid': '',
  'accept-language': 'en-US',
  'user-agent': 'BabyNew/3.5.4()/818/Dalvik/2.1.0 (Linux; U; Android 11; Google Pixel 7 Build/QQ1B.400205.002)',
  'Content-Type': 'application/json',
  'content-length': '383',
  'host': 'v2.sense-u.com',
  'connection': 'Keep-Alive',
  'accept-encoding': 'gzip'
}

response = requests.request("POST", url, headers=headers, data=payload)
if response.ok:
    print('Login successful')
    data = response.json()
    bearer_token = data['data']['token']    
    access_token = data['data']['access_token']
