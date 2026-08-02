---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/options-onprem.html
---

# Service consumers operating on premises
<a name="options-onprem"></a>

This section discusses connectivity options between SaaS workloads in the AWS Cloud and the on-premises data centers. Many consumers with on-premises requirements, especially at the enterprise level, see the cloud as an extension of their physical network, and they want to reflect that in their architecture. That means private connectivity to the SaaS offering in the cloud, either through logical tunnels or even through a private physical connection. Other consumers will accept connectivity through the public internet, which is also discussed in this section.

**This section discusses the following network access approaches:**
+ [Connecting with AWS Site-to-Site VPN](#options-onprem-site-to-site)
+ [Connecting with AWS Direct Connect](#options-onprem-direct-connect)
+ [Connecting with a transit VPC architecture](#options-onprem-transit-vpc)
+ [Connecting through the public internet](#options-onprem-internet)

The following networking value map summarizes how each of these options scores for each evaluation metric. For more information about the evaluation metrics, see [Evaluation metrics](evaluating.md#evaluating-metrics) in this guide. In the map, a five represents the best score, such as the lowest TCO, best network isolation, or lowest time to repair. For more information about how to read this radar chart, see [Networking value map](evaluating.md#evaluating-map) in this guide.

**Note**
The provider-managed transit VPC option is excluded because the scores heavily depend on which services are being operated.

![Radar chart that shows scores for each evaluation metric.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/857f5319-acc8-4970-9056-ac9d301ca7d2.png)

The radar chart shows the following values.

|
|
| **Evaluation metric** | **AWS Site-to-Site VPN** | **AWS Direct Connect** | **Consumer-managed transit VPC** | **Public internet access** |
| --- |--- |--- |--- |--- |
| **Ease of integration** | 3 | 1 | 4 | 5 |
| **TCO** | 2 | 1 | 5 | 4 |
| **Scalability** | 3 | 1 | 5 | 5 |
| **Adaptability** | 3 | 2 | 4 | 5 |
| **Network isolation** | 3 | 4 | 5 | 1 |
| **Observability** | 3 | 4 | 5 | 5 |
| **Time to repair** | 3 | 2 | 5 | 5 |

## Connecting with AWS Site-to-Site VPN
<a name="options-onprem-site-to-site"></a>

[AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) connections can terminate on either a virtual private gateway or a transit gateway. A *virtual private gateway* is the VPN endpoint on the AWS side of your Site-to-Site VPN connection that can be attached to a single VPC. A *transit gateway* is a transit hub that can be used to interconnect multiple VPCs and on-premises networks. It can also be used as a VPN endpoint for the AWS side of the Site-to-Site VPN connection. This section discusses both options.

### Connection through a virtual private gateway
<a name="connection-through-a-virtual-private-gateway.e558894c-f3f1-5600-8c5e-92dee8e1b752"></a>

After you create a virtual private gateway, you attach it to the VPC that contains your SaaS offering. Then, you enable route propagation to propagate the VPN routes to the VPC route table. Those routes can be either static or BGP-advertised dynamic routes.

For high availability, an Site-to-Site VPN connection has two VPN tunnels that terminate in two Availability Zones on the AWS side. If one becomes unavailable, the second tunnel can take over. A single tunnel allows a maximum bandwidth of 1.25 Gbps. Because virtual private gateways do not support equal-cost multi-path routing (ECMP), you can use only one tunnel at a time.

To increase fault tolerance, you can set up a second VPN connection to a second physical customer gateway. After the connection is established, the consumer can reach resources in the SaaS provider's VPC.

The following diagram shows this architecture.

![Connections from on-premises data centers to the AWS Cloud through a virtual gateway.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/610e688a-6892-4599-92de-09ca072e08f2.png)

The following are the benefits of this approach:
+ Time to repair: Managed failover to secondary VPN tunnel
+ Observability: Integration for managed active monitoring by using [Network Synthetic Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html)
+ Ease of integration: Dynamic routing support through BGP
+ Adaptability: Compatibility with most on-premises networking equipment
+ Adaptability: IPv6 support
+ TCO: AWS Site-to-Site VPN is a fully managed service, so it requires less operational effort
+ TCO: No cost for virtual gateways, although there are charges for the two public IPv4 addresses on each
+ Network isolation: Enables secure private communication through the internet

The following are the drawbacks of this approach:
+ Ease of integration: The consumer must configure their customer gateway
+ Scalability: Lack of ECMP support limits bandwidth to 1.25 Gbps per virtual gateway
+ Scalability: Limited scaling due to increased network complexity and operational overhead
+ Adaptability: [IPv6 support](https://docs.aws.amazon.com/vpn/latest/s2svpn/ipv4-ipv6.html) only for the inside IP addresses of the VPN tunnels
+ Adaptability: No transitive routing
+ TCO: Operational overhead to maintain, manage, and configure numerous VPN connections for the SaaS provider

### Connection through a transit gateway
<a name="connection-through-a-transit-gateway.5f627363-fc78-5513-9ae7-99036f6813bc"></a>

Connections through transit gateways are similar to virtual gateways. However, there are a few differences to keep in mind.

First, routes for the VPN attachment can be automatically propagated within the transit gateway route table, but you must manually add the routes to the attached VPCs.

Compared to a virtual gateway, Transit Gateway supports ECMP. If the customer gateway supports ECMP, it can use both tunnels to achieve a total maximum throughput of 2.5 Gbps. You can establish multiple connections between the same on-premises network to the transit gateway. Using this approach, you can increase the maximum bandwidth by up to 2.5 Gbps per connection.

The following diagram shows this architecture.

![Connections from on-premises data centers to the AWS Cloud through transit gateways.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/8bd10258-88e8-4fe8-8e26-dc2af871be3d.png)

The following are the benefits of this approach:
+ Time to repair: Managed failover to secondary VPN tunnel
+ Observability: Integration for managed active monitoring by using [Network Synthetic Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html)
+ Ease of integration: Dynamic routing support through BGP
+ Scalability: ECMP support allows [scaling VPN throughput](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/) to satisfy large bandwidth requirements
+ Scalability: Large number of VPN connections supported by a single transit gateway (up to almost 5,000)
+ Scalability: One place to manage and monitor all the VPN connections
+ Adaptability: Compatibility with most on-premises networking equipment
+ Adaptability: IPv6 support
+ Adaptability: Inherit flexibility of AWS Transit Gateway
+ TCO: AWS Transit Gateway is a fully managed service, so it requires less operational effort
+ TCO: No cost for virtual gateways, although there are charges for the two public IPv4 addresses on each
+ Network isolation: Enables secure private communication through the internet

The following are the drawbacks of this approach:
+ Ease of integration: The consumer must configure their customer gateway
+ Scalability: Limited scaling due to increased network complexity and operational overhead
+ Adaptability: [IPv6 support](https://docs.aws.amazon.com/vpn/latest/s2svpn/ipv4-ipv6.html) only for the inside IP addresses of the VPN tunnels
+ TCO: Operational overhead to maintain, manage, and configure numerous VPN connections for the SaaS provider
+ TCO: Extra charges for use of AWS Transit Gateway
+ TCO: Additional complexity managing the transit gateway route tables

## Connecting with AWS Direct Connect
<a name="options-onprem-direct-connect"></a>

[AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. Unlike the other architecture options, a [dedicated connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dedicated_connection.html) cannot be established in a few minutes. Instead, this process can take up to several days if all requirements are met. If not, it might take longer. Therefore, we suggest that you reach out to your AWS account team or AWS Support for help with this approach. Optionally, you can choose a [hosted connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/hosted_connection.html) that is provided by an AWS Partner and shared with other customers. The architecture is the same regardless. You might choose Direct Connect because it reduces latency, improves bandwidth, or complies with regulatory requirements.

To use the Direct Connect connection, consumers must create either a public, private, or transit virtual interface. There are different [architecture options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) available. The most flexible one to connect multiple on-premises locations to the AWS Cloud is a transit virtual interface connected to an [Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html). An Direct Connect gateway is a global, logical component that allows the service provider to connect up to six transit gateways to it. Furthermore, you can connect up to 30 virtual interfaces to the gateway. For scale, you can create additional Direct Connect gateways. In the SaaS provider account, the transit gateways then attach to the VPCs, as described previously.

Consumers can connect using one to four Direct Connect connections from a total of one or two [Direct Connect locations](https://aws.amazon.com/directconnect/locations/), depending on the desired level of resiliency. For more information, see [Configure Direct Connect for maximum resiliency](https://docs.aws.amazon.com/directconnect/latest/UserGuide/max-resiliency-set-up.html). An AWS Site-to-Site VPN connection over the internet might also serve as a lower-cost backup path for an Direct Connect connection. Supported Direct Connect dedicated connections can use [MACsec](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html) to encrypt the link on Layer 2 between the Direct Connect location and the data center. It is common to have a Site-to-Site VPN connection for additional confidentiality of the data. The Site-to-Site VPN connection can terminate on the transit gateway by using a normal VPN attachment. The following diagram shows this architecture.

![Connections from on-premises data centers to the AWS Cloud through AWS Direct Connect.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/5c4093e5-5b61-4461-b526-057b05a45dd7.png)

The following are the benefits of this approach:
+ Observability: Integration for managed active monitoring by using [Network Synthetic Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html)
+ Scalability: Support for increased bandwidth throughput
+ Adaptability: IPv6 support
+ TCO: Potential to reduce data transfer
+ TCO: Consistent network experience
+ Network isolation: Private connectivity that can fulfill regulatory requirements

The following are the drawbacks of this approach:
+ Ease of integration: Time and manual effort to set up
+ Scalability: Limited scalability beyond tens of Direct Connect connections because there are multiple [quotas](https://docs.aws.amazon.com/directconnect/latest/UserGuide/limits.html) to track
+ Adaptability: Configuration options depend on the available Direct Connect locations
+ TCO: Scheduled Direct Connect maintenance can cause downtime that requires action

## Connecting with a transit VPC architecture
<a name="options-onprem-transit-vpc"></a>

Transit VPC is an architecture option that gives flexibility to the consumers for how to connect to AWS, and it allows SaaS providers to benefit from having unified access to their service through AWS PrivateLink. The consumer connects from on premises to a transit VPC that contains only an entry point (such as a virtual private gateway) and an interface VPC endpoint, which is an AWS PrivateLink resource. The transit VPCs should either be owned by the SaaS provider or by the consumers. This section discusses both options.

You can create the transit VPC and subnets with CIDR ranges that are compatible with the on-premises data center. If they require private connectivity, consumers can connect to that VPC through AWS Direct Connect or AWS Site-to-Site VPN. You can also configure access to the transit account from the public internet by using an Application Load Balancer or Network Load Balancer that points to the VPC endpoint.

### Consumer-managed transit VPC
<a name="consumer-managed-transit-vpc.9e4ac57b-e2ad-516e-a6f6-16361c548f3a"></a>

In this approach, the SaaS provider leaves management of the transit VPCs up to the consumers. From a technical point of view, the SaaS provider's architecture is the same as when connecting to consumers in the AWS Cloud through AWS PrivateLink. From sales and product perspective, it is additional effort because some consumers don't have AWS accounts yet. They might be hesitant to open and operate an account. The SaaS provider should give guidance to their consumers about how to create AWS accounts and connect their on-premises data center. The following diagram shows a mix of public and private access, where the consumers own the transit VPCs.

![The consumer manages a transit VPC in the AWS Cloud.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/facca3c1-c561-4310-9f63-458838d40cad.png)

The following are the benefits of this approach:
+ Time to repair: Operational overhead is largely offloaded to SaaS consumers
+ Adaptability: SaaS consumers can choose from different access options
+ Adaptability: No CIDR range conflicts, even when using Site-to-Site VPN or Direct Connect
+ All metrics: Service provider inherits AWS PrivateLink benefits

The following are the drawbacks of this approach:
+ Ease of integration: SaaS consumers require at least one AWS account
+ TCO: A transit VPC is an architecture, not a fully managed service, so it requires more operational effort

### Provider-managed transit VPC
<a name="provider-managed-transit-vpc.26c8551e-0ee4-5d6e-b118-4768390258d8"></a>

This approach uses the same technologies, but the account boundaries and responsibilities change. Here, the SaaS provider owns the transit VPCs, preferably in a separate account from the SaaS offering. This decoupling reduces costs, reduces risks, and allows the transit account to scale independently. For environments that require a high degree of isolation, you can create additional separation between tenants by using a subnet or by creating a separate transit VPC for each consumer. The consumers can then choose how to connect to the transit VPC. This approach provides more options to expand the total addressable market, but it has a higher TCO for the SaaS provider due to the need to operate and monitor additional architectural components.

![The SaaS provider manages one or more transit VPCs in the AWS Cloud.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/8089d241-fd4b-4916-bc2b-fd5121ef45bf.png)

The following are the benefits of this approach:
+ Adaptability: SaaS consumers can choose from different access options
+ Adaptability: SaaS consumers don't need to have an AWS account
+ Adaptability: No CIDR range conflicts, even when using Site-to-Site VPN or Direct Connect

The following are the drawbacks of this approach:
+ TCO: A transit VPC is an architecture, not a fully managed service, so it requires more operational effort
+ TCO: SaaS provider needs to operate and monitor additional architectural components

## Connecting through the public internet
<a name="options-onprem-internet"></a>

Public internet access** **is also a valid option for providing access to a SaaS offering, although it does not offer private connectivity in the traditional sense. Some consumers might still prefer a public access approach because it requires no additional networking infrastructure between them and the SaaS provider. It reduces complexity, cost, and integration time in exchange for an increased attack surface. Strong authentication and authorization mechanisms can help mitigate the increased threat level, and you should always encrypt traffic. It is still recommended that you have an additional layer of security in this scenario, such as by using [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html).

The architecture in this scenario is straightforward. The consumer connects to a public host (the SaaS provider) through the internet. The application can be hosted directly on a public Amazon Elastic Compute Cloud (Amazon EC2) instance with an [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html). The preferred option is to host it behind an Application Load Balancer or similar service. For better performance and caching static assets, you can use a content delivery network, such as [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html). To serve an application with minimum latency over two global static Anycast IP addresses, you can place [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) in front of an Amazon EC2 instance, Network Load Balancer, or Application Load Balancer. In addition, CloudFront, Application Load Balancers, AWS AppSync, and Amazon API Gateway all integrate with AWS WAF. The following diagram provides an overview of the public internet access connectivity options.

![Connectivity to a SaaS offering through the public internet.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/65e826b1-1382-4e43-a688-c1537735ae3f.png)

The following table describes supported protocols and integrations for this scenario.

|
|
| **Service or resource** | **IPv6** | **AWS WAF integration** | **Can be a Global Accelerator endpoint** |
| --- |--- |--- |--- |
| **Amazon CloudFront** | Supported | Supported | Not supported |
| **Amazon API Gateway** | Supported | Supported | Not supported |
| **AWS AppSync** | Partially supported | Supported | Not supported |
| **Amazon EC2 with an Elastic IP address** | Supported | Not supported | Supported |
| **Application Load Balancer** | Supported | Supported | Supported |
| **Network Load Balancer** | Supported | Not supported | Supported |

The following are the benefits of this approach:
+ Ease of integration: Simplicity and accessibility
+ Scalability: Unlimited scale
+ Adaptability: No CIDR range conflicts possible
+ Adaptability: CloudFront support

The following are the drawbacks of this approach:
+ Network isolation: No private connectivity
+ Network isolation: Strong security measures required

Other benefits and drawbacks apply, depending on the services that you choose.
