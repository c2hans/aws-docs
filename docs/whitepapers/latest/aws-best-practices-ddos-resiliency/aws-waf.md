---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf.html
---

# AWS WAF
<a name="aws-waf"></a>

 By using AWS WAF, you can configure web access control lists (web ACLs) on your global CloudFront distributions or regional resources to filter, monitor and block requests based on request signatures. To determine whether to allow or block requests, you can consider factors such as the IP address or country of origin, certain strings or patterns in the request, the size of specific parts of the request, and the presence of malicious SQL code or scripting. You can also run [CAPTCHA puzzles and silent client session challenges](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-actions.html) against requests.

 Both AWS WAF and CloudFront also enable you to set [geo-restrictions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html) to block or allow requests from selected countries. This can help block or rate-limit attacks from geographic locations where you don't expect to serve users. With fine-grained geographic match rule statements in AWS WAF, you can control access down to the region level.

 You can use [Scope-down statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-scope-down-statements.html) to narrow the scope of the requests that the rule evaluates to save costs and [labels on web requests](https://docs.aws.amazon.com/waf/latest/developerguide/waf-labels.html) to allow a rule that matches the request to communicate the match results to rules that are evaluated later in the same web ACL. Choose this option to reuse the same logic across multiple rules.

 We recommend using a layered funnel approach when building your web ACL rule groups, with the goal of reducing the attack vectors early. Consider adding the following rules in the order listed. After testing and evaluating the results, you can change the order or add other rules as you see fit.

*Table 3 – Recommended WAF rules*

| WAF rule name | WAF rule type | Action | Priority |
| --- | --- | --- | --- |
| ALLOWed IPs (\*) | Custom (with [IP set](https://docs.aws.amazon.com/waf/latest/developerguide/waf-ip-set-managing.html)) | ALLOW | 1 |
| BLOCKed IPs (\*) | Custom (with IP set) | BLOCK | 2 |
| GEO-fencing (\*) | Custom (Country-codes) | BLOCK or ALLOW | 3 |
| [AntiDDoS AMR](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html) (\*\*) | Managed | BLOCK or COUNT | 4 |
| [AWSManagedRulesAmazonIpReputationList](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html) (\*) (AWSManagedIPDDoSList rule Count by Default) (\*) | Managed | BLOCK during DDoS event | 5 |
| RateLimit capture-all (higher level of allowed traffic) (\*) | Rate-Based rule | BLOCK, CAPTCHA, CHALLENGE | 6 |
| (multiple separate) RateLimits for specific types—such as API, URI, IP lists, J3 and J4, and so on—and lower limits for traffic type (\*) | Rate-Based rule | BLOCK, CAPTCHA, CHALLENGE | 7 |
| Core rule set (\*) | Managed | BLOCK, CAPTCHA, CHALLENGE | 8 |
| Bot control (common) (\*\*) | Managed | BLOCK, CAPTCHA, CHALLENGE | 9 |

 \* Basic AWS WAF pricing applies

 \*\* Available for additional fees (threat intelligence)

 You can also define a complete custom response, with response code, headers, and body.

 To help identify malicious requests, review your web server logs or use [AWS WAF logging](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) and request sampling. By enabling AWS WAF logging, you get detailed information about the traffic analyzed by the web ACL. AWS WAF supports log filtering, allowing you to specify which web requests are logged and which requests are discarded from the log after the inspection. [Information recorded in the logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) includes the time that AWS WAF received the request from your AWS resource, detailed information about the request, and the matching action for each rule requested.

 Sampled requests provide details about requests within the past three hours that matched one of your AWS WAF rules. You can use this information to identify potentially malicious traffic signatures and create a new rule to deny those requests. If you see several requests with a random query string, make sure to allow only the query string parameters that are relevant to cache for your application. This technique is helpful in mitigating a cache busting attack against your origin.
