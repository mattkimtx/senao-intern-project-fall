# USING API

To use the Create User API, you must send a JSON payload with an HTTP request ("POST"). Here is an example of a Create User script using Python.

```
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
```

To Login in using the API, you must send a JSON payload with an HTTP request ("GET"). Here is an example of a Login script using Python

```
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

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```