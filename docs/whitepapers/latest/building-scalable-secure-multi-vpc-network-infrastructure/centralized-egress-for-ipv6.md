---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-for-ipv6.html
---

# Centralized egress for IPv6
<a name="centralized-egress-for-ipv6"></a>

 To support IPv6 egress in dual stack deployments that have centralized IPv4 egress, one of two patterns must be chosen:
+  Centralized IPv4 egress with decentralized IPv6 egress
+  Centralized IPv4 egress and centralized IPv6 egress

 In the first pattern, shown in the following diagram, egress-only internet gateways are deployed in each spoke VPC. Egress-only internet gateways are horizontally scaled, redundantly, and highly available gateways that allow outbound communication over IPv6 from instances inside your VPC. They prevent the internet from initiating IPv6 connections with your instances. Egress-only internet gateways have no charge. In this deployment model, IPv6 traffic flows out of the egress-only internet gateways in each VPC and IPv4 traffic flows over the centralized NAT Gateways deployed.

![A diagram depicting centralized IPV4 egress and decentralized outbound only IPv6 egress.](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/centralized-ipv4-egress-and-decentralized-outbound-ipv6.png)

 In the second pattern, shown in the following diagrams, egress IPv6 traffic from your instances is sent to a centralized VPC. This can be accomplished by using IPv6-to-IPv6 Network Prefix Translation (NPTv6) with NAT66 instances and NAT Gateways or by using Proxy Instances and Network Load Balancer. This pattern is applicable if centralized traffic inspection for outbound traffic is required and it cannot be performed in each spoke VPC.

![A diagram depicting centralized IPv6 egress using NAT gateways and NAT66 instances.](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/centralized-ipv6-egress-using-nat-gateways.png)

![A diagram depicting centralized IPv4 and IPv6 egress using proxy instances and Network Load Balancer.](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/centralized-ipv4-and-ipv6-egress.png)

 The [IPv6 on AWS whitepaper](https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/advanced-dual-stack-and-ipv6-only-network-designs.html) describes the centralized IPv6 egress patterns. The IPv6 egress patterns are discussed in more detail in the blog [Centralized outbound internet traffic for dual stack IPv4 and IPv6 VPCs](https://aws.amazon.com/blogs/networking-and-content-delivery/centralizing-outbound-internet-traffic-for-dual-stack-ipv4-and-ipv6-vpcs/), along with special considerations, sample solutions, and diagrams.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
