import json
import requests


image_path = {"path": "tests/test001.jpg"}

r = requests.post("http://127.0.0.1:8000/image/", data=json.dumps(image_path))
# r = requests.get("http://127.0.0.1:8000")
print(r.status_code)
print(r.json())
