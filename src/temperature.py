import requests
import json
from digitalai.release.integration import BaseTask

class Temperature(BaseTask):

    def execute(self) -> None:

        latitude = self.input_properties['latitude']
        longitude = self.input_properties['longitude']

        url = "https://api.open-meteo.com/v1/forecast?latitude=" + latitude + "&longitude=" + longitude + "&current_weather=true"
        self.add_comment(f"Sending request to {url}")
        r = requests.get(url)
        if r.status_code == 200:
            obj= {}
            obj = json.loads(r.text)
            self.set_output_property('temperature', obj['current_weather']['temperature'])
            self.set_output_property('time',obj['current_weather']['time'] + '(' + obj['timezone'] + ')')