---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/cloudfront.html
---

# Amazon CloudFront
<a name="cloudfront"></a>

 Amazon CloudFront is a content delivery network (CDN) that helps protect HTTP/S-based applications in the following ways:
+  CloudFront protects your backend services by validating connections at multiple network layers. Each request must establish a proper TCP or UDP (for QUIC and HTTP/3) session, complete a TLS handshake (for HTTPS), and provide a well-formed HTTP gRPC request. This multi-layer validation filters out malformed or incomplete connection attempts before they reach your origin.
+  CloudFront edge locations provide automatic, always-on mitigation of network and transport layer (Layer 3 and 4) attacks, protecting both the CDN service and your origin infrastructure.
+  CloudFront automatically closes connections from slow reading or slow writing attackers (for example, [Slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security))), or novel attacks such as HTTP/2 rapid reset.
+  CloudFront provides built-in protection against common HTTP protocol attacks, including HTTP request smuggling, HTTP desync attacks, and request splitting.
+  CloudFront WAF capacity is scaled to match the CloudFront points of presence (POP) capacity—the capacity constraints of Regional WAF don't apply.
+  The CloudFront global edge network provides massive absorption capacity for traffic spikes, regardless of where your origin is hosted. Whether your backend infrastructure is in AWS, another cloud provider, or on-premises, CloudFront can be combined with properly configured WAF rules and effective caching strategies to absorb large-scale request floods that would otherwise overwhelm backend origin services.

## HTTP caching
<a name="cdn-caching"></a>

**CloudFront**

 Amazon CloudFront caching capabilities are a powerful tool for protecting your origin servers' capacity, even with dynamic content delivery. By implementing strategic caching policies, even with short time to live (TTL), you can significantly reduce the load on your origin infrastructure.

 When content is served from the CloudFront [cache hierarchy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ConfiguringCaching.html)—edge POPs (points of presence closest to users), Regional Edge Caches (RECs, larger consolidated caching layers that sit between POPs and your origin), and Origin Shield (an additional centralized caching layer that reduces origin load by acting as a single point of contact for cache fills)—requests might be served as cache objects from downstream peers in the network, preventing volume from reaching your origin.

 For content that isn't yet cached or has expired, CloudFront [request collapsing](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-traffic-spikes) further protects origins by consolidating multiple simultaneous requests into a single origin request. This combination of edge caching and request collapsing means that even during high-traffic events or volumetric request floods, only a fraction of requests need to reach your origin service, making CDN caching an essential strategy for origin capacity preservation.

 There's a common misconception among content owners that their content isn't CDN-cacheable, when in fact it can be cached or be made to be cacheable. Even when dealing with real dynamic content delivered through asynchronous requests, the main page structure itself can and should be cached. Maximizing the [cache hit ratio](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html) is crucial for performance and DDoS resilience—it can be the determining factor between whether an HTTP request flood attack impacts your service or not.

**Important**
Page cacheability should be established as a non-functional requirement during the initial planning stages of any website deployment.
Did you know? Statistically, the '/' URI is the most commonly targeted URI by bad actors in HTTP request floods.

 The following are some solutions to consider for some common perceived blockers to caching static content:
+  For web pages that require immediate updates when new content is published, content freshness can be managed through multiple strategies, using HTTP standard [Cache-Control response header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) directives, CloudFront [caching policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html) settings, or a combination of the two as follows:
  +  Implement a split TTL approach: Set 0 TTL for viewers using the Cache-Control response header `max-age=0` directive. This means that clients will always check for content freshness on page re-load. Set longer TTLs at the CDN level using a non-zero [minimum TTL](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesMinTTL) in the relevant distribution caching policy (using the managed [CachingOptimized](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html#managed-cache-caching-optimized) cache policy makes sense here). You can also optionally add the [`s-maxage` Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#s-maxage) response header directive at the origin to increase the CDN caching time above the minimum TTL.
  +  Use microcaching with minimum TTL values as low as 1 or 2 seconds for non-personalized but highly dynamic content such as election results or live streaming manifests.
  +  Set Etag or Last-Modified response headers to enable [conditional requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html#stale-content). When content hasn't changed, CloudFront responds with an [HTTP 304 (Not Modified)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/304) status and a zero-byte response body, which optimizes page load times and minimizes Data Transfer Out charges.
  +  Use CloudFront [cache invalidations](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html), which can be automatically triggered through content management system integrations during publish events—be aware that there are limits in terms of requests per second for these cache invalidation APIs.
+  For static assets such as images, scripts, and other page resources, implement unique file versioning with higher TTL values (1 year or more). Instead of updating files in place, publish new versions with unique URIs or query strings, and update their references in HTML. This strategy provides optimal delivery efficiency and maximum offload across browser caches, CDN cache, and origin services while ensuring immediate content updates through reference changes rather than cache invalidations.
+  For sites with mixed content, create multiple cache behaviors with appropriate cache policies to maximize DDoS resilience. While static content should be aggressively cached, truly dynamic endpoints that can't be cached should be identified early and protected with additional controls such as scoped-down AWS WAF [rate-based rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-request-limiting.html) with lower limits than any rate-based rules that are broadly applied.
+  Non-personalized HTML with Cache-Control header directives like `no-cache`, `no-store` can be cached on CDN by using a non-zero [Minimum TTL](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesMinTTL) in the relevant CloudFront cache behavior.
+  In a situation where the origin performance has been adversely impacted, consider adding the [`stale-while-revalidate`](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html#stale-content) Cache-Control directive, so that users no longer need to wait for responses from the origin. It's ideal for content that refreshes frequently or unpredictably, or where content requires significant time to regenerate, and where having the latest version of the content isn't essential.
+  If you have an adaptive website and serve different pages based on device-type, you can configure caching based on device type by updating both the cache policy and [origin request policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html) to use [device type headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html#header-caching-web-device).
+  The [`stale-if-error` directive](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html#stale-if-error-only) enhances the user experience and improves availability by serving stale content when origins return an error.
+  Most major content management systems (CMS) have a plug-in to replicate static content to Amazon S3.

**Note**
 If you [forward all headers to the origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html), caching is disabled regardless of other cache settings.

**Request collapsing**

 Request collapsing occurs when multiple users simultaneously request the same content that isn't in cache. CloudFront intelligently manages these requests by sending only one to the origin server, while briefly pausing all the others. After CloudFront receives the origin's response, it serves this cached content to all waiting requests, preventing a flood of duplicate requests from the same caching instance from overwhelming your origin server during a typical DDoS attack.

 The following configurations prevent request collapsing from occurring:
+  The minimum TTL is 0
+  Cookie forwarding is enabled in [the cache policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html), [the origin request policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html), or the legacy cache settings

**Note**
 A request flood attack in conjunction with non-collapsed but otherwise cacheable requests, can be sufficient to overwhelm some origins, especially those that are unable to dynamically scale.

**Origin shield**

 Enabling features like [CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html) can help further reduce the load on your origin by enabling a centralized caching layer. This can be useful for low-capacity origins that are unable to dynamically scale.

**Error pages and error caching**

 CloudFront [caches some 4xx and 5xx status codes](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HTTPStatusCodes.html#HTTPStatusCodes-cached-errors) returned by your origin for a default duration of 10 seconds. While it might seem illogical to cache server errors, doing so can prevent a snowball effect of viewer retries from an error response further degrading an origin's heath. Another option is to use the `stale-if-error` Cache-Control directive for content that is cached.

 In addition, you can now use CloudFront to create [custom error pages](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/creating-custom-error-pages.html). If you choose to configure these, we recommend:
+  Storing error pages in an alternate origin, such as an Amazon S3 bucket, so that CloudFront can access them, even when your other origins are returning errors.
+  Enabling CDN caching for the error pages with a longer minimum TTL than the error caching TTL to minimize requests to the origin containing the error pages.

## Amazon EC2-based caching
<a name="ec2-based-caching"></a>

 There are some use cases, such as requiring regional TLS-termination, where customers don't want to use a global CDN like CloudFront. In this case, it's worth setting up a dynamically scaled EC2 instance running a cache such as Varnish, to protect the content source.
