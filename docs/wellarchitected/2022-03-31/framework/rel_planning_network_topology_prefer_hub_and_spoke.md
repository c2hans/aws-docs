---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_planning_network_topology_prefer_hub_and_spoke.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL02-BP04 Prefer hub-and-spoke topologies over many-to-many mesh
<a name="rel_planning_network_topology_prefer_hub_and_spoke"></a>

 If more than two network address spaces (for example, VPCs and on-premises networks) are connected via VPC peering, AWS Direct Connect, or VPN, then use a hub-and-spoke model, like that provided by AWS Transit Gateway.

 If you have only two such networks, you can simply connect them to each other, but as the number of networks grows, the complexity of such meshed connections becomes untenable. AWS Transit Gateway provides an easy to maintain hub-and-spoke model, allowing the routing of traffic across your multiple networks.

![Diagram showing not using AWS Transit Gateway](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/without-transit-gateway.png)

![Diagram showing using AWS Transit Gateway](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/with-transit-gateway.png)

 **Common anti-patterns:**
+  Using VPC peering to connect more than two VPCs.
+  Establishing multiple BGP sessions for each VPC to establish connectivity that spans Virtual Private Clouds (VPCs) spread across multiple AWS Regions.

 **Benefits of establishing this best practice:** As the number of networks grows, the complexity of such meshed connections becomes untenable. AWS Transit Gateway provides an easy to maintain hub-and-spoke model, allowing routing of traffic among your multiple networks.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Prefer hub-and-spoke topologies over many-to-many mesh. If more than two network address spaces (VPCs, on-premises networks) are connected via VPC peering, AWS Direct Connect, or VPN, then use a hub-and-spoke model like that provided by AWS Transit Gateway.
  +  For only two such networks, you can simply connect them to each other, but as the number of networks grows, the complexity of such meshed connections becomes untenable. AWS Transit Gateway provides an easy to maintain hub-and-spoke model, allowing routing of traffic across your multiple networks.
    +  [What Is a Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help plan your networking](https://aws.amazon.com/partners/find/results/?keyword=network)
+  [AWS Marketplace for Network Infrastructure](https://aws.amazon.com/marketplace/b/2649366011)
+  [Multiple data center HA network connectivity](https://aws.amazon.com/answers/networking/aws-multiple-data-center-ha-network-connectivity/)
+  [VPC Endpoints and VPC Endpoint Services (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html)
+  [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+  [What Is a Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)

 **Related videos:**
+  [AWS re:Invent 2018: Advanced VPC Design and New Capabilities for Amazon VPC (NET303)](https://youtu.be/fnxXNZdf6ew)
+  [AWS re:Invent 2019: AWS Transit Gateway reference architectures for many VPCs (NET406-R1)](https://youtu.be/9Nikqn_02Oc)
