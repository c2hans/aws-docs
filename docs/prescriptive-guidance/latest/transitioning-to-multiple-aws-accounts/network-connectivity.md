---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/network-connectivity.html
---

# Network connectivity
<a name="network-connectivity"></a>

## Connecting VPCs
<a name="connecting-vp-cs"></a>

Many companies use VPC peering in Amazon Virtual Private Cloud (Amazon VPC) to connect development and production VPCs. Using a VPC peering connection, you can route traffic between two VPCs by using private IP addressing. The connected VPCs can be in different AWS accounts and in different AWS Regions. For more information, see [What is VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) (Amazon VPC documentation). As companies grow and the number of VPCs increases, maintaining peering connections between all of the VPCs can become a maintenance burden. You might also be limited by the maximum number of VPC peering connections per VPC. For more information, see the [VPC peering connection quota](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-peering) (Amazon VPC documentation).

If you have multiple development, test, and staging environments that host non-production data across multiple AWS accounts, you might want to provide network connectivity between all of those VPCs but disallow any access to production environments. You can use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) to connect multiple VPCs across multiple accounts. You can separate the route tables to prevent development VPCs from communicating to production VPCs through the transit gateway, which acts as centralized router. For more information, see [Centralized router](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-centralized-router.html) (AWS Transit Gateway documentation).

AWS Transit Gateway also supports peering with other transit gateways, including those in different AWS accounts or AWS Regions. Because Transit Gateway is a fully managed, highly available service, you need to provision only one transit gateway for each Region.

For more information and detailed network architectures, see [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) (AWS Whitepaper).

## Connecting applications
<a name="connecting-applications"></a>

If you need to establish communication between applications in different accounts in the same environment (such as production), you can use one of the following options:
+ [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) or [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) can provide connectivity at the network level if you want to open broad access to multiple IP addresses and ports.
+ [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) creates endpoints in a private subnet of the VPC, and these endpoints are registered as DNS entries in [Amazon Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html). By using DNS, applications can resolve the endpoints and connect to the registered services, without requiring NAT gateways or internet gateways in the VPC.
+ [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-service-network.html) associates services, such as applications, across multiple accounts and VPCs and collects them into a *service network*. Clients in VPCs associated with the service network can send requests to all other services that are associated with the service network, regardless of whether they're in the same account. VPC Lattice integrates with AWS Resource Access Manager (AWS RAM) so that you can share resources with other accounts or through AWS Organizations. You can associate a VPC with only one service network. This solution doesn't require use of VPC peering or AWS Transit Gateway to communicate across accounts.

## Best practices for network connectivity
<a name="connectivity-best-practices"></a>
+ Create an AWS account that you use for the centralized networking. Name this account **network-prod**, and use it for AWS Transit Gateway and [Amazon VPC IP Address Manager](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) (IPAM). Add this account to the **Infrastructure\_Prod** organizational unit.
+ Use [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) (AWS RAM) to share the transit gateway, VPC Lattice service networks, and IPAM pools with the rest of the organization. This allows any AWS account within your organization to interact with these services.
+ By using IPAM pools to centrally manage IPv4 and IPv6 address allocations, you can allow your end-users to self-provision VPCs by using [AWS Service Catalog](https://aws.amazon.com/servicecatalog/). This helps you appropriately size VPCs and prevent overlapping IP address spaces.
+ Use a centralized egress approach for traffic bound to the internet, and use a decentralized ingress approach for traffic coming into your environment from the internet. For more information, see [Centralized egress](centralized-egress.md) and [Decentralized ingress](decentralized-ingress.md).
