import requests

#  (Quotable API for random quotes)
url = "https://api.quotable.io/random"


response = requests.get(url, verify=False)

# Check if the request was successful (status code 200)
if response.status_code == 200:
   
    data = response.json()

    # Extract information
    quote = data['content']
    author = data['author']

    # Print
    print(f"Quote: {quote}")
    print(f"Author: {author}")
else:
    print(f"Error fetching data. Status Code: {response.status_code}")
