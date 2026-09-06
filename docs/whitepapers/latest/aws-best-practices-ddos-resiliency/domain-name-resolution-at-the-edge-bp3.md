---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/domain-name-resolution-at-the-edge-bp3.html
---

# Domain name resolution at the edge (BP3)
<a name="domain-name-resolution-at-the-edge-bp3"></a>

## Using Route 53 for DNS availability
<a name="using-route53-for-dns-availability"></a>

 Amazon Route 53 is a highly available and scalable DNS service that you can use to direct traffic to your web application. It includes advanced features like [Traffic Flow](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html), [Health Checks and Monitoring](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html), [Latency-Based Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html), and [Geo DNS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html). You can use these advanced features to control how the service responds to DNS requests to improve the performance of your web application and to avoid site outages. It's the only AWS service that has a 100% data plane availability SLA.

 Amazon Route 53 uses techniques such as [shuffle sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/) and [anycast striping](https://aws.amazon.com/blogs/architecture/a-case-study-in-global-fault-isolation/), that can help users access your application even if the DNS service is targeted by a DDoS attack.

 With shuffle sharding, each name server in your delegation set corresponds to a unique set of edge locations and internet paths. This provides greater fault tolerance and minimizes overlap between customers. If one name server in the delegation set is unavailable, users can retry and receive a response from another name server at a different edge location.

 Anycast striping allows each DNS request to be served by the most optimal location, dispersing the network load and reducing DNS latency. This provides a faster response for users. Additionally, Amazon Route 53 can detect anomalies in the source and volume of DNS queries and prioritize requests from users that are known to be reliable.

 For more information about using Amazon Route 53 to route users to your application, see [Getting Started with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html).

## Configuring Route 53 for cost protection from `NXDOMAIN` attacks
<a name="configuring-route53-for-cost-protection-from-nxdomain-attacks"></a>

 `NXDOMAIN` attacks occur when attackers send a flood of requests to a hosted zone for non-existent sub-domains, often using known legitimate resolvers. The purpose of these attacks might be to impact the cache of the recursive resolver or the availability of the authoritative resolver, or could be a form of DNS reconnaissance to try to discover hosted zone records. Using Route 53 for your authoritative resolver mitigates the risk of availability/performance impact, however the result can be an increase in the per-query cost of Route 53. To protect against cost increases, take advantage of [Route 53 pricing](https://aws.amazon.com/route53/pricing/) in which DNS queries are free when both of the following are true:
+  The domain (example.com) or subdomain name (store.example.com) and the record type (A) in the query match an alias record.
+  The alias target is an AWS resource other than another Route 53 record.

 Create a [wildcard record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html#domain-name-format-asterisk), for example, `*.example.com` with a type `A` (Alias) pointing at an AWS resource such as an Amazon S3 bucket or CloudFront distribution, so that when a query for `qwerty12345.example.com` is made, the IP of the resource will be returned and you will not be charged for the query.
