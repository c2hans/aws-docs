---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/architecture-3.html
---

# Architecture 3: AWS Transit Gateway
<a name="architecture-3"></a>

[AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is a managed routing service that connects VPCs and on-premises networks. Transit Gateway can help you simplify your network topology and avoid complex peering relationships between large numbers of VPCs.

Transit Gateway acts as a cloud router. Each new connection is only made once between a VPC and the transit gateway. By using the transit gateway as a hub that support transitive routing, you do not need to add peer relationships between every single VPC in a mesh topology. For more information about Transit Gateway and its quotas, see [Quotas for your transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-quotas.html).

Using Transit Gateway to integrate a third-party service has the following benefits:
+ Supports bidirectional traffic between your VPCs and the third-party network
+ Supports all types of IP traffic (both TCP and UDP)
+ Deploys a centralized traffic inspection point between your VPCs and the third-party network
+ Easily scales as the number of VPCs involved in the integration changes

The disadvantages of using a Transit Gateway solution include:
+ This option is typically more expensive than the direct peering options.
+ Overlapping CIDR blocks are not supported.
+ Many third-party providers do not support this solution because they want to maintain complete control and minimize sharing components with their customers.

The following architecture diagram shows a simplified representation of using Transit Gateway to connect your VPCs to those of a third-party provider. Each VPC connects to the transit gateway, and the gateway supports transitive routing between all of the attached VPCs.

![Using Transit Gateway to connect VPCs in different AWS accounts](https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/images/guide-img/80f3a808-d645-486e-82c4-f574fdcf6710/images/40e29cc8-b5f3-4b1c-957a-2b3fb8b8c55b.png)

However, the actual configuration is more nuanced, and this architecture is divided into different deployment considerations and options.

## Centralizing network inspection
<a name="centralized-network-inspection"></a>

If you use Transit Gateway, you can deploy a centralized network traffic inspection point, a dedicated inspection VPC. By using static routes in the route table associated with the intra-Region peering attachment, you can direct traffic coming from the third-party network to the inspection VPC. To inspect the traffic, you can use AWS Network Firewall or an AWS Gateway Load Balancer paired with virtual security appliances deployed on Amazon Elastic Compute Cloud (Amazon EC2) instances. For more information, see *Centralized deployment model* in [Deployment models for AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/) (AWS blog post).

The transit gateway must be in [appliance mode](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html#transit-gateway-appliance-support) for the inspection VPC attachment to route the bidirectional traffic symmetrically. As shown in the following architecture diagram, the transit gateway directs traffic from the attached VPCs to an elastic network interface in the inspection VPC.

![Creating a centralized inspection point in a dedicated VPC.](https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/images/guide-img/80f3a808-d645-486e-82c4-f574fdcf6710/images/6fa8e69d-2277-4609-8c4f-f563ae33fa93.png)

## Selecting a deployment option
<a name="selecting-deployment-options"></a>

The first thing to consider is whether you will be using an existing transit gateway in your network or creating a new, dedicated transit gateway. We recommend deploying a new, dedicated transit gateway because it proves provides more control and separation from the third-party network. The sample architectures in this guide create a new transit gateway, and you can create peering connections between the existing gateway and new gateway.

The second thing to consider is which architecture is best for your use case:

1. [Architecture 3.1: Transit Gateway with AWS RAM](architecture-3-1.md) – In this deployment option, you share a single transit gateway with the third-party account. You use AWS Resource Access Manager (AWS RAM) to configure the sharing relationship.

1. [Architecture 3.2: Transit Gateway peering](architecture-3-2.md) – In this deployment option, you create a peering connection between two transit gateways, one in your account and one in the third-party account.

When selecting between these options, consider the following benefits and disadvantages of each.

|
|
|   | Architecture 3.1: Transit Gateway with AWS RAM | Architecture 3.2: Transit Gateway peering |
| --- |--- |--- |
| **Benefits** | A transit gateway is not required in the third-party account, leading to a more streamlined architecture. | A third party might find this solution more acceptable because it provides them more control of the networking configuration. |
| You have enhanced control and visibility as the owner of the shared transit gateway. | You have reduced operational effort because the third party maintains their own VPC attachments. |
| **Disadvantages** | The third party might be reluctant because it reduces their control of the networking configuration. | The networking architecture is more complex. |
| You are responsible for configuring transit gateway attachments to VPCs in the third-party account. | This architecture creates an additional hop in the traffic path. |

### Cost considerations
<a name="cost-considerations.c64232fa-4aed-543c-99da-f55520bc3e91"></a>

Also consider the following cost implications when deciding between these options:
+ The hourly fee for the transit gateway attachment is charged to the account owner of the attachment (or *VPC*). Some costs will be owned by you, and others will be owned by the third party.
+ Data processing is charged to the owner of the VPC that sends traffic through the transit gateway. There is no charge for receiving data from the transit gateway.
+ There are no data-processing charges for data sent between two peered transit gateways.

For more information, see [AWS Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/).
