---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS WAF
<a name="aws-waf"></a>

 By using AWS WAF, you can configure web access control lists (Web ACLs) on your global CloudFront distributions or regional resources to filter, monitor and block requests based on request signatures. To determine whether to allow or block requests, you can consider factors such as the IP address or country of origin, certain strings or patterns in the request, the size of specific parts of the request, and the presence of malicious SQL code or scripting. You can also run CAPTCHA puzzles and silent client session challenges against requests.

 Both AWS WAF and CloudFront also enable you to set geo-restrictions to block or allow requests from selected countries. This can help block or rate-limit attacks from geographic locations where you do not expect to serve users. With fine-grained geographic match rule statements in AWS WAF, you can control access down to the region level.

 You can use [Scope-down statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-scope-down-statements.html) to narrow the scope of the requests that the rule evaluates to save costs and ["labels" on web requests](https://docs.aws.amazon.com/waf/latest/developerguide/waf-labels.html) to allow a rule that matches the request to communicate the match results to rules that are evaluated later in the same web ACL. Choose this option to reuse the same logic across multiple rules.

 You can also define a complete custom response, with response code, headers, and body.

 To help identify malicious requests, review your web server logs or use AWS WAF’s logging and request sampling.By enabling AWS WAF logging, you get detailed information about the traffic analyzed by the Web ACL. AWS WAF supports log filtering, allowing you to specify which web requests are logged and which requests are discarded from the log after the inspection.

 Information recorded in the logs includes the time that AWS WAF received the request from your AWS resource, detailed information about the request, and the matching action for each rule requested.

 Sampled requests provide details about requests within the past three hours that matched one of your AWS WAF rules. You can use this information to identify potentially malicious traffic signatures and create a new rule to deny those requests. If you see a number of requests with a random query string, make sure to allow only the query string parameters that are relevant to cache for your application. This technique is helpful in mitigating a cache busting attack against your origin.
