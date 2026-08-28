---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/building-crawler.html
---

# Building the web crawler
<a name="building-crawler"></a>

As described in the [Architecture](architecture.md) section, the application runs in batches—one for each company.

Topics:
+ [Capturing and processing the robots.txt file](#building-crawler-robots-txt)
+ [Capturing and processing the sitemap](#building-crawler-sitemap)
+ [Designing the crawler](#building-crawler-design)

## Capturing and processing the robots.txt file
<a name="building-crawler-robots-txt"></a>

After you prepare the dataset, you need to confirm whether the domain has a [robots.txt](https://en.wikipedia.org/wiki/Robots.txt) file. For web crawlers and other bots, the robots.txt file indicates which sections of the website they are allowed to visit. Honoring the instructions in this file is an important best practice for ethically crawling websites. For more information, see [Best practices for ethical web crawlers](best-practices.md) in this guide.

### To capture and process the robots.txt file
<a name="to-capture-and-process-the-robots.txt-file.c91a8e94-b90e-58e8-85b0-e3f220f97c89"></a>

1. If you haven't done so already, install the `requests` library by running the following command in a terminal:

   ```
   pip install requests
   ```

1. Run the following script. This script does the following:
   + It defines a `check_robots_txt` function that takes a domain as input.
   + It constructs the full URL for the robots.txt file.
   + It sends a GET request to the URL for the robots.txt file.
   + If the request is successful (status code 200), then a robots.txt file exists.
   + If the request fails or returns a different status code, then a robots.txt file doesn't exist or isn't accessible.

   ```
   import requests
   from urllib.parse import urljoin
   def check_robots_txt(domain):
       # Ensure the domain starts with a protocol
       if not domain.startswith(('http://', 'https://')):
           domain = 'https://' + domain
       # Construct the full URL for robots.txt
       robots_url = urljoin(domain, '/robots.txt')
       try:
           # Send a GET request to the robots.txt URL
           response = requests.get(robots_url, timeout=5)
           # Check if the request was successful (status code 200)
           if response.status_code == 200:
               print(f"robots.txt found at {robots_url}")
               return True
           else:
               print(f"No robots.txt found at {robots_url} (Status code: {response.status_code})")
               return False
       except requests.RequestException as e:
           print(f"Error checking {robots_url}: {e}")
           return False
   ```
**Note**
This script handles exceptions for network errors or other issues.

1. If a robots.txt file exists, use the following script to download it:

   ```
   import requests

   def download(self, url):
       response = requests.get(url, headers=self.headers, timeout=5)
       response.raise_for_status()  # Raise an exception for non-2xx responses
       return response.text

   def download_robots_txt(self):
       # Append '/robots.txt' to the URL to get the robots.txt file's URL
       robots_url = self.url.rstrip('/') + '/robots.txt'
       try:
           response = download(robots_url)
           return response
       except requests.exceptions.RequestException as e:
           print(f"Error downloading robots.txt: {e}, \nGenerating sitemap using combinations...")
           return e
   ```
**Note**
These scripts can be customized or modified according to your use case. You can also combine these scripts.

## Capturing and processing the sitemap
<a name="building-crawler-sitemap"></a>

Next, you need to process the [sitemap](https://en.wikipedia.org/wiki/Site_map). You can use the sitemap to focus crawling on important pages. This improves the crawling efficiency. For more information, see [Best practices for ethical web crawlers](best-practices.md) in this guide.

### To capture and process the sitemap
<a name="to-capture-and-process-the-sitemap.42898c4e-0876-5eae-a363-95d158a19187"></a>

Run the following script. This script defines a `check_and_download_sitemap` function that:
+ Accepts a base URL, an optional sitemap URL from robots.txt, and a user-agent string.
+ Checks multiple potential sitemap locations, including the one from robots.txt (if provided).
+ Attempts to download the sitemap from each location.
+ Verifies that the downloaded content is in XML format.
+ Calls the `parse_sitemap` function to extract the URLs. This function:
  + Parses the XML content of the sitemap.
  + Handles both regular sitemaps and sitemap index files.
  + Recursively fetches sub-sitemaps if a sitemap index is encountered.

```
import requests
from urllib.parse import urljoin
import xml.etree.ElementTree as ET

def check_and_download_sitemap(base_url, robots_sitemap_url=None, user_agent='SitemapBot/1.0'):
    headers = {'User-Agent': user_agent}
    sitemap_locations = [robots_sitemap_url, urljoin(base_url, '/sitemap.xml'), urljoin(base_url, '/sitemap_index.xml'),
        urljoin(base_url, '/sitemap/'), urljoin(base_url, '/sitemap/sitemap.xml')]

    for sitemap_url in sitemap_locations:
        if not sitemap_url:
            continue
        print(f"Checking for sitemap at: {sitemap_url}")
        try:
            response = requests.get(sitemap_url, headers=headers, timeout=10)
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', '')
                if 'xml' in content_type:
                    print(f"Successfully downloaded sitemap from {sitemap_url}")
                    return parse_sitemap(response.text)
                else:
                    print(f"Found content at {sitemap_url}, but it's not XML. Content-Type: {content_type}")
        except requests.RequestException as e:
            print(f"Error downloading sitemap from {sitemap_url}: {e}")
    print("No sitemap found.")
    return []

def parse_sitemap(sitemap_content):
    urls = []
    try:
        root = ET.fromstring(sitemap_content)
        # Handle both sitemap and sitemapindex
        for loc in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
            urls.append(loc.text)

        # If it's a sitemap index, recursively fetch each sitemap
        if root.tag.endswith('sitemapindex'):
            all_urls = []
            for url in urls:
                print(f"Fetching sub-sitemap: {url}")
                sub_sitemap_urls = check_and_download_sitemap(url)
                all_urls.extend(sub_sitemap_urls)
            return all_urls
    except ET.ParseError as e:
        print(f"Error parsing sitemap XML: {e}")
    return urls

if __name__ == "__main__":
    base_url = input("Enter the base URL of the website: ")
    robots_sitemap_url = input("Enter the sitemap URL from robots.txt (or press Enter if none): ").strip() or None
    urls = check_and_download_sitemap(base_url, robots_sitemap_url)
    print(f"Found {len(urls)} URLs in sitemap:")
    for url in urls[:5]:  # Print first 5 URLs as an example
        print(url)
    if len(urls) > 5:
        print("...")
```

## Designing the crawler
<a name="building-crawler-design"></a>

Next, you design the web crawler. The crawler is designed to follow the best practices described in [Best practices for ethical web crawlers](best-practices.md) in this guide. This `EthicalCrawler` class demonstrates several key principles of ethical crawling:
+ **Fetching and parsing the robots.txt file** – The crawler fetches the robots.txt file for the target website.
+ **Respecting crawling permissions** – Before crawling any URL, the crawler checks if the rules in the robots.txt file allow crawling for that URL. If a URL is disallowed, then the crawler skips it and moves to the next URL.
+ **Honoring crawl delay** – The crawler checks for a crawl-delay directive in the robots.txt file. If one is specified, the crawler uses this delay between requests. Otherwise, it uses a default delay.
+ **User-agent identification** – The crawler uses a custom user-agent string to identify itself to websites. If needed, website owners can set specific rules to restrict or allow your crawler.
+ **Error handling and graceful degradation** – If the robots.txt file can't be fetched or parsed, the crawler proceeds with conservative default rules. It handles network errors and non-200 HTTP responses.
+ **Limited crawling** – To avoid overwhelming the server, there is a limit to how many pages can be crawled.

The following script is pseudocode that explains how the web crawler works:

```
import requests
from urllib.parse import urljoin, urlparse
import time

class EthicalCrawler:
    def __init__(self, start_url, user_agent='EthicalBot/1.0'):
        self.start_url = start_url
        self.user_agent = user_agent
        self.domain = urlparse(start_url).netloc
        self.robots_parser = None
        self.crawl_delay = 1  # Default delay in seconds

    def can_fetch(self, url):
        if self.robots_parser:
            return self.robots_parser.allowed(url, self.user_agent)
        return True  # If no robots.txt, assume allowed but crawl conservatively

    def get_crawl_delay(self):
        if self.robots_parser:
            delay = self.robots_parser.agent(self.user_agent).delay
            if delay is not None:
                self.crawl_delay = delay
        print(f"Using crawl delay of {self.crawl_delay} seconds")

    def crawl(self, max_pages=10):
        self.get_crawl_delay()
        pages_crawled = 0
        urls_to_crawl = [self.start_url]
        while urls_to_crawl and pages_crawled < max_pages:
            url = urls_to_crawl.pop(0)
            if not self.can_fetch(url):
                print(f"robots.txt disallows crawling: {url}")
                continue
            try:
                response = requests.get(url, headers={'User-Agent': self.user_agent})
                if response.status_code == 200:
                    print(f"Successfully crawled: {url}")
                    # Here you would typically parse the content, extract links, etc.
                    # For this example, we'll just increment the counter
                    pages_crawled += 1
                else:
                    print(f"Failed to crawl {url}: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error crawling {url}: {e}")

            # Respect the crawl delay
            time.sleep(self.crawl_delay)

        print(f"Crawling complete. Crawled {pages_crawled} pages.")
```

### To build an advanced, ethical web crawler that collects ESG data
<a name="to-build-an-advanced--ethical-web-crawler-that-collects-esg-data.183b8dfc-e84e-5461-bd88-7740caea17c8"></a>

1. Copy the following code sample for the advanced ethical web crawler used in this system:

   ```
   import requests
   from urllib.parse import urljoin, urlparse
   import time
   from collections import deque
   import random
   from bs4 import BeautifulSoup
   import re
   import csv
   import os

   class EnhancedESGCrawler:
       def __init__(self, start_url):
           self.start_url = start_url
           self.domain = urlparse(start_url).netloc
           self.desktop_user_agent = 'ESGEthicalBot/1.0'
           self.mobile_user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
           self.robots_parser = None
           self.crawl_delay = None
           self.urls_to_crawl = deque()
           self.crawled_urls = set()
           self.max_retries = 2
           self.session = requests.Session()
           self.esg_data = []
           self.news_links = []
           self.pdf_links = []

       def setup(self):
           self.fetch_robots_txt() # Provided in Previous Snippet
           self.fetch_sitemap() # Provided in Previous Snippet

       def can_fetch(self, url, user_agent):
           if self.robots_parser:
               return self.robots_parser.allowed(url, user_agent)
           return True

       def delay(self):
           if self.crawl_delay is not None:
               time.sleep(self.crawl_delay)
           else:
               time.sleep(random.uniform(1, 3))

       def get_headers(self, user_agent):
           return {'User-Agent': user_agent,
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'DNT': '1',
                   'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1'}

       def extract_esg_data(self, url, html_content):
           soup = BeautifulSoup(html_content, 'html.parser')
           esg_data = {
               'url': url,
               'environmental': self.extract_environmental_data(soup),
               'social': self.extract_social_data(soup),
               'governance': self.extract_governance_data(soup)
           }
           self.esg_data.append(esg_data)
           # Extract news links and PDFs
           self.extract_news_links(soup, url)
           self.extract_pdf_links(soup, url)

       def extract_environmental_data(self, soup):
           keywords = ['carbon footprint', 'emissions', 'renewable energy', 'waste management', 'climate change']
           return self.extract_keyword_data(soup, keywords)

       def extract_social_data(self, soup):
           keywords = ['diversity', 'inclusion', 'human rights', 'labor practices', 'community engagement']
           return self.extract_keyword_data(soup, keywords)

       def extract_governance_data(self, soup):
           keywords = ['board structure', 'executive compensation', 'shareholder rights', 'ethics', 'transparency']
           return self.extract_keyword_data(soup, keywords)

       def extract_keyword_data(self, soup, keywords):
           text = soup.get_text().lower()
           return {keyword: len(re.findall(r'\b' + re.escape(keyword) + r'\b', text)) for keyword in keywords}

       def extract_news_links(self, soup, base_url):
           news_keywords = ['news', 'press release', 'article', 'blog', 'sustainability']
           for a in soup.find_all('a', href=True):
               if any(keyword in a.text.lower() for keyword in news_keywords):
                   full_url = urljoin(base_url, a['href'])
                   if full_url not in self.news_links:
                       self.news_links.append({'url': full_url, 'text': a.text.strip()})

       def extract_pdf_links(self, soup, base_url):
           for a in soup.find_all('a', href=True):
               if a['href'].lower().endswith('.pdf'):
                   full_url = urljoin(base_url, a['href'])
                   if full_url not in self.pdf_links:
                       self.pdf_links.append({'url': full_url, 'text': a.text.strip()})

       def is_relevant_to_sustainable_finance(self, text):
           keywords = ['sustainable finance', 'esg', 'green bond', 'social impact', 'environmental impact',
                       'climate risk', 'sustainability report', 'corporate responsibility']
           return any(keyword in text.lower() for keyword in keywords)

       def attempt_crawl(self, url, user_agent):
           for _ in range(self.max_retries):
               try:
                   response = self.session.get(url, headers=self.get_headers(user_agent), timeout=10)
                   if response.status_code == 200:
                       print(f"Successfully crawled: {url}")
                       if response.headers.get('Content-Type', '').startswith('text/html'):
                           self.extract_esg_data(url, response.text)
                       elif response.headers.get('Content-Type', '').startswith('application/pdf'):
                           self.save_pdf(url, response.content)
                       return True
                   else:
                       print(f"Failed to crawl {url}: HTTP {response.status_code}")
               except requests.RequestException as e:
                   print(f"Error crawling {url} with {user_agent}: {e}")

               self.delay()
           return False

       def crawl_url(self, url):
           if not self.can_fetch(url, self.desktop_user_agent):
               print(f"Robots.txt disallows desktop user agent: {url}")
               if self.can_fetch(url, self.mobile_user_agent):
                   print(f"Attempting with mobile user agent: {url}")
                   return self.attempt_crawl(url, self.mobile_user_agent)
               else:
                   print(f"Robots.txt disallows both user agents: {url}")
                   return False

           return self.attempt_crawl(url, self.desktop_user_agent)

       def crawl(self, max_pages=100):
           self.setup()

           if not self.urls_to_crawl:
               self.urls_to_crawl.append(self.start_url)

           pages_crawled = 0
           while self.urls_to_crawl and pages_crawled < max_pages:
               url = self.urls_to_crawl.popleft()
               if url not in self.crawled_urls:
                   if self.crawl_url(url):
                       pages_crawled += 1
                   self.crawled_urls.add(url)
                   self.delay()

           print(f"Crawling complete. Successfully crawled {pages_crawled} pages.")
           self.save_esg_data()
           self.save_news_links()
           self.save_pdf_links()

       def save_esg_data(self):
           with open('esg_data.csv', 'w', newline='', encoding='utf-8') as file:
               writer = csv.DictWriter(file, fieldnames=['url', 'environmental', 'social', 'governance'])
               writer.writeheader()
               for data in self.esg_data:
                   writer.writerow({
                       'url': data['url'],
                       'environmental': ', '.join([f"{k}: {v}" for k, v in data['environmental'].items()]),
                       'social': ', '.join([f"{k}: {v}" for k, v in data['social'].items()]),
                       'governance': ', '.join([f"{k}: {v}" for k, v in data['governance'].items()])
                   })
           print("ESG data saved to esg_data.csv")

       def save_news_links(self):
           with open('news_links.csv', 'w', newline='', encoding='utf-8') as file:
               writer = csv.DictWriter(file, fieldnames=['url', 'text', 'relevant'])
               writer.writeheader()
               for news in self.news_links:
                   writer.writerow({
                       'url': news['url'],
                       'text': news['text'],
                       'relevant': self.is_relevant_to_sustainable_finance(news['text'])
                   })
           print("News links saved to news_links.csv")

       def save_pdf_links(self):
           # Code for saving PDF in S3 or filesystem

       def save_pdf(self, url, content):
           # Code for saving PDF in S3 or filesystem

   # Example usage
   if __name__ == "__main__":
       start_url = input("Enter the starting URL to crawl for ESG data and news: ")
       crawler = EnhancedESGCrawler(start_url)
       crawler.crawl(max_pages=50)
   ```

1. Set up the various attributes, including user agents, empty collections for URLs, and data storage lists.

1. Adjust the keywords and relevance criteria in the `is_relevant_to_sustainable_finance()` method to match your specific needs.

1. Make sure that the robots.txt file permits crawling the website and that you are using the crawl delay and user agent specified in the robots.txt file.

1. Consider making the following customizations to the provided web crawler script, as needed for your organization:
   + Implement the `fetch_sitemap()` method for more efficient URL discovery.
   + Enhance error logging and handling for production use.
   + Implement more sophisticated content relevance analysis.
   + Add depth and breadth controls to limit crawling scope.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
