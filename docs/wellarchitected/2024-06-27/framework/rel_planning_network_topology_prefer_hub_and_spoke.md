---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel_planning_network_topology_prefer_hub_and_spoke.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL02-BP04 Prefer hub-and-spoke topologies over many-to-many mesh
<a name="rel_planning_network_topology_prefer_hub_and_spoke"></a>

 When connecting multiple private networks, such as Virtual Private Clouds (VPCs) and on-premises networks, opt for a hub-and-spoke topology over a meshed one. Unlike meshed topologies, where each network connects directly to the others and increases the complexity and management overhead, the hub-and-spoke architecture centralizes connections through a single hub. This centralization simplifies the network structure and enhances its operability, scalability, and control.

 AWS Transit Gateway is a managed, scalable, and highly-available service designed for construction of hub-and-spoke networks on AWS. It serves as the central hub of your network that provides network segmentation, centralized routing, and the simplified connection to both cloud and on-premises environments. The following figure illustrates how you can use AWS Transit Gateway to build your hub-and-spoke topology.

![Hub-and-spoke network topology with AWS Transit Gateway connecting VPN, Direct Connect , and VPCs.](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/images/hub-and-spoke.png)

 **Common anti-patterns:**
+  You overcomplicate routing policies in a hub-and-spoke architecture, which reduces reduce network efficiency and complicates both troubleshooting and proactive management.
+  Insufficient routing-based segmentation within the hub could lead to vulnerabilities, which potentially exposes the network to unauthorized access.
+  Without careful optimization, traffic routed through the hub can lead to higher data transfer costs, particularly for traffic crossing Availability Zones and Regions. Effective traffic management strategies are essential to control expenses.

 **Benefits of establishing this best practice:** As the number of connected networks increases, management and expansion of meshed connectivity becomes increasingly challenging. AWS Transit Gateway offers a scalable and reliable managed hub for construction and operation of your hub-and-spoke topologies. When you use AWS Transit Gateway, you can establish connections and centralizes traffic routing across multiple networks.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Plan your network.
+  Create your AWS Transit Gateway.
+  Attach your VPCs.
+  If needed, create VPN connections or Direct Connect gateways and associate them with the Transit Gateway.
+  Define how traffic is routed between the connected VPCs and other connections through configuration of your Transit Gateway route tables.
+  Use Amazon CloudWatch to monitor and adjust configurations as necessary for performance and cost optimization.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [What Is a Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
+  [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html)
+  [Building a global network using AWS Transit Gateway Inter-Region peering](https://aws.amazon.com/blogs/networking-and-content-delivery/building-a-global-network-using-aws-transit-gateway-inter-region-peering/)
+  [Amazon Virtual Private Cloud Connectivity Options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html)
+  [APN Partner: partners that can help plan your networking](https://aws.amazon.com/partners/find/results/?keyword=network)
+  [AWS Marketplace for Network Infrastructure](https://aws.amazon.com/marketplace/b/2649366011)

 **Related videos:**
+  [AWS re:Invent 2023 - AWS networking foundations](https://www.youtube.com/watch?v=8nNurTFy-h4)
+  [AWS re:Invent 2023 - Advanced VPC designs and new capabilities](https://www.youtube.com/watch?v=cRdDCkbE4es)
