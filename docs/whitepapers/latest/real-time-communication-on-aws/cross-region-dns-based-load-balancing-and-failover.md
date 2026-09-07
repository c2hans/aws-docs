---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/cross-region-dns-based-load-balancing-and-failover.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cross-Region DNS-based load balancing and failover
<a name="cross-region-dns-based-load-balancing-and-failover"></a>

 [Amazon Route 53](https://aws.amazon.com/route53/) provides a global DNS service that can be used as a public or private endpoint for RTC clients to register and connect with media applications. With Amazon Route 53, DNS health checks can be configured to route traffic to healthy endpoints or to independently monitor the health of your application.

The Amazon Route 53 Traffic Flow feature makes it easy for you to manage traffic globally through a variety of routing types, including latency-based routing, geo DNS, geoproximity, and weighted round robin—all of which can be combined with DNS Failover to enable a variety of low-latency, fault-tolerant architectures. The Amazon Route 53 Traffic Flow simple visual editor allows you to manage how your end users are routed to your application’s endpoints—whether in a single AWS Region or distributed around the globe.

 In the case of global deployments, the latency-based routing policy in Route 53 is especially useful to direct customers to the nearest point of presence for a media server to improve the quality of service associated with real-time media exchanges.

 Note that to enforce a failover to a new DNS address, client caches must be flushed. Also, DNS changes may have a lag as they are propagated across global DNS servers. You can manage the refresh interval for DNS lookups with the Time to Live attribute. This attribute is configurable at the time of setting up DNS policies.

 To reach global users quickly or to meet the requirements of using a single public IP, AWS Global Accelerator can also be used for cross-Region failover. [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/?blogs-global-accelerator.sort-by=item.additionalFields.createdDate&blogs-global-accelerator.sort-order=desc&aws-global-accelerator-wn.sort-by=item.additionalFields.postDateTime&aws-global-accelerator-wn.sort-order=desc) is a networking service that improves availability and performance for applications with both local and global reach. AWS Global Accelerator provides static IP addresses that act as a fixed entry point to your application endpoints, such as your Application Load Balancers, Network Load Balancers, or Amazon EC2 instances in single or multiple AWS Regions. It uses the AWS global network to optimize the path from your users to your applications, improving performance, such as the latency of your TCP and UDP traffic.

AWS Global Accelerator continually monitors the health of your application endpoints, and automatically redirects traffic to the nearest healthy endpoints in the event of current endpoints turning unhealthy. For additional security requirements, Accelerated Site-to-Site VPN uses AWS Global Accelerator to improve the performance of VPN connections by intelligently routing traffic through the AWS Global Network and AWS edge locations.

![A diagram depicting inter-Region high availability design using AWS Global Accelerator or Amazon Route 53.](https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/images/inter-region-ha-design.png)
