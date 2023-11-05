import os
import secrets 

import requests

from .util.decorators import logged_in

class SenseUClient:
    def __init__(self, username=None, password=None):
        self.base_url = "http://v2.sense-u.com"
        self.username = username or os.environ.get('SENSE_U_USERNAME')
        self.password = password or os.environ.get('SENSE_U_PASSWORD')
        self.bearer_token = None
        self.device_uuid = secrets.token_hex(20).upper()
        self.device_token = None
        self.headers = {
            'os': 'android',
            'version': '3.5.4',
            'build': '818',
            'accept-language': 'en-US',
            'user-agent': 'BabyNew/3.5.4()/818/Dalvik/2.1.0 (Linux; U; Android 11; Google Pixel 7 Build/QQ1B.400205.002)',
            'Content-Type': 'application/json',
            'host': 'v2.sense-u.com',
            'device-uuid': self.device_uuid,
            'connection': 'Keep-Alive',
            'accept-encoding': 'gzip'
        }

    def login(self):
        url = f"{self.base_url}/login"
        payload = {
            "device_time_zone": "Europe/Rome",
            "device_name": "Google Pixel 7",
            "device_lang": "en",
            "user_code": self.password,
            "app_version": "3.5.4",
            "device_uuid": self.device_uuid,
            "package_name": "com.senseu.baby",
            "device_os": "Android 11",
            "username": self.username,
        }
        response = requests.post(url, json=payload, headers=self.headers)
        if response.ok:
            data = response.json()
            self.bearer_token = data['data']['token']
            self.headers['token'] = self.bearer_token
            print('Login successful')
        else:
            print('Login failed:', response.text)

    def _make_api_call(self, method, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=payload)
        return response

    @logged_in
    def list_devices(self):
        response = self._make_api_call("GET", "/device/lists")
        if response.ok:
            return response.json()['data']
        else:
            print('Failed to list devices:', response.text)

    @logged_in
    def get_user_info(self):
        response = self._make_api_call("GET", "/user/info")
        if response.ok:
            return response.json()['data']
        else:
            print('Failed to get user info:', response.text)

    @logged_in
    def get_base_stations(self):
        response = self._make_api_call("GET", "/base_station/lists")
        if response.ok:
            return response.json()['data']
        else:
            print('Failed to get base stations:', response.text)
    
    @logged_in
    def get_children(self):
        response = self._make_api_call("GET", "/child")
        if response.ok:
            return response.json()['data']
        else:
            print('Failed to get children:', response.text)
