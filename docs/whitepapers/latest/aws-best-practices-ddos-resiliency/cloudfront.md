---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/cloudfront.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon CloudFront
<a name="cloudfront"></a>

 Amazon CloudFront can help reduce server load by preventing non-web traffic from reaching your origin. To send a request to a CloudFront application, the connection must be established with a valid IP address through a completed TCP handshake, which cannot be faked. Additionally, CloudFront can automatically close connections from slow reading or slow writing attackers (for example, [Slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security))).

## CDN caching
<a name="cdn-caching"></a>

 CloudFront allows you to serve both dynamic content and static content from AWS edge locations. By serving proxy cacheable content from CDN cache you prevent requests from reaching your origin from a given edge cache node for the duration of the caching TTL. In conjunction with [request collapsing](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-traffic-spikes) for expired but cacheable content, even very short TTL mean that negligible numbers of requests will reach your origin during request floods for that content. In addition enabling features like [CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html) can further help reduce the load on your origin – anything you can do to [improve your cache hit ratio](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html) can mean the difference between an impactful and non-impactful request flood attack.
