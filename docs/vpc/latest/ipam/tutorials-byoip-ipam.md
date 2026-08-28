---
source_url: https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam.html
---

# Tutorial: Bring your IP addresses to IPAM
<a name="tutorials-byoip-ipam"></a>

The tutorials in this section walk you through the process of bringing public IP address space to AWS and managing the space with IPAM.

Managing public IP address space with IPAM has the following benefits:
+ **Improves public IP addresses utilization across your organization**: You can use IPAM to share IP address space across AWS accounts. Without using IPAM, you cannot share your public IP space across AWS Organizations accounts.
+ **Simplifies the process of bringing public IP space to AWS**: You can use IPAM to onboard public IP address space once, and then use IPAM to distribute your public IPs across Regions to resources like EC2 instances and [application load balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-ip-pools.html). Without IPAM, you have to onboard your public IPs for each AWS Region.

**Note**
To monitor RPKI validity, detect route overlaps, and automate ROA management for your BYOIP prefixes, see [Monitor BGP route protection](monitor-bgp-route-security.md) and [Tutorial: Set up delegated RPKI for BYOIP prefixes](tutorials-byoip-bgp-security.md).

**Topics**
+ [Verify domain control](tutorials-byoip-ipam-domain-verification-methods.md)
+ [Bring your own IP to IPAM using both the AWS Management Console and the AWS CLI](tutorials-byoip-ipam-console-intro.md)
+ [Bring your own IP CIDR to IPAM using only the AWS CLI](tutorials-byoip-ipam-cli-only-intro.md)
+ [Bring your own IP to CloudFront using IPAM (supports IPv4 and IPv6)](tutorials-byoip-cloudfront.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
