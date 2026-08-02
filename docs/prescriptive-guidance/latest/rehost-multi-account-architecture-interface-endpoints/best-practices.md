---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-multi-account-architecture-interface-endpoints/best-practices.html
---

# Best practices
<a name="best-practices"></a>
+ Avoid single points of failure. For VPC endpoints and Route 53 Resolver endpoints, use two or more Availability Zones for high availability.
+ Do not use Route 53 Resolver endpoints to forward DNS queries between VPCs. We strongly recommend that you use the Amazon DNS Server (.2 resolver) as the DNS resolver for all instances inside Amazon EC2. This resolver provides the highest level of availability and scalability with the lowest latency.
+ For additional best practices, see [Best practices for Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html) in the Route 53 documentation.
