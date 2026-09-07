---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/evolving-the-architecture-with-amazon-cloudfront.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Evolving the architecture with Amazon CloudFront
<a name="evolving-the-architecture-with-amazon-cloudfront"></a>

 Amazon CloudFront content delivery web service integrates with other AWS products to give you an easy way to distribute content to users on your website with low latency, high data transfer speeds, and no minimum usage commitments.

## Factors contributing to page load latency
<a name="factors-contributing-to-page-load-latency"></a>

 To explore factors that contribute to latency, we use the example of a user in Singapore visiting a web page hosted from an Amazon S3 bucket in the US West (Oregon) Region in the United States. From the moment the user visits a web page to the moment it shows up in the browser, several factors contribute to latency:
+  **FACTOR (1)** Time it takes for the browser (Singapore) to request the web page from Amazon S3 (US West [Oregon] Region).
+  **FACTOR (2)** Time it takes for Amazon S3 to retrieve the page contents and serve up the page.
+  **FACTOR (3)** Time it takes for the page contents (US West [Oregon] Region) to be delivered across the Internet to the browser (Singapore).
+  **FACTOR (4)** Time it takes for the browser to parse and display the web page. This latency is illustrated in the following figure.

![A diagram showing factors affecting page load latency.](https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/page-load-factors.png)

 AWS addresses **FACTOR (2)** by optimizing Amazon S3 to serve up content as quickly as possible. You can improve **FACTOR (4)** by optimizing the actual page content (for example, minifying CSS and JavaScript, using efficient image and video formats). However, page- loading studies consistently show that most latency is due to **FACTOR (1)** and **FACTOR (3)**. (We find that the performance penalty incurred by a web flow due to its TCP handshake is between 10% and 30% of the latency to serve the HTTP request, as we show in detail in Section 2 of [TCP Fast Open](https://raghavan.usc.edu/papers/tfo-conext11.pdf).)

 Most of the delay in accessing pages over the internet is due to the round-trip delay associated with establishing TCP connections (the infamous three-way TCP handshake) and the time it takes for TCP packets to be delivered across long Internet distances).

 In short, serve content as close to your users as possible. In our example, users in the USA will experience relatively fast page load times, whereas users in Singapore will experience slower page loads. Ideally, for the users in Singapore, you would want to serve up content as close to Singapore as possible.
