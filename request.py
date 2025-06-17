import requests

# Step 1: Get the token
response = requests.post("http://127.0.0.1:8000/api/token/", json={
    "username": "Rishi",
    "password": "Chilveri#rishi14"
})
tokens = response.json()
access = tokens['access']

# Step 2: Use the access token
headers = {
    "Authorization": f"Bearer {access}"
}
res = requests.get("http://127.0.0.1:8000/api/core/secret/", headers=headers)
print(res.json())
