import requests
import csv
from dotenv import load_dotenv
import os

load_dotenv()

# API details
api_url = "https://api.firecrawl.dev/v1/scrape"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('FIRECRAWL_API_KEY')}"
}
output_csv = "professor_contacts.csv"
url_file = "faculty_links.txt" 

def load_urls(file_path):
    try:
        with open(file_path, "r") as file:
            urls = [line.strip() for line in file.readlines()]
            print(f"Loaded {len(urls)} URLs from {file_path}")
            return urls
    except Exception as e:
        print(f"Error loading URLs from {file_path}: {e}")
        return []

def fetch_contact_info(url):
    payload = {
        "url": url,
        "formats": ["extract"],
        "extract": {
            "prompt": "Extract the professor's email id from the page"
        }
    }
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                extract = data.get("data", {}).get("extract", {})
                contact = extract.get("professor", {}).get("contact", {})
                print(f"Successfully fetched data for URL: {url}")
                return {
                    "url": url,
                    "name": extract.get("professor", {}).get("name", ""),
                    "email": contact.get("email", ""),
                    "phone": contact.get("phone", ""),
                    "office": contact.get("office", ""),
                }
            else:
                print(f"API success flag is false for URL: {url}")
        else:
            print(f"Failed for URL {url}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error fetching data for URL {url}: {e}")
    return None

def save_to_csv(data, file_path):
    try:
        with open(file_path, "w", newline="") as csvfile:
            fieldnames = ["url", "name", "email", "phone", "office"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Successfully saved {len(data)} records to {file_path}")
    except Exception as e:
        print(f"Error saving data to CSV {file_path}: {e}")

def main():
    print("Script started.")
    urls = load_urls(url_file)
    if not urls:
        print("No URLs to process. Exiting.")
        return
    
    contact_info = []
    for i, url in enumerate(urls):
        print(f"Processing {i+1}/{len(urls)}: {url}")
        info = fetch_contact_info(url)
        if info:
            contact_info.append(info)
        else:
            print(f"No contact information found for URL: {url}")
    
    if contact_info:
        save_to_csv(contact_info, output_csv)
    else:
        print("No contact information extracted. CSV file will not be created.")
    
    print("Script finished.")

if __name__ == "__main__":
    main()
