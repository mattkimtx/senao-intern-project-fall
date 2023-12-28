<<<<<<< HEAD
# USING API

To use the Create User API, you must send a JSON payload with an HTTP request ("POST"). Here is an example of a Create User script using Python.

```
import requests
import json

=======
# Using the Create and Verify Account API

### Below are two example of using the Create and Verify Account API with a python script

Here is an example of creating an account by sending a JSON payload with the HTTP request "POST"

```
import requests
import json

>>>>>>> refs/remotes/origin/SCB-181
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

<<<<<<< HEAD
To Login in using the API, you must send a JSON payload with an HTTP request ("GET"). Here is an example of a Login script using Python

=======
Here is an example of verifying an account by sending a JSON payload with the HTTP request "GET"
>>>>>>> refs/remotes/origin/SCB-181
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