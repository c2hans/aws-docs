---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html
---

# Amazon VPC-to-Amazon VPC connectivity options
<a name="amazon-vpc-to-amazon-vpc-connectivity-options"></a>

 Use these design patterns when you want to integrate multiple Amazon VPCs into a larger virtual network. This is useful if you require multiple VPCs due to security, billing, presence in multiple regions, or internal charge-back requirements, to more easily integrate AWS resources between Amazon VPCs. You can also combine these patterns with the Network–to–Amazon VPC connectivity options for creating a corporate network that spans remote networks and multiple VPCs.

 VPC connectivity between VPCs is best achieved when using non-overlapping IP ranges for each VPC being connected. For example, if you’d like to connect multiple VPCs, make sure each VPC is configured with unique Classless Inter-Domain Routing (CIDR) ranges. Therefore, we advise you to allocate a single, contiguous, non-overlapping CIDR block to be used by each VPC. For additional information about Amazon VPC routing and constraints, see the Amazon VPC Frequently Asked Questions.

|  Option  |  Use Case  |  Advantages  |  Limitations  |
| --- | --- | --- | --- |
|  [VPC peering](vpc-peering.md) |  AWS-provided network connectivity between two VPCs.  |  Leverages AWS managed scalable networking infrastructure  |  VPC peering does not support transitive peering relationships <br /> Difficult to manage at scale  |
| [AWS Transit Gateway](aws-transit-gateway.md) |  AWS-provided regional router connectivity for VPCs  |  AWS managed high availability and scalability service <br /> Regional network hub for up to 5,000 attachments  | Transit Gateway peering only supports static routes |
|  [AWS PrivateLink](aws-privatelink.md)  |  AWS-provided network connectivity between two VPCs using interface endpoints  |  Leverages AWS managed scalable networking infrastructure  |  VPC Endpoint services only available in the AWS region in which they are created  |
| [Software VPN](software-vpn-1.md) |  Software appliance- based VPN connections between VPCs  |  Supports a wide array of VPN vendors, products, and protocols <br /> Managed entirely by you  |  You are responsible for implementing HA solutions for all VPN endpoints (if required) <br /> VPN instances could become a network bottleneck  |
|  [Software VPN-to-AWS Site-to-Site VPN](software-vpn-to-aws-site-to-site-vpn.md)  |  Software appliance to VPN connection between VPCs  |  AWS managed high availability VPC VPN connection <br /> Supports a wide array of VPN vendors and products managed by you <br /> Supports static routes and dynamic BGP peering and routing policies  |  You are responsible for implementing HA solutions for the software appliance VPN endpoints (if required) <br /> VPN instances could become a network bottleneck <br /> IPsec VPN protocol only to AWS Managed VPN  |
