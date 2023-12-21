import requests
import json

# url link
url = "http://127.0.0.1:8000/account/signup/"

# example user
payload = json.dumps({
  "username": "matthew",
  "password": "aA12345678"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


