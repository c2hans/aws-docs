---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/architecture.html
---

# Architecture for a scalable web crawling system on AWS
<a name="architecture"></a>

The following architecture diagram shows a web crawler system that is designed to ethically extract environmental, social, and governance (ESG) data from websites. You use a Python-based crawler that is optimized for AWS infrastructure. You use AWS Batch to orchestrate the large-scale crawling jobs and use Amazon Simple Storage Service (Amazon S3) for storage. Downstream applications can ingest and store the data from the Amazon S3 bucket.

![Using a web crawler system to extract ESG data from websites.](http://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/images/guide-img/c05f0876-d987-41f0-9b7d-d5d908a52b17/images/82a1d2f5-a0c3-4d71-9758-d896f68f23a2.png)

The diagram shows the following workflow:

1. Amazon EventBridge Scheduler initiates the crawling process at an interval that you schedule.

1. AWS Batch manages the execution of the web crawler jobs. The AWS Batch job queue holds and orchestrates the pending crawling jobs.

1. The web crawling jobs run in Amazon Elastic Container Service (Amazon ECS) containers on AWS Fargate. The jobs run in a public subnet of a virtual private cloud (VPC).

1. The web crawler crawls the target website and retrieves ESG data and documents, such as PDF, CSV, or other document files.

1. The web crawler stores the retrieved data and raw files in an Amazon S3 bucket.

1. Other systems or applications ingest or process the stored data and files in the Amazon S3 bucket.

## Web crawler design and operations
<a name="architecture-crawler"></a>

Some websites are specifically designed to be run on desktops or on mobile devices. The web crawler is designed to support the use of a desktop user agent or a mobile user agent. These agents help you successfully make requests to the target website.

After the web crawler is initialized, it performs the following operations:

1. The web crawler calls the `setup()` method. This method fetches and parses the robots.txt file.
**Note**
You can also configure the web crawler to fetch and parse the sitemap.

1. The web crawler processes the robots.txt file. If a crawl delay is specified in the robots.txt file, the web crawler extracts the crawl delay for the desktop user agent. If a crawl delay is not specified in the robots.txt file, then the web crawler uses a random delay.

1. The web crawler calls the `crawl()` method, which initiates the crawling process. If no URLs are in the queue, it adds the start URL.
**Note**
The crawler continues until it reaches the maximum number of pages or runs out of URLs to crawl.

1. The crawler processes the URLs. For each URL in the queue, the crawler checks if the URL has already been crawled.

1. If a URL hasn't been crawled, the crawler calls the `crawl_url()` method as follows:

   1. The crawler checks the robots.txt file to determine whether it can use the desktop user agent to crawl the URL.

   1. If allowed, the crawler attempts to crawl the URL by using the desktop user agent.

   1. If not allowed or if the desktop user agent fails to crawl, then the crawler checks the robots.txt file to determine whether it can use the mobile user agent to crawl the URL.

   1. If allowed, the crawler attempts to crawl the URL by using the mobile user agent.

1. The crawler calls the `attempt_crawl()` method, which retrieves and processes the content. The crawler sends a GET request to the URL with appropriate headers. If the request fails, the crawler uses retry logic.

1. If the file is in HTML format, the crawler calls the `extract_esg_data()` method. It uses [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) to parse the HTML content. It extracts environmental, social, and governance (ESG) data by using keyword matching.

   If the file is a PDF, the crawler calls the `save_pdf()` method. The crawler downloads and saves the PDF file to the Amazon S3 bucket.

1. The crawler calls the `extract_news_links()` method. This finds and stores links to news articles, press releases, and blog posts.

1. The crawler calls the `extract_pdf_links()` method. This identifies and stores links to PDF documents.

1. The crawler calls the `is_relevant_to_sustainable_finance()` method. This checks whether the news or articles are related to sustainable finance by using predefined keywords.

1. After each crawl attempt, the crawler implements a delay by using the `delay()` method. If a delay was specified in the robots.txt file, it uses that value. Otherwise, it uses a random delay between 1 and 3 seconds.

1. The crawler calls the `save_esg_data()` method to save the ESG data to a CSV file. The CSV file is saved in the Amazon S3 bucket.

1. The crawler calls the `save_news_links()` method to save the news links to a CSV file, including relevance information. The CSV file is saved in the Amazon S3 bucket.

1. The crawler calls the `save_pdf_links()` method to save the PDF links to a CSV file. The CSV file is saved in the Amazon S3 bucket.

## Batching and data processing
<a name="architecture-batching"></a>

The crawling process is organized and performed in a structured manner. AWS Batch assigns the jobs for each company so that they run in parallel, in batches. Each batch focuses on a single company's domain and subdomains, as you've identified them in your dataset. However, jobs in the same batch run sequentially so that they do not inundate the website with too many requests. This helps the application to manage the crawling workload more efficiently and make sure that all relevant data is captured for each company.

By organizing the web crawling into company-specific batches, this containerizes the collected data. This helps prevent the data from one company from being mixed with data from other companies.

Batching helps the application efficiently gather data from the web, while maintaining a clear structure and separation of information based on the target companies and their respective web domains. This approach helps to ensure the integrity and usability of the data collected, as it is neatly organized and associated with the appropriate company and domains.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
