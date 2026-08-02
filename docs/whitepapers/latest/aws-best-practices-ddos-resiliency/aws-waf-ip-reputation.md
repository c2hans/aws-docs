---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf-ip-reputation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS WAF – IP reputation
<a name="aws-waf-ip-reputation"></a>

 To prevent attacks based on IP address reputation, you can create rules using IP matching or use [Managed Rules](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html) for AWS WAF.

 [Amazon's IP reputation list rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-amazon) includes rules based on Amazon's internal threat intelligence. These rules look for IP addresses that are bots, performing reconnaissance against AWS resources, or actively engaging in DDoS activities. The `AWSManagedIPDDoSList` rule, has been observed blocking over 90% of malicious request floods.

 The [Anonymous IP list rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-anonymous) contains rules to block requests from services that allow the obfuscation of viewer identity. These include requests from VPNs, proxies, Tor nodes, and cloud platforms (excluding AWS).

 In addition you can make use of third-party IP reputation lists by using the [IP Lists parser](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/component-details.html#ip-lists-parser) component of the [Security Automations for AWS WAF](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/component-details.html) solution.
