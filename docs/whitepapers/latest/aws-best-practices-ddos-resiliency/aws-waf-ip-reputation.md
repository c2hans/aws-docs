---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-waf-ip-reputation.html
---

# AWS WAF – IP reputation rule groups
<a name="aws-waf-ip-reputation"></a>

 To help mitigate attacks based on IP address reputation, you can create rules that match IPs making HTTP requests to custom IPSets that you maintain or use [AWS WAF Managed IP Reputation rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html). From a DDoS perspective, the two most important rules are:
+ `AWSManagedIPDDoSList` rule within the `AWSManagedRulesAmazonIpReputationList` rule group
+ `AnonymousIPList` rule with the `AWSManagedRulesAmazonIpReputationList` rule group

**`AWSManagedIPDDoSList` rule within the `AWSManagedRulesAmazonIpReputationList` rule group:** The [Amazon IP reputation list rule-group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-amazon) AWSManagedRulesAmazonIpReputationList includes rules based on various Amazon internal threat intelligence teams. These rules look for IP addresses that are bots performing reconnaissance against AWS resources or actively engaging in DDoS activities against AWS resources. The AWSManagedIPDDoSList rule, which is in Count mode by default, is curated by the AWS perimeter protection team and contains IPs that have recently been observed participating in DDoS attacks against our customers. Surges in traffic matching this rule are a strong indicator of a DDoS attempt and AWS recommends adding the AWSManagedRulesAmazonIpReputationList rule group to your web ACL and take one of the following actions with regards to the AWSManagedIPDDoSList rule:
+  Move it into Block or Challenge mode
+  Leave it in Count mode and create a subsequent rate-based rule using a custom aggregation key using the WAF label namespace `awswaf:managed:aws:amazon-ip-list`, applied to requests matching this rule group

 Choosing between these two options depends on your application's traffic pattern and DDoS resilience requirements. Based on our observations across AWS customers, web properties typically fall into two distinct categories: those that regularly receive a low, consistent volume of traffic matching the AWSManagedIPDDoSList rule during normal operations, and those that only see matches during active DDoS attacks. Understanding your application's baseline behavior is crucial for determining the most effective protection strategy.

 If your application can handle small volumes of potentially malicious traffic without performance impact, you might opt for the rate-based approach. However, if your application is sensitive to any level of malicious traffic or you observe clear separation between legitimate and attack traffic patterns, implementing an immediate block action might be more appropriate.

**Note**
 Even when the AWSManagedRulesAmazonIpReputationList rule group is in Block mode within the web ACL, the AWSManagedIPDDoSList rule will be in Count unless the rule group has been edited to move the rule to Block.

 To determine your resources baseline, add the rule group to your web ACL and use CloudWatch AWS WAFv2 CountedRequests metrics (using the Sum statistic) for the AWSManagedRulesAmazonIpReputationList, rule group, to identify if your web application receives traffic from this rule group during non-attack periods. You might want to use WAF logs to pivot to the specific IPs that matched rules within the rule group, to see if their behavior in terms of the requests that they made, was in keeping with what legitimate user behavior looks like. Then you can make an informed decision to Block or Challenge actions or create a rate-based rule.

 If you choose to use a rate-based rule rather than block this traffic (most customers choose to block this outright) it would look like the following configuration pseudo-code:

```
rule name: rbr_ipddoslist
rule type: rate-based
limit: <a low number>
evaluation window: 300
aggregation key (custom): label namespace 'awswaf:managed:aws:amazon-ip-list:'
scope-down: if label matches 'awswaf:managed:aws:amazon-ip-list:AWSManagedIPDDoSList'
action: BLOCK
```

**`AnonymousIPList` rule with the `AWSManagedRulesAmazonIpReputationList` rule group:** The [Anonymous IP list rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html#aws-managed-rule-groups-ip-rep-anonymous) contains rules to block requests from services that allow the obfuscation of viewer identity. These include requests from VPNs, proxies, Tor nodes, and cloud platforms (excluding AWS). Requests from clients matching the AnonymousIPList rule are potential candidates for being used for malicious purposes like DDoS, and you should consider moving this rule to Block, but be careful of the HostingProviderIPListinBlock—it's a very blunt instrument and customers frequently choose to leave this rule in Count mode.

 In addition, you can use third-party IP reputation lists by using the [IP Lists parser](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/component-details.html#ip-lists-parser) component of the [Security Automations for AWS WAF](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/component-details.html) solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
