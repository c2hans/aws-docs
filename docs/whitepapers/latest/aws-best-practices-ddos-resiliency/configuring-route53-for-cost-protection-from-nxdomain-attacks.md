---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/configuring-route53-for-cost-protection-from-nxdomain-attacks.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Configuring Route 53 for cost protection from `NXDOMAIN` attacks
<a name="configuring-route53-for-cost-protection-from-nxdomain-attacks"></a>

 `NXDOMAIN` attacks occur when attackers send a flood of requests to a hosted zone for non-existent sub-domains, often via known "good" resolvers. The purpose of these attacks may be to impact the cache of the recursive resolver and/or the availability of the authoritative resolver, or could be a form of DNS reconnaissance to try to discover hosted zone records. Using Route 53 for your authoritative resolver mitigates the risk of availability/performance impact, however the result can be a significant cost increase in monthly Route 53 costs. To protect against cost increases, take advantage of [Route 53 pricing](https://aws.amazon.com/route53/pricing/) in which DNS queries are free when both of the following are true:
+  The domain or subdomain name (`example.com` or `store.example.com`) and the record type (`A`) in the query match an alias record.
+  The alias target is an AWS resource other than another Route 53 record.

 Create a wildcard record, for example, `*.example.com` with a type `A` (Alias) pointing at an AWS resource such as an EC2 instance, Elastic Load Balancer or CloudFront distribution, so that when a query for `qwerty12345.example.com` is made, the IP of the resource will be returned and you will not be charged for the query.
