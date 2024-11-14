import requests

url = "http://10.100.52:11632/?page=recover"
data = {
    "mail": "admin@borntosec.com",  # Modify this value
    "Submit": "Submit"
}

response = requests.post(url, data=data)

print(response.text)  # Analyze the response to see if the flag is revealed
