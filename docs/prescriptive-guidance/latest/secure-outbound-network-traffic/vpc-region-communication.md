---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-outbound-network-traffic/vpc-region-communication.html
---

# Communicating across VPCs and AWS Regions
<a name="vpc-region-communication"></a>

Multi-VPC infrastructures can help organizations segment their workloads and expand their footprints. This type of architecture can also create challenges when resources need to communicate with AWS services in different VPCs, AWS Regions, and AWS accounts.

To establish connectivity between two VPCs, you can use either [VPC peering](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.html) or [AWS Transit Gateway](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html). A VPC peering connection is a networking connection between two VPCs that routes traffic between them using private IPv4 or IPv6 addresses. AWS Transit Gateway connects VPCs to a single Transit Gateway instance, which consolidates an organization's entire AWS routing configuration in one place.

For more information, see the [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) AWS Whitepaper.

**Note**
To create and manage a multi-VPC AWS network infrastructure at scale, it's a best practice to use AWS Transit Gateway.

## Key considerations when choosing between VPC peering and AWS Transit Gateway
<a name="key-considerations-when-choosing-between-vpc-peering-and-aws-transit-gateway.05ff1a4a-bb8a-55fd-9c9b-acb63172bf78"></a>

**VPC peering**
+ Traffic between each VPC is managed individually between each VPC.
+ VPC peering doesn't support [transitive routing](https://docs.aws.amazon.com/vpc/latest/peering/invalid-peering-configurations.html#transitive-peering). A direct VPC peering connection is required between each VPC that must communicate with one another.

**AWS Transit Gateway**
+ Traffic between each VPC is managed through the AWS Transit Gateway service, which acts as a centralized hub that connects each VPC.
+ AWS Transit Gateway supports transitive routing. Traffic is routed among all the connected networks by using route tables.
