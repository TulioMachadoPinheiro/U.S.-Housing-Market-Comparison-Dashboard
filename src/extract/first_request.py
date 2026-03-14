import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status code:", response.status_code)
print("Success!" if response.status_code == 200 else "Something went wrong.")