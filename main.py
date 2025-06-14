from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import urljoin, urlparse
import time


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

CHROME_DRIVER_PATH = 'G:\\selenium-scrap\\chromedriver-win64\\chromedriver.exe'

driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)

url = input(" Enter the website URL (e.g., https://example.com): ").strip()

visited = set()
pages_data = []

def get_internal_links(base_url):
    anchors = driver.find_elements(By.TAG_NAME, "a")
    base_domain = urlparse(base_url).netloc
    links = set()

    for anchor in anchors:
        href = anchor.get_attribute("href")
        if href:
            full_url = urljoin(base_url, href)
            if (
                full_url.startswith("http")
                and urlparse(full_url).netloc == base_domain
                and "#" not in href
                and full_url not in visited
            ):
                links.add(full_url)
    return list(links)

def scrape_page(page_url):
    try:
        driver.get(page_url)
        time.sleep(2)
        try:
            content_element = driver.find_element(By.TAG_NAME, "main")
        except:
            content_element = driver.find_element(By.TAG_NAME, "body")
        text = content_element.text
        pages_data.append(f"\n\n===== PAGE: {page_url} =====\n{text}")
        visited.add(page_url)
    except Exception as e:
        print(f" Failed to scrape {page_url} -> {e}")

try:
    print(" Scraping main page")
    scrape_page(url)

    print(" Collecting internal links")
    internal_links = get_internal_links(url)

    print(f" Found {len(internal_links)} internal pages.")
    for link in internal_links:
        scrape_page(link)

    with open("scraped_content.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(pages_data))

    print("\n All content saved to 'scraped_content.txt'.")

finally:
    driver.quit()
