---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/faq.html
---

# FAQ
<a name="faq"></a>

## What if a robots.txt file is not available?
<a name="faq1"></a>

The absence of a robots.txt file doesn't necessarily mean you can't or shouldn't crawl a website. Crawling should always be done responsibly, respecting the website's resources and the implicit rights of the website owner.

## What if a sitemaps.xml file is not available?
<a name="faq2"></a>

Depending on the requirement, you can do one of the following:
+ **Search for HTML sitemaps** – Look for an HTML sitemap page that lists the important pages on the website. These are often linked in the footer.
+ **Crawl from the homepage** – Start crawling from the homepage and follow internal links to discover other pages.
+ **Analyze URL patterns** – Analyze the website's URL structure to identify patterns and programmatically generate potential URLs.
+ **Review the robots.txt file** – Check the robots.txt file for any disallowed pages or directories. These can provide clues about the site structure.
+ **Review API endpoints** – Some websites offer API endpoints that can be used to retrieve content and structure information.
+ **Check search engine results** – Use search engines to find indexed pages of the website by using the [site: search operator](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site), such as `site:example.com`.
+ **Analyze backlinks** – Analyze backlinks to the website to discover important pages that other sites are linking to.
+ **Review web archives** – Check internet archives, such as the [Wayback Machine](https://web.archive.org/), for older versions of the site that might have had sitemaps or different structures.
+ **Look for content management system (CMS) patterns** – If you can identify the CMS, use common URL patterns associated with that system.
+ **Confirm JavaScript rendering** – If the site heavily relies on JavaScript, make sure that your crawler can render JavaScript to discover dynamically loaded content. For some websites, the sitemap.xml file loads after JavaScript rendering is enabled.

## Can I use a serverless solution instead of Amazon EC2 or Amazon ECS?
<a name="faq3"></a>

Yes. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions for web crawling can be a viable option, especially for smaller-scale or more modular crawling tasks. However, for large-scale, long-running crawling operations, a more traditional approach that uses Amazon Elastic Compute Cloud (Amazon EC2) instances or Amazon Elastic Container Service (Amazon ECS) might be more suitable. It's important to carefully evaluate your specific requirements and trade-offs when choosing the right compute service for your web crawling needs.

## Why is the crawler getting a 403 status code?
<a name="faq4"></a>

HTTP 403 is an HTTP status code that means access to the requested resource is forbidden. If the request was correct, then the server understood the request and will not fulfill it. To prevent a 403 status code, you can do the following:
+ Limit your crawl rate.
+ Check whether the sitemap or robots.txt file allows the crawler to access the URL.
+ Try with a mobile user agent instead of a desktop user agent.

If none of the above work, you should respect the decision of the website owners and not crawl the page.
