---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-to-internet.html
---

# Centralized egress to internet
<a name="centralized-egress-to-internet"></a>

As you deploy applications in your multi-account environment, many apps will require outbound-only internet access (for example, downloading libraries, patches, or OS updates). This can be achieved for both IPv4 and IPv6 traffic. For IPv4, this can achieved through network address translation (NAT) in the form of a NAT gateway (recommended), or alternatively, a self-managed NAT instance running on an Amazon EC2 instance, as a means for all egress internet access. Internal applications reside in private subnets, while NAT Gateways and Amazon EC2 NAT instances reside in a public subnet.

AWS recommends that you use NAT gateways because they provide better availability and bandwidth and require less eﬀort on your part to administer. For more information, refer to [Compare NAT gateways and NAT instances](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html).

For IPv6 traffic, egress traffic can be configured to leave each VPC through an egress only internet gateway in a decentralized manner or it can be configured to be sent to a centralized VPC using NAT instances or proxy instances. The IPv6 patterns are discussed in [Centralized egress for IPv6](centralized-egress-for-ipv6.md).

**Topics**
+ [Using the NAT gateway for centralized IPv4 egress](using-nat-gateway-for-centralized-egress.md)
+ [Using the NAT gateway with AWS Network Firewall for centralized IPv4 egress](using-nat-gateway-with-firewall.md)
+ [Using the NAT gateway and Gateway Load Balancer with Amazon EC2 instances for centralized IPv4 egress](using-nat-gateway-and-gwlb-with-ec2.md)
+ [Centralized egress for IPv6](centralized-egress-for-ipv6.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
