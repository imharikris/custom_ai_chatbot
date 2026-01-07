import requests
from bs4 import BeautifulSoup
from typing import List
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection": "keep-alive"
}

def clean_text(soup: BeautifulSoup) -> str:
    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.decompose()
    text = soup.get_text(separator=" ")
    lines = [line.strip() for line in text.splitlines()]
    cleaned = " ".join(line for line in lines if line)
    return cleaned

def scrape_page(url: str) -> str:
    session = requests.Session()
    retry = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    response = session.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return clean_text(soup)

def scrape_website(urls: List[str], output_path:str):
    all_texts =[]

    for url in urls:
        print(f"Scraping {url}")
        try:
            page_text = scrape_page(url)
            section =(f"\n\n===== SOURCE URL =====\n"
                f"{url}\n"
                f"===== PAGE CONTENT =====\n"
                f"{page_text}\n"
            )
            all_texts.append(section)
        except requests.exceptions.RequestException as e:
            print(f"Failed to scrape {url}: {e}")
            continue
        time.sleep(2)  # Be polite and avoid overwhelming the server

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(all_texts))

if __name__ == "__main__":
    URLS = ["https://fastapi.tiangolo.com/",
        "https://fastapi.tiangolo.com/tutorial/first-steps/",
        "https://fastapi.tiangolo.com/tutorial/path-params/",
        "https://fastapi.tiangolo.com/tutorial/query-params/",
        "https://fastapi.tiangolo.com/tutorial/body/",
    ]
    scrape_website(urls=URLS, output_path = "data/raw/website.txt")