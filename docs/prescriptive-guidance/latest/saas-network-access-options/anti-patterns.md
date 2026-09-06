---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/anti-patterns.html
---

# Anti-patterns for network access in the AWS Cloud
<a name="anti-patterns"></a>

An *anti-pattern* is a frequently used solution for a recurring issue where the solution is counter-productive, ineffective, or less effective than an alternative. The design options mentioned in this section usually work, but they come with significant disadvantages. If possible, they should be avoided because better alternatives are available.

This section discusses the following anti-patterns and challenges:
+ [Availability Zone mismatch with AWS PrivateLink](#anti-patterns-az-mismatch)
+ [AWS Site-to-Site VPN connections between AWS accounts](#anti-patterns-vpn-connection)

## Availability Zone mismatch with AWS PrivateLink
<a name="anti-patterns-az-mismatch"></a>

When providing access to an application through AWS PrivateLink, SaaS consumers can create interface VPC endpoints only in the Availability Zones where the application is deployed. For example, if the application is deployed in `use1-az1` and `use1-az2`, the consumer cannot deploy a VPC endpoint in `use1-az3`. We recommend that you deploy the SaaS offering in every Availability Zone. The majority of AWS Regions have three Availability Zones, although some have more. For a comprehensive list, see [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). Consider the number of Availability Zones when choosing an AWS Region.

**Note**
Availability zone names are different from Availability Zone IDs. For more information, see [Availability Zone IDs for your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html).

If a SaaS provider chooses not to deploy in all Availability Zones, there are some consequences. Assume the SaaS offering is deployed in `use1-az1` and `use1-az2`, but the consumer is using all three Availability Zones, including `use1-az3`. The interface VPC endpoints are deployed on the consumer side in `use1-az1` and `use1-az2`, and now the application in `use1-az3` needs to access one of these endpoints. First of all, traffic must be allowed from the subnets in the unmatched Availability Zones into the respective VPC endpoints. The consumer can decide to use the regional AWS PrivateLink DNS name, which can resolve to either VPC endpoint and which evenly distributes the traffic between the two. Or the consumer might choose to send traffic directly to an endpoint, such as `use1-az2`. This results in 67% of the traffic arriving on the provider side in `use1-az2` and 33% in `use1-az1`. The following figure depicts this scenario.

![Traffic is not evenly distributed to the Availability Zones.](http://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/images/guide-img/c6ce66a8-c949-4e68-b09d-850373110e63/images/d96ca5e2-eb91-4525-b6ed-45aa39e635a2.png)

With a significant number of consumers and an uneven distribution of traffic, a workload might run into capacity issues in one Availability Zone and be under capacity in another. To tackle that issue, the SaaS provider can decide to evenly load balance the traffic on their side by enabling [cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#cross-zone-load-balancing) on the Network Load Balancer. This incurs additional charges.

If only one Availability Zone is matched by the service provider, then all traffic will enter over a single endpoint. This creates an even larger imbalance. As a result, the SaaS offering is no longer highly available for the consumer. It doesn't matter to the consumer if the application is served over additional Availability Zones that they are not using themselves. In the worst case, a SaaS provider might not be able to serve a consumer who doesn't use any of the same Availability Zones.

In the rare case that there is no feasible option for the SaaS provider to provision their application over all Availability Zones, it is also possible to create a subnet only in the missing Availability Zones and then extend the service to those empty Availability Zones. Cross-zone load balancing can then distribute the incoming traffic over the actual application endpoints in the other Availability Zones.

## AWS Site-to-Site VPN connections between AWS accounts
<a name="anti-patterns-vpn-connection"></a>

Companies migrating from on-premises environments into the cloud sometimes try to lift and shift the entire network. This can cause problems because there are significant differences between on-premises and cloud networking practices. If this mindset shift does not happen, things like AWS Site-to-Site VPN connections from one VPC to another VPC can happen. This approach fails to take advantage of purpose-built networking services in the AWS Cloud, which simplify management and improve performance. Adapting to cloud-native designs helps reduce operational overhead and results in more reliable, scalable connectivity between VPCs.

If you're thinking of providing this connectivity option as a SaaS provider, ask yourself or the consumer why AWS Site-to-Site VPN should be used. Then, work backwards from those requirements to find a better connectivity option. The [Comparing service capabilities](services.md#services-capabilities) section of this guide contains a matrix that you can use to help identify options. Then, you can work through the relevant sections of this guide to find an architectural approach that addresses your use case.
