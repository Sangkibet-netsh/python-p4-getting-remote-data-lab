import requests
import json



url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        # response = requests.get(URL)
        # return response.text
        response = requests.get(self.url)
        return response.content


    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
    
requester = GetRequester(url)
response_body = requester.get_response_body()
print(response_body)
