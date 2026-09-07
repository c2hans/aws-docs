---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/speeding-up-your-amazon-s3-based-website-using-amazon-cloudfront.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Speeding up your Amazon S3-based website using Amazon CloudFront
<a name="speeding-up-your-amazon-s3-based-website-using-amazon-cloudfront"></a>

 Amazon CloudFront is a CDN that uses a global network of edge locations for content delivery. Amazon CloudFront also provides reports to help you understand how users are using your website.

 As a CDN, Amazon CloudFront can distribute content with low latency and high data transfer rates. There are multiple [CloudFront edge](https://aws.amazon.com/cloudfront/details/) locations all around the world.

 Therefore, no matter where a visitor lives in the world, there is an Amazon CloudFront edge location that is relatively close (from an Internet latency perspective).

 The Amazon CloudFront edge locations cache content from an origin server and deliver that cached content to the user. When creating an [Amazon CloudFront distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/MigrateS3ToCloudFront.html), specify your Amazon S3 bucket as the origin server. The Amazon CloudFront distribution itself has a DNS. You can refer to it using a CNAME if you have a custom domain name. To point the A record of a root domain to an Amazon CloudFront distribution, you can use Amazon Route 53 alias records, as illustrated in the following diagram.

![A diagram that depcits using Amazon Route 53 alias records with an Amazon Cloudfront distribution .](https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/s3-alias-records.jpeg)

 Amazon CloudFront also keeps persistent connections with your origin servers so that those files can be fetched from the origin servers as quickly as possible. Finally, Amazon CloudFront uses additional optimizations (for example, wider TCP initial congestion window) to provide higher performance while delivering your content to viewers.

 When an end user requests a web page using that domain name, CloudFront determines the best edge location to serve the content. If an edge location doesn’t yet have a cached copy of the requested content, CloudFront pulls a copy from the Amazon S3 origin server and holds it at the edge location to fulfill future requests. Subsequent users requesting the same content from that edge location experience faster page loads because that content is already cached. The following diagram shows the flow in detail.

![A diagram that shows how Amazon CloudFront caches content.](https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/cloudfront-caching.png)
