---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/networking.html
---

# Networking integration
<a name="networking"></a>

Most enterprises  require connectivity between accounts in their AWS Control Tower–managed environment. This often extends to connecting corporate offices and on-premises data centers. AWS Virtual Private Network (Site-to-Site VPN) and AWS Direct Connect are used as network paths to provide that hybrid connectivity for workloads.
+ [Site-to-Site VPN](https://aws.amazon.com/vpn/)** **establishes a secure and private tunnel from your network or device to the AWS Cloud over the internet. It allows you to securely connect your on-premises network or branch office site to your VPC.
+ [AWS Direct Connect](https://aws.amazon.com/directconnect/) makes it easy to establish a dedicated network connection from your on-premises environment to AWS. It provides a more consistent network experience than internet-based connections.
+ [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) connects VPCs and on-premises networks through a central hub and enables various routing scenarios. It controls how traffic is routed among the connected networks.

The easiest way to get started with hybrid connectivity is to establish site-to-site VPN over the internet. This extends your data center or branch office to the cloud by using IPsec tunnels. You can configure routing by using Border Gateway Protocol (BGP) or configure static routes. Each AWS Site-to-Site VPN connection consists of two VPN tunnel endpoints for redundancy. Each tunnel terminates in a different Availability Zone within the AWS global network, for high availability.

AWS Site-to-Site VPN supports terminating IPsec tunnels on both virtual private gateways and AWS Transit Gateway at the AWS end. When you terminate a VPN on a virtual private gateway, you can access the VPC that the gateway is attached to. However, if you use Transit Gateway, you gain connectivity to thousands of VPCs over a pair of VPN tunnels. Additionally, Transit Gateway supports equal-cost multipath (ECMP) routing, which enables you to load-balance traffic across multiple VPN tunnels for high availability and bandwidth aggregation.

In summary, terminating a VPN at a transit gateway is a default starting point for hybrid architectures, because it provides more flexibility in the number of VPCs you can connect to, and added functionality such as ECMP.

The following diagram shows how you can connect an on-premises environment to your VPCs on AWS by using AWS Site-to-Site VPN.

![Connecting on-premises environment to VPCs by using AWS Site-to-Site VPN.](http://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/images/guide-img/156d118c-ed00-4c5b-9a02-63c2673a3342/images/c49b8730-4480-447e-adb9-fade1078baf8.png)

For end-to-end network performance, you can use Direct Connect to enable consistent, low-latency, high-bandwidth, dedicated fiber connectivity between your on-premises data centers and AWS. Direct Connect provides dedicated connections at bandwidths of 1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps. Hosted connections provided by Direct Connect Partners use pre-established network links and are available from 50 Mbps up to 25 Gbps.

Direct Connect provides three types of virtual interfaces (VIFs):
+ Public VIFs** **provide global connectivity to public AWS resources, including AWS public service endpoints, public Amazon EC2 IP addresses, and public Elastic Load Balancing addresses.
+ Private VIFs** **provide connectivity to the private IP range of your VPC.
+ Transit VIFs enable connectivity to transit gateways.

The following sections provide examples of these connectivity options.
