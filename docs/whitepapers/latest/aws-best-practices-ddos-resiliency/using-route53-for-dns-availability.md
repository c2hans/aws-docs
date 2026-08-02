---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/using-route53-for-dns-availability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using Route 53 for DNS availability
<a name="using-route53-for-dns-availability"></a>

 Amazon Route 53 is a highly available and scalable Domain Name System (DNS) service that can be used to direct traffic to your web application. It includes advanced features like Traffic Flow, Health Checks and Monitoring, Latency-Based Routing, and Geo DNS. These advanced features allow you to control how the service responds to DNS requests to improve the performance of your web application and to avoid site outages. It's the only AWS service that has a 100% data plane availability SLA.

 Amazon Route 53 uses techniques such as [shuffle sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/) and [anycast striping](https://aws.amazon.com/blogs/architecture/a-case-study-in-global-fault-isolation/), that can help users access your application even if the DNS service is targeted by a DDoS attack.

 With shuffle sharding, each name server in your delegation set corresponds to a unique set of edge locations and internet paths. This provides greater fault tolerance and minimizes overlap between customers. If one name server in the delegation set is unavailable, users can retry and receive a response from another name server at a different edge location.

 Anycast striping allows each DNS request to be served by the most optimal location, dispersing the network load and reducing DNS latency. This provides a faster response for users. Additionally, Amazon Route 53 can detect anomalies in the source and volume of DNS queries, and prioritize requests from users that are known to be reliable.

 For more information about using Amazon Route 53 to route users to your application, refer to [Getting Started with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html).
