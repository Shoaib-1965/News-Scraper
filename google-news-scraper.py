import csv
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_google_news():

    with sync_playwright() as p:
        # Launch browser normally (no proxy)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Google News search URL
        url = "https://news.google.com/search?q=web+scraping&hl=en-US&gl=US&ceid=US%3Aen"
        page.goto(url)

        # Try to accept cookies (if appears)
        try:
            accept_button = page.wait_for_selector('text="Accept all"', timeout=5000)
            if accept_button:
                page.click('text="Accept all"')
        except:
            print("No 'Accept all' button found, continuing...")

        page.wait_for_timeout(5000)

        # Parse the page
        soup = BeautifulSoup(page.content(), "html.parser")

        # Extract article titles + URLs
        links = soup.find_all("a", class_="WwrzSb")
        titles = soup.find_all("a", class_="JtKRv")

        proxy_count = 0
        total_count = 0

        # CSV save location
        csv_path = r"C:\Users\Shoaib Altaf\Downloads\Google-News-scraper-main\scraped_articles.csv"

        # Create CSV and write data
        with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Title", "URL", "Contains Proxy"])
            writer.writeheader()

            # Loop through first 10 results
            for title, link in zip(titles[:10], links[:10]):
                article_title = title.text
                article_url = link["href"]

                # Fix relative URLs
                if article_url.startswith("./"):
                    article_url = "https://news.google.com" + article_url

                # Open article page
                page.goto(article_url)
                page.wait_for_timeout(5000)

                # Extract content
                article_soup = BeautifulSoup(page.content(), "html.parser")
                article_text = article_soup.get_text().lower()

                contains_proxy = "proxy" in article_text or "proxies" in article_text

                # Save to CSV
                writer.writerow({
                    "Title": article_title,
                    "URL": page.url,
                    "Contains Proxy": contains_proxy
                })

                # Print output
                print(f"Title: {article_title}")
                print(f"URL: {page.url}")
                print(f"Contains proxy word: {contains_proxy}\n")

                total_count += 1
                if contains_proxy:
                    proxy_count += 1

        print(f"\n{proxy_count}/{total_count} articles contained proxy keywords.")
        browser.close()

if __name__ == "__main__":
    scrape_google_news()
