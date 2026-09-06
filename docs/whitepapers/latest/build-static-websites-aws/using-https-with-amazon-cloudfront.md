---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/using-https-with-amazon-cloudfront.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using HTTPS with Amazon CloudFront
<a name="using-https-with-amazon-cloudfront"></a>

 You can configure Amazon CloudFront to require that viewers use HTTPS to request your objects, so that connections are encrypted when Amazon CloudFront communicates with viewers. You can also configure Amazon CloudFront to use HTTPS to get objects from your origin, so that connections are encrypted when Amazon CloudFront communicates with your origin. If you want to require HTTPS for communication between Amazon CloudFront and Amazon S3, you must change the value of the Viewer Protocol Policy to Redirect HTTP to HTTPS or HTTPS Only.

 We recommend using Redirect HTTP to HTTPS. Viewers can use both protocols. HTTP GET and HEAD requests are automatically redirected to HTTPS requests. Amazon CloudFront returns HTTP status code 301 (Moved Permanently) along with the new HTTPS URL. The viewer then resubmits the request to Amazon CloudFront using the HTTPS URL.

## Amazon CloudFront reports
<a name="amazon-cloudfront-reports"></a>

 Amazon CloudFront includes a set of reports that provide insight into and answers to the following questions:
+  What is the overall health of my website?
+  How many visitors are viewing my website?
+  Which browsers, devices, and operating systems are they using?
+  Which countries are they coming from?
+  Which websites are the top referrers to my site?
+  What assets are the most popular ones on my site?
+  How often is CloudFront caching taking place?

 Amazon CloudFront reports can be used alongside other online analytics tools, and we encourage the use of multiple reporting tools. Note that some analytics tools may require you to embed client-side JavaScript in your HTML pages. Amazon CloudFront reporting does not require any changes to your web pages. See the [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/reports.html) for more information on reports.
