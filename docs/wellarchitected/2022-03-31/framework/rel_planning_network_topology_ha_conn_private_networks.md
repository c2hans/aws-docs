---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_planning_network_topology_ha_conn_private_networks.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-premises environments
<a name="rel_planning_network_topology_ha_conn_private_networks"></a>

 Use multiple AWS Direct Connect connections or VPN tunnels between separately deployed private networks. Use multiple Direct Connect locations for high availability. If using multiple AWS Regions, ensure redundancy in at least two of them. You might want to evaluate AWS Marketplace appliances that terminate VPNs. If you use AWS Marketplace appliances, deploy redundant instances for high availability in different Availability Zones.

 AWS Direct Connect is a cloud service that makes it easy to establish a dedicated network connection from your on-premises environment to AWS. Using Direct Connect Gateway, your on-premises data center can be connected to multiple AWS VPCs spread across multiple AWS Regions.

 This redundancy addresses possible failures that impact connectivity resiliency:
+  How are you going to be resilient to failures in your topology?
+  What happens if you misconfigure something and remove connectivity?
+  Will you be able to handle an unexpected increase in traffic or use of your services?
+  Will you be able to absorb an attempted Distributed Denial of Service (DDoS) attack?

 When connecting your VPC to your on-premises data center via VPN, you should consider the resiliency and bandwidth requirements that you need when you select the vendor and instance size on which you need to run the appliance. If you use a VPN appliance that is not resilient in its implementation, then you should have a redundant connection through a second appliance. For all these scenarios, you need to define an acceptable time to recovery and test to ensure that you can meet those requirements.

 If you choose to connect your VPC to your data center using a Direct Connect connection and you need this connection to be highly available, have redundant Direct Connect connections from each data center. The redundant connection should use a second Direct Connect connection from different location than the first. If you have multiple data centers, ensure that the connections terminate at different locations. Use the [Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) to help you set this up.

 If you choose to fail over to VPN over the internet using Site-to-Site VPN, it’s important to understand that it supports up to 1.25-Gbps throughput per VPN tunnel, but does not support Equal Cost Multi Path (ECMP) for outbound traffic in the case of multiple AWS Managed VPN tunnels terminating on the same VGW. We do not recommend that you use AWS Managed VPN as a backup for Direct Connect connections unless you can tolerate speeds less than 1 Gbps during failover.

 You can also use VPC endpoints to privately connect your VPC to supported AWS services and VPC endpoint services powered by AWS PrivateLink without traversing the public internet. Endpoints are virtual devices. They are horizontally scaled, redundant, and highly available VPC components. They allow communication between instances in your VPC and services without imposing availability risks or bandwidth constraints on your network traffic.

 **Common anti-patterns:**
+  Having only one connectivity provider between your on-site network and AWS.
+  Consuming the connectivity capabilities of your AWS Direct Connect connection, but only having one connection.
+  Having only one path for your VPN connectivity.

 **Benefits of establishing this best practice:** By implementing redundant connectivity between your cloud environment and you corporate or on-premises environment, you can ensure that the dependent services between the two environments can communicate reliably.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Ensure that you have highly available connectivity between AWS and on-premises environment. Use multiple AWS Direct Connect connections or VPN tunnels between separately deployed private networks. Use multiple Direct Connect locations for high availability. If using multiple AWS Regions, ensure redundancy in at least two of them. You might want to evaluate AWS Marketplace appliances that terminate VPNs. If you use AWS Marketplace appliances, deploy redundant instances for high availability in different Availability Zones.
  +  Ensure that you have a redundant connection to your on-premises environment You may need redundant connections to multiple AWS Regions to achieve your availability needs.
    +  [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)
    +  [Using Redundant Site-to-Site VPN Connections to Provide Failover](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNConnections.html)
      +  Use service API operations to identify correct use of Direct Connect circuits.
        +  [DescribeConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnections.html)
        +  [DescribeConnectionsOnInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnectionsOnInterconnect.html)
        +  [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html)
        +  [DescribeDirectConnectGatewayAttachments](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAttachments.html)
        +  [DescribeDirectConnectGateways](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGateways.html)
        +  [DescribeHostedConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeHostedConnections.html)
        +  [DescribeInterconnects](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeInterconnects.html)
      +  If only one Direct Connect connection exists or you have none, set up redundant VPN tunnels to your virtual private gateways.
        +  [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
  +  Capture your current connectivity (for example, Direct Connect, virtual private gateways, AWS Marketplace appliances).
    +  Use service API operations to query configuration of Direct Connect connections.
      +  [DescribeConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnections.html)
      +  [DescribeConnectionsOnInterconnect](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnectionsOnInterconnect.html)
      +  [DescribeDirectConnectGatewayAssociations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html)
      +  [DescribeDirectConnectGatewayAttachments](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAttachments.htmll)
      +  [DescribeDirectConnectGateways](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGateways.html)
      +  [DescribeHostedConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeHostedConnections.html)
      +  [DescribeInterconnects](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeInterconnects.html)
    +  Use service API operations to collect virtual private gateways where route tables use them.
      +  [DescribeVpnGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html)
      +  [DescribeRouteTables](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html)
    +  Use service API operations to collect AWS Marketplace applications where route tables use them.
      +  [DescribeRouteTables](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help plan your networking](https://aws.amazon.com/partners/find/results/?keyword=network)
+  [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)
+  [AWS Marketplace for Network Infrastructure](https://aws.amazon.com/marketplace/b/2649366011)
+  [Amazon Virtual Private Cloud Connectivity Options Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html)
+  [Multiple data center HA network connectivity](https://aws.amazon.com/answers/networking/aws-multiple-data-center-ha-network-connectivity/)
+  [Using Redundant Site-to-Site VPN Connections to Provide Failover](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNConnections.html)
+  [Using the Direct Connect Resiliency Toolkit to get started](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resilency_toolkit.html)
+  [VPC Endpoints and VPC Endpoint Services (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html)
+  [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+  [What Is a Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
+  [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_VPN.html)
+  [Working with Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html)

 **Related videos:**
+  [AWS re:Invent 2018: Advanced VPC Design and New Capabilities for Amazon VPC (NET303)](https://youtu.be/fnxXNZdf6ew)
+  [AWS re:Invent 2019: AWS Transit Gateway reference architectures for many VPCs (NET406-R1)](https://youtu.be/9Nikqn_02Oc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
