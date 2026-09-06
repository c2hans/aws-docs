---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/amazon-vpc-connectivity-options-for-ipv6.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon VPC connectivity options for IPv6
<a name="amazon-vpc-connectivity-options-for-ipv6"></a>

 There are a growing number of ways in which Amazon VPCs can connect to each other. Many of these options are detailed in the [VPC to VPC connectivity](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.html) section of the [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) whitepaper. AWS recommends you read the following subsections alongside, and it follows the same structure while providing additional insight regarding IPv6 operation as both papers cover:
+  VPC peering
+  AWS Transit Gateway
+  VPC subnet sharing
+  AWS PrivateLink

## VPC peering
<a name="vpc-peering"></a>

 VPC peering is the simplest method for VPC-to-VPC connectivity. It supports both intra- and inter-Region connectivity. The peering itself is IP protocol agnostic. After you establish peering, you must configure one or more static routes defining which prefixes are reachable. Both IPv4 and IPv6 prefixes may be routed across the same peering.

 The following diagram depicts a VPC peering between two VPCs supporting IPv4 and IPv6 simultaneously. The peering is agnostic, and the subnet route tables are the deciding factor for which prefixes are reachable.

![This is a diagram that shows dual-stack IPv6 VPC peering.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/dual-stack-ipv6-vpc-peering.png)

 With VPC peering, you can choose to route only the IPv6 CIDRs of your peered VPCs, thus ensuring IPv6-only connectivity. Also, you cannot peer two VPCs together if their IPv4 CIDRs are overlapping and their IPv6 CIDRs don’t overlap. For this use case, you can use the AWS Transit Gateway.

## AWS Transit Gateway
<a name="aws-transit-gateway"></a>

 [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) is a scalable highly available way to establish network connectivity between multiple VPCs. A Transit Gateway is a Regional construct, and attaches VPCs within the same Region. Transit Gateways located in different AWS Regions can establish a peering relationship, enabling global connectivity for your network.

## IPv6 connectivity with Transit Gateway
<a name="ipv6-connectivity-with-transit-gateway"></a>

 You use a Transit Gateway attachment to connect a VPC to a Transit Gateway. An attachment deploys an elastic network interface into each subnet you select. Traffic is routed into Transit Gateways using static routes in VPC subnet routing tables with the attachment as the next-hop. The attachments themselves are IP protocol agnostic, and you can route IPv4 and IPv6 prefixes via the same attachment. To support IPv6, the elastic network interfaces used by the attachments need to have IPv6 addresses assigned to them.

**Note**
If you retrofit IPv6 into an existing VPC with a Transit Gateway attachment, its elastic network interfaces won’t be auto-assigned IPv6 addresses; you need to explicitly configure assignment for the elastic network interfaces. If you don’t, IPv6 traffic cannot use the attachment.

**Note**
You cannot create a transit gateway attachment using IPv6-only subnets.

![This is a diagram that shows dual-stack AWS Transit Gateway routing.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/dual-stack-aws-transit-gateway-routing.png)

## IPv6 traffic within and between Transit Gateways
<a name="ipv6-traffic-within-and-between-transit-gateways"></a>

 A Transit Gateway attachment is both a source and a destination of packets. You can attach the following resources to your Transit Gateway:
+  VPCs
+  One or more VPN connections
+  One or more AWS Direct Connect gateways
+  One or more Transit Gateway Connect attachments
+  One or more Transit Gateway peering connections

 A Transit Gateway has one or more routing tables. A routing table can receive its entries through a combination of static route configuration and dynamic propagations from other attachments (VPC, Direct Connect, Site-to-Site VPN, or Connect Peering). In either case, IPv6 routes are supported.

### AWS Transit Gateway Connect attachments for IPv6
<a name="aws-transit-gateway-connect-attachments-for-ipv6"></a>

 You can create a *Transit Gateway Connect attachment* to establish a connection and dynamic routing between a transit gateway and third-party virtual appliances (such as SD-WAN appliances).

 These attachments take the form of IP Generic Routing Encapsulation (GRE) protocol tunnels and enable dynamic exchange of routing information between an EC2 instances in a VPC and a TGW. Route exchange is facilitated by a Border Gateway Protocol (BGP) peering. TGW connect peers support IPv6 using Multi-Protocol BGP (MP-BGP) and a `/125` CIDR block from the well-known `fd00::/8` unique local address range.

 Multiprotocol BGP (MP-BGP) is an extension to BGP that enables BGP to carry routing information for multiple network layers and address families. MP-BGP can carry the unicast routes used for multicast routing separately from the routes used for unicast IP forwarding.

![This is a diagram that shows AWS Transit Gateway Connect dual-stack IPV6 routing.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/aws-transit-gateway-connect-dual-stack-ipv6-routing.png)

## AWS PrivateLink
<a name="aws-privatelink"></a>

 [AWS PrivateLink](https://aws.amazon.com/privatelink/) provides private connectivity between VPCs, AWS services, and customer on-premises networks, without exposing traffic to the public internet. AWS PrivateLink makes it easy to connect services across different accounts and VPCs to significantly simplify your network architecture.

![This is a diagram that shows AWS PrivateLink in a dual-stack scenario.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/aws-privatelink-in-a-dual-stack-scenario.png)

## VPC sharing
<a name="vpc-sharing"></a>

 VPC sharing allows VPC owners to share a subnet across AWS accounts. You may share dual-stack subnets the same way as IPv4-only ones. IPv6 resources deployed into a shared subnet function identical to those deployed into non-shared subnets.
