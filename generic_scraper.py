from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website_title(url):
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        title = soup.title.string if soup.title else "No title found"
        driver.quit()

        print(f"[+] Title: {title}")
    except Exception as e:
        print(f"[!] Error scraping generic site: {e}")

