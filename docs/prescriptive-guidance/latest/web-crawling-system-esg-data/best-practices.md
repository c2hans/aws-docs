---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/best-practices.html
---

# Best practices for ethical web crawlers
<a name="best-practices"></a>

This section discusses best practices and key ethical considerations for building a web-crawling application that collects environmental, social, and governance (ESG) data. By adhering to these best practices, you can protect your project and organization and contribute to a more responsible and sustainable web ecosystem. This approach helps you access valuable data and use it for research, business, and innovation in a way that respects all stakeholders.

## Robots.txt compliance
<a name="best-practices-robots"></a>

The robots.txt file is used on websites to communicate with web crawlers and bots about which parts of the website should or should not be accessed or crawled. When a web crawler encounters a robots.txt file on a website, it parses the instructions and adjusts its crawling behavior accordingly. This prevents the crawler from violating the website owner's instructions and maintains a cooperative relationship between the website and the crawler. Therefore, the robots.txt file helps with access control, the protection of sensitive content, load management, and legal compliance.

We recommend that you adhere to the following best practices:
+ Always check and respect the rules in the robots.txt file.
+ Before crawling any URL, check the rules for both desktop and mobile user agents.
+ If the website allows only mobile user agents, use a different agent header, such as a mobile agent header, for your request.

The absence of a robots.txt file doesn't necessarily mean you can't or shouldn't crawl a website. Crawling should always be done responsibly, respecting the website's resources and the owner's implicit rights. The following are recommended best practices when a robots.txt is not present:
+ Assume crawling is allowed, but proceed with caution.
+ Implement polite crawling practices.
+ Consider reaching out to the website owner for permission if you plan on performing extensive crawling.

## Crawl-rate limiting
<a name="best-practices-crawl-rate"></a>

Use a reasonable crawl rate to avoid overwhelming the server. Implement delays between requests, either as specified by the robots.txt file or by using a random delay. For small or medium-sized websites, 1 request every 10–15 seconds might be appropriate. For larger websites or those with explicit crawl permissions, 1–2 requests per second might be appropriate.

## User-agent transparency
<a name="best-practices-user-agent"></a>

Identify your crawler in the user-agent header. This HTTP header information is intended to identify the device that is requesting the content. Commonly, the word *bot* is included in the name of the agent. Crawlers and other bots sometimes use an important field in the header to include contact information.

## Efficient crawling
<a name="best-practices-site-map"></a>

Use the sitemap, which is developed by the website owner, in order to focus on important pages.

## Adaptive approach
<a name="best-practices-adaptive"></a>

Program the crawler to switch to a mobile user agent if the desktop version is unsuccessful. This can provide the crawler access and reduce the strain on the website's server.

## Error handling
<a name="best-practices-error-handling"></a>

Make sure that the crawler handles various HTTP status codes appropriately. For example, the crawler should pause if it encounters a 429 status code ("Too many requests"). If the crawler continuously receives 403 status codes ("Forbidden"), then consider stopping crawling.

## Crawling in batches
<a name="best-practices-batches"></a>

We recommend that you do the following:
+ Instead of crawling all the URLs at once, divide the task into smaller batches. This can help distribute the load and reduce the risk of encountering issues, such as timeouts or resource constraints.
+ If the overall crawling task is expected to be long-running, consider dividing it into multiple smaller, more manageable tasks. This can make the process more scalable and resilient.
+ If the number of URLs to crawl is relatively small, consider using a serverless solution, such as AWS Lambda. Lambda functions can be a good fit for short-lived, event-driven tasks because they automatically scale and handle resource management.

## Security
<a name="best-practices-security"></a>

For web-crawling compute tasks, we recommend that you configure the environment to allow outbound traffic only. This helps enhance security by minimizing the attack surface and reducing the risk of unauthorized inbound access. Allowing only outbound connections permits the crawling process to communicate with the target websites and retrieve the necessary data, and it restricts any inbound traffic that could potentially compromise the system.

## Other considerations
<a name="best-practices-other-considerations"></a>

Review the following additional considerations and best practices:
+ Check for crawling guidelines in the website's terms of service or privacy policy.
+ Look for `meta` tags in the HTML that might provide crawling directives.
+ Be aware of legal restrictions in your jurisdiction regarding data collection and use.
+ Be prepared to stop crawling if requested by the website owner.
