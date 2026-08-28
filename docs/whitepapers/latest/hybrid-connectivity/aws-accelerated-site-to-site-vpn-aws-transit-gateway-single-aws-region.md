---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/aws-accelerated-site-to-site-vpn-aws-transit-gateway-single-aws-region.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Accelerated Site-to-Site VPN – AWS Transit Gateway, Single AWS Region
<a name="aws-accelerated-site-to-site-vpn-aws-transit-gateway-single-aws-region"></a>

 **This model is constructed of:**
+  Single AWS Region.
+  AWS Managed Site-to-Site VPN connection with AWS Transit Gateway.
+  Accelerated VPN enabled.

![Diagram showing AWS Managed VPN – AWS Transit Gateway, Single AWS Region](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/managed-vpn-tg-single-region.png)

 **Connectivity model attributes:**
+  Provide the ability to establish optimized VPN connections over the public internet by using [AWS Accelerated Site-to-Site VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html).
+  Provide the ability to achieve higher VPN connection bandwidth by configuring multiple VPN tunnels with ECMP.
+  Can be used for connection from multiple of remote sites.
+  Offers automated failover with dynamic routing (BGP).
+  With AWS Transit Gateway connected to VPCs, all the connected VPCs can use the same VPN connections. You can also control the desired communication model among the VPCs, for more information refer to [How Transit Gateways Work](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html).
+  Offers flexible design options to integrate third-party security and SD-WAN virtual appliances with AWS Transit Gateway. See [Centralized network security for VPC-to-VPC and on-premises to VPC traffic](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-network-security-for-vpc-to-vpc-and-on-premises-to-vpc-traffic.html).

 **Scale considerations:**
+  Up 50 Gbps of bandwidth with multiple IPsec tunnels and ECMP configured (each traffic flow will be limited to the maximum bandwidth per VPN tunnel).
+  [Thousands](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-quotas.html) of VPCs can be connected per AWS Transit Gateway.
+  Refer to the [Site-to-Site VPN quotas](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-limits.html) for other scale limits, such as number of routes.

 **Other considerations:**
+  The additional AWS Transit Gateway processing costs for data transfer between the on-premises data center and AWS.
+  Security groups of a remote VPC cannot be referenced in AWS Transit Gateway – this is supported by VPC peering, however.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
