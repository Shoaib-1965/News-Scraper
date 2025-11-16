# **📰 Google News Scraper**

## **🔍 Automated News Article Extraction Tool**

**Google News Scraper** is a powerful Python-based web scraping tool that automatically extracts and analyzes news articles from Google News. Built with **Playwright** and **BeautifulSoup**, this scraper searches for articles about web scraping, extracts titles and URLs, analyzes content for specific keywords, and exports everything to a structured CSV file.

The tool uses browser automation to handle dynamic content, cookie consent dialogs, and JavaScript-rendered pages, making it robust and reliable for news data extraction.

---

## **🚀 Key Features**

### **⚡ Core Functionality**

✅ **Automated Google News Search** — Searches Google News with custom queries  
✅ **Article Title Extraction** — Captures article headlines accurately  
✅ **URL Collection** — Extracts and validates article links  
✅ **Full Article Scraping** — Visits each article page and extracts complete content  
✅ **Keyword Analysis** — Searches for specific keywords (e.g., "proxy", "proxies") in articles  
✅ **CSV Export** — Saves all data in organized CSV format  
✅ **Cookie Consent Handling** — Automatically accepts cookie dialogs  
✅ **Dynamic Content Support** — Handles JavaScript-rendered pages with Playwright  
✅ **Statistical Reporting** — Provides summary of keyword matches found  
✅ **Customizable Search** — Easy to modify search queries and keywords

---

## **📸 Application Screenshots**

<p align="center">
  <img src="https://github.com/user-attachments/assets/3f4f9bd8-bdfe-485b-b3d7-b49502e93f84" alt="Scraper Dashboard" width="700" style="border-radius: 12px;"/>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/8e84982a-70e4-478b-a487-41d80a533923" alt="Article Extraction" width="700" style="border-radius: 12px;"/>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/8b29413b-b65e-43af-8db1-e219bbc613bc" alt="Code Implementation" width="700" style="border-radius: 12px;"/>
</p>

---

## **🔧 Technical Implementation**

### **Technologies Used:**

- **Python 3.x** — Core programming language
- **Playwright** — Browser automation for dynamic content
- **BeautifulSoup4** — HTML parsing and data extraction
- **CSV Module** — Structured data export
- **Chromium Browser** — Headless/visible browser automation

### **Architecture:**
```
Browser Launch (Playwright)
    ↓
Google News Search
    ↓
HTML Parsing (BeautifulSoup)
    ↓
Article Link Extraction
    ↓
Visit Each Article Page
    ↓
Content Analysis & Keyword Detection
    ↓
CSV Data Export
```

---

## **💡 How It Works**

### **Step-by-Step Process:**

1. **🌐 Launch Browser** — Playwright opens Chromium browser (visible mode for debugging)
2. **🔎 Search Google News** — Navigates to Google News with predefined search query
3. **🍪 Handle Cookies** — Automatically accepts cookie consent if prompted
4. **📋 Extract Links** — Parses page HTML to find article titles and URLs
5. **📄 Visit Articles** — Opens each article link to access full content
6. **🔍 Keyword Search** — Scans article text for specified keywords (case-insensitive)
7. **💾 Save to CSV** — Writes title, URL, and keyword match status to CSV file
8. **📊 Generate Report** — Displays summary statistics of findings

---

## **📊 Output Format**

The scraper generates a CSV file with the following structure:

| Title | URL | Contains Proxy |
|-------|-----|----------------|
| Article headline | Full article URL | True/False |

**Example Output:**
```
Title: "Web Scraping Best Practices in 2024"
URL: https://example.com/article
Contains Proxy: True

5/10 articles contained proxy keywords.
```

---

## **⚙️ Configuration Options**

### **Customizable Parameters:**

- **Search Query** — Modify the Google News search term
- **Article Limit** — Change number of articles to scrape (default: 10)
- **Keywords** — Add or modify keywords to search for
- **CSV Path** — Specify output file location
- **Browser Mode** — Toggle between headless and visible browser
- **Timeout Settings** — Adjust page load wait times

---

## **🛠️ Installation & Setup**

### **Prerequisites:**
```bash
Python 3.7 or higher
pip (Python package manager)
```

### **Installation Steps:**

```bash
# Clone the repository
git clone https://github.com/yourusername/news-scraper.git

# Navigate to project directory
cd news-scraper

# Install required packages
pip install playwright beautifulsoup4

# Install Playwright browsers
playwright install chromium

# Run the scraper
python scraper.py
```

---

## **📝 Code Structure**

### **Main Components:**

**1. Browser Initialization**
```python
browser = p.chromium.launch(headless=False)
page = browser.new_page()
```

**2. Google News Navigation**
```python
url = "https://news.google.com/search?q=web+scraping"
page.goto(url)
```

**3. Cookie Consent Handling**
```python
accept_button = page.wait_for_selector('text="Accept all"')
page.click('text="Accept all"')
```

**4. Article Extraction**
```python
links = soup.find_all("a", class_="WwrzSb")
titles = soup.find_all("a", class_="JtKRv")
```

**5. Keyword Analysis**
```python
contains_proxy = "proxy" in article_text or "proxies" in article_text
```

**6. CSV Export**
```python
writer.writerow({
    "Title": article_title,
    "URL": page.url,
    "Contains Proxy": contains_proxy
})
```

---

## **🎯 Use Cases**

✔️ **Market Research** — Monitor news trends and competitor mentions  
✔️ **Content Aggregation** — Collect articles on specific topics  
✔️ **SEO Analysis** — Track keyword usage in news articles  
✔️ **Academic Research** — Gather news data for studies  
✔️ **Media Monitoring** — Track coverage of specific subjects  
✔️ **Competitive Intelligence** — Monitor industry news and developments

---

## **🔒 Features Breakdown**

### **🤖 Browser Automation**
- Handles dynamic JavaScript content
- Manages cookie consent dialogs
- Waits for content to load properly
- Supports both headless and visible modes

### **📊 Data Processing**
- Extracts structured data from HTML
- Validates and fixes relative URLs
- Case-insensitive keyword matching
- Clean CSV output formatting

### **⚡ Performance**
- Configurable timeout settings
- Efficient HTML parsing
- Batch processing of articles
- Error handling for robustness

---

## **🚀 Future Enhancements**

🔹 Support for multiple news sources  
🔹 Advanced keyword analysis (NLP)  
🔹 Sentiment analysis integration  
🔹 Database storage option  
🔹 Scheduled automatic runs  
🔹 Email notifications for new articles  
🔹 GUI interface for easy configuration  

---

## **🔗 Connect With Me**

**LinkedIn:**  
🔵 [Shoaib Altaf](https://www.linkedin.com/in/shoaib-altaf-2a1760313/)

**Instagram:**  
📷 [@shoaib_altaf1965](https://instagram.com/shoaib_altaf1965)

---

## **⭐ Support**

If you find this project useful, please **⭐ star the repository** — it helps support future development!

---

## **📄 License**

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

**🔍 Automating News Intelligence | 🐍 Built with Python**
