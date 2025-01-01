# RH Smith Faculty Directory Scraper

This project automates the process of extracting faculty contact information from the University of Maryland's Robert H. Smith School of Business faculty directory. It performs the following tasks:

1. **Fetch Faculty Pages**: Uses Firecrawl API to scrape URLs of faculty pages from the directory.
2. **Extract Contact Information**: Calls Firecrawl API for each faculty page to extract contact details such as email, phone number, office location, etc.
3. **Save Data**: Stores the extracted information in a CSV file for easy access.



## Prerequisites

- Python 3.7 or higher
- Internet connection
- API key for Firecrawl API

### Python Packages

Install required packages:

```bash
pip install requests python-dotenv
```

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a `.env` File

Create a `.env` file in the project root and add your API key:

```
FIRECRAWL_API_KEY=your-api-key-here
```

### 3. Run Scripts

#### Fetch Faculty Links

Run the `getUrls.py` script to retrieve faculty page URLs and save them to `faculty_links.txt`:

```bash
python getUrls.py
```

#### Extract Contact Information

Run the `getContactInfo.py` script to extract contact information from the faculty pages and save it to `professor_contacts.csv`:

```bash
python getContactInfo.py
```

## Output Files

1. **faculty_links.txt**: Contains the URLs of all faculty pages.
2. **professor_contacts.csv**: Contains extracted contact information in the following format:

   | URL                                       | Name         | Email           | Phone       | Office              |
   |-------------------------------------------|--------------|-----------------|-------------|---------------------|
   | https://www.rhsmith.umd.edu/directory/jie-zhang | Jie Zhang    | jiejie@umd.edu  | 301-405-7899 | 3311 Van Munching Hall |

3. **scrape_log.log**: A log file with progress updates and errors.

## Script Details

### `getUrls.py`

This script:
1. Sends a POST request to the Firecrawl `map` API.
2. Fetches all faculty page URLs from the specified directory.
3. Saves the URLs to `faculty_links.txt`.

### `getContactInfo.py`

This script:
1. Reads URLs from `faculty_links.txt`.
2. Sends a POST request to the Firecrawl `scrape` API for each URL.
3. Extracts and saves contact details in `professor_contacts.csv`.
