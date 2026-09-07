---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/architecture-2.html
---

# Architecture 2: VPC peering
<a name="architecture-2"></a>

You can use VPC peering to connect to a third-party account and enable direct interaction between applications and resources in your AWS account with application and services in the third-party account. [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) is a networking connection between two VPCs that allows you to route traffic between them by using private IPv4 addresses or IPv6 addresses. The VPCs do not need to be in the same AWS account or AWS Region. There is no gateway or other device; the VPCs communicate directly.

This architecture supports bidirectional traffic between the VPCs and supports all types of IP traffic. Traffic remains on the global AWS infrastructure and never travels over the public internet. This reduces the risk from external threats, such as common exploits and DDoS attacks. All inter-Region traffic is encrypted. This architecture is designed to prevent single points of failure and bandwidth bottlenecks.

The following architecture diagram shows how you can use VPC peering connections to connect VPCs in your account with a VPC in the third-party account.

![Creating VPC peering connections between VPCs in different AWS accounts](https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/images/guide-img/80f3a808-d645-486e-82c4-f574fdcf6710/images/d70ad29e-ce7f-4bf1-8fd0-a2ab6c7038e3.png)

VPC peering is subject to limitations, such as these connections do not support transitive peering relationships or overlapping CIDR blocks. In addition, there is a quota on the number of connections each VPC can have. For more information, see [VPC peering limitations](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-basics.html#vpc-peering-limitations).

Because the number of peering connections grows with the number of VPCs, this architecture is not recommended if scalability is one of your requirements.

## Cost considerations
<a name="cost-considerations-2"></a>
+ There is no charge to create a VPC peering connection.
+ There is a charge for data transfer across peering connections.

For more information, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/).
