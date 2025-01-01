import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# API details
api_url = "https://api.firecrawl.dev/v1/map"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('FIRECRAWL_API_KEY')}"
}
payload = {
    "url": "https://www.rhsmith.umd.edu/directory",
    "includeSubdomains": True
}

output_file = "faculty_links.txt"

try:
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            links = data.get("links", [])
            
            with open(output_file, "w") as file:
                for link in links:
                    file.write(link + "\n")
            
            print(f"Links have been saved to {output_file}")
        else:
            print("API call was successful, but 'success' flag is False.")
    else:
        print(f"API call failed with status code {response.status_code}: {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
