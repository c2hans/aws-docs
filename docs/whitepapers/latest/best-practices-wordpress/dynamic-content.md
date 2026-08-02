---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/dynamic-content.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Dynamic content
<a name="dynamic-content"></a>

 Dynamic content includes the output of server-side WordPress PHP scripts. Dynamic content can also be served via CloudFront by configuring the WordPress website as an origin. Since dynamic content includes personalized content, you need to configure CloudFront to forward certain HTTP cookies and HTTP headers as part of a request to your custom origin server. CloudFront uses the forwarded cookie values as part of the key that identifies a unique object in its cache. To ensure that you maximize the caching efficiency, you should configure CloudFront to only forward those HTTP cookies and HTTP headers that really vary the content (not cookies that are only used on the client side or by third-party applications, for example, for web analytics).

![Whole website delivery via Amazon CloudFront](http://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/images/image3.png)

* Whole website delivery via Amazon CloudFront *

 The preceding figure includes two origins: one for static content and another for dynamic content. For implementation details, see [Appendix A: CloudFront configuration](appendix-a-cloudfront-configuration.md) and [Appendix B: Plugins installation and configuration](appendix-b-plugins-installation-and-configuration.md).

 CloudFront uses standard cache control headers to identify if and for how long it should cache specific HTTP responses. The same cache control headers are also used by web browsers to decide when and for how long to cache content locally for a more optimal end user experience (for example, a `.css` file that is already downloaded will not be re-downloaded every time a returning visitor views a page). You can configure cache control headers on the web server level (for example, via `.htaccess` files or modifications of the `httpd.conf` file) or install a WordPress plugin (for example, W3 Total Cache) to dictate how those headers are set for both static and dynamic content.
