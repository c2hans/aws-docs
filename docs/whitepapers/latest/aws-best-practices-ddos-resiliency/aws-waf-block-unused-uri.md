---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf-block-unused-uri.html
---

# AWS WAF – Block access to unused URI paths and file extensions
<a name="aws-waf-block-unused-uri"></a>

 Block access to unused URI paths using AWS WAF. The most obvious example here would be the '/' URI path for an API endpoint, which would typically return an HTTP 404 (Not Found).

 Likewise consider blocking access to file extensions that you don't use, for example: `if NOT uri_path matches regex .*\.(css|js|png|jpg|svg|woff2|html|json)$ AND uri_path contains '.'`

 Blocking access to such paths prevents sudden high-volume request floods on non-existent or mutating URLs from overwhelming your target group (for ALB endpoints) or origin (for CloudFront).
