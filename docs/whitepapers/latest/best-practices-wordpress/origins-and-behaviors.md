---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/origins-and-behaviors.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Origins and behaviors
<a name="origins-and-behaviors"></a>

 An [origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html) is a location where CloudFront sends requests for content that it distributes through the edge locations. Depending on your implementation you can have one or two origins. One for dynamic content (the Lightsail instance in the [single-server deployment option](simple-deployment.md), or the Application Load Balancer in the [elastic deployment option](elastic-deployment.md)) using a custom origin. You may have a second origin to direct CloudFront to for your static content. In the preceding [reference architecture](reference-architecture.md), this is an S3 bucket. When you use Amazon S3 as an origin for your distribution, you need to use a [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html) to make the content publicly accessible.

 [Behaviors](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehavior.html) allow you to set rules that govern how CloudFront caches your content, and, in turn, determine how effective the cache is. Behaviors allow you to control the protocol and HTTP methods your website is accessible by. They also allow you to control whether to pass HTTP headers, cookies, or query strings to your backend (and, if so, which ones). Behaviors apply to specific URL path patterns.
