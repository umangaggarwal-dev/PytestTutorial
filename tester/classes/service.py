import json


class Service:
    def process_data(self, string):
        return json.loads(string)