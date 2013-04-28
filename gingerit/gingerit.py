import requests


class GingerIt:
    def __init__(self):
        self.url = 'http://services.gingersoftware.com/Ginger/correct/json/GingerTheText'
        self.api_key = '6ae0c3a0-afdc-4532-a810-82ded0054236'
        self.api_version = '2.0'
        self.lang = 'US'

    def parse(self, text):
        s = requests.Session()
        req = s.get(
            self.url,
            params={
                'lang': self.lang,
                'apiKey': self.api_key,
                'clientVersion': self.api_version,
                'text': text
            },
        )
        return req
