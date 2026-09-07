---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html
---

# AWS Direct Connect
<a name="aws-direct-connect"></a>

 [AWS Direct Connect](https://aws.amazon.com/directconnect/) makes it easy to establish a dedicated connection from an on-premises network to one or more VPCs. Direct Connect can reduce network costs, increase bandwidth throughput, and provide a more consistent network experience than internet-based connections. It uses industry-standard 802.1Q VLANs to connect to Amazon VPC using private IP addresses. The VLANs are configured using [virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html) (VIFs), and you can configure three different types of VIFs:
+  **Public virtual interface** - Establish connectivity between AWS public endpoints and your data center, office, or colocation environment.
+  **Transit virtual interface** - Establish private connectivity between AWS Transit Gateway and your data center, office, or colocation environment. This connectivity option is covered in the section [AWS Direct Connect \+ AWS Transit Gateway](aws-direct-connect-aws-transit-gateway.md).
+  **Private virtual interface** - Establish private connectivity between Amazon VPC resources and your data center, office, or colocation environment. The use of private VIFs is shown in the following figure.
![Diagram showing AWS Direct Connect.](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-direct-connect.png)

 You can establish connectivity to the AWS backbone using AWS Direct Connect by establishing a cross-connect to AWS devices in a [Direct Connect location](https://aws.amazon.com/directconnect/locations/). You can access any AWS Region from any of our Direct Connect locations (except China). If you don’t have equipment at a location, you can choose from an ecosystem of [WAN service providers](https://aws.amazon.com/directconnect/partners/) for integrating your AWS Direct Connect endpoint in an AWS Direct Connect location with your remote networks.

With AWS Direct Connect, you have two types of connection:
+  **Dedicated connections**, where a physical ethernet connection is associated with a single customer. You can order port speeds of 1, 10, or 100 Gbps. You might need to work with a partner in the AWS Direct Connect Partner Program to help you establish network circuits between an AWS Direct Connect connection and your data center, office, or colocation environment.
+  **Hosted connections**, where a physical ethernet connection is provisioned by an AWS Direct Connect Partner and shared with you. You can order port speeds between 50 Mbps and 10 Gbps. Your work with the Partner in both the Direct Connect connection they established and the network circuits between an AWS Direct Connect connection and your data center, office, or colocation environment.

 For dedicated connections, you can also use a link aggregation group (LAG) to aggregate multiple connections at a single AWS Direct Connect endpoint. You treat them as a single, managed connection. You can aggregate up to four 1- or 10-Gbps connections, and up to two 100-Gbps connections.

 When discussing high availability in AWS Direct Connect, we recommend using additional Direct Connect connections. The [Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) offers guidance in building highly resilient network connections between AWS and your data center, office, or colocation environment. The following figure shows you an example of a high-resiliency connectivity option, with two Direct Connect connections terminated in two different Direct Connect locations.

![A diagram example that shows a high-resiliency connectivity option.](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/redundant-aws-direct-connect.png)

 AWS Direct Connect is not encrypted by default. For dedicated connections of 10 or 100 Gbps, you can use MAC security (MACsec) as an encryption option. For connections of 1 Gbps or less, you can create VPN tunnels on top of the connection – this option is covered in [AWS Direct Connect \+ AWS Site-to-Site VPN](aws-direct-connect-site-to-site-vpn.md) and [AWS Direct Connect \+ AWS Transit Gateway \+ AWS Site-to-Site VPN](aws-direct-connect-aws-transit-gateway-vpn.md) sections.

 One important resource in AWS Direct Connect is the Direct Connect gateway, which is a globally available resource to enable connections to multiple Amazon VPCs or Transit Gateways across different Regions or AWS accounts. This resource also allows you to connect to any participating VPC or Transit Gateway from one private VIF or transit VIF, reducing AWS Direct Connect management, as shown in the following figure.

![Diagram that shows connecting to any participating VPC or Transit Gateway from one private VIF or transit VIF.](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/aws-direct-connect-gateway.png)

Regarding IP addressing, AWS Direct Connect virtual interfaces support both IPv4 and IPv6 BGP sessions for dual-stack operation.
+  Private and transit VIFs IPv4 configuration make use of either AWS-generated IPv4 addresses or addresses configured by you. For public VIFs IPv4 BGP peering, you must specify an unique public /31 IPv4 CIDR that you own (or submit a request to have a CIDR block assigned).
+  For all types of VIFs IPv6 BGP peering, AWS assigns a /125 CIDR, which is not configurable.

## Additional resources
<a name="additional-resources-2"></a>
+  [AWS Direct Connect User Guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
+  [AWS Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html)
+  [AWS Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html)
+  [AWS Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html)
+  [AWS Direct Connect MAC Security](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html)
+  [AWS Direct Connect locations](https://aws.amazon.com/directconnect/locations/)
+  [AWS Direct Connect Delivery Partners](https://aws.amazon.com/directconnect/partners/)
