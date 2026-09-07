---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/using-gwlb-with-tg-for-cns.html
---

# Using Gateway Load Balancer with Transit Gateway for centralized network security
<a name="using-gwlb-with-tg-for-cns"></a>

Often times, customers want to incorporate virtual appliances to handle the traffic filtering and to provide security inspection capabilities. In such use cases, they can integrate Gateway Load Balancer, virtual appliances, and Transit Gateway to deploy a centralized architecture for inspecting VPC-to-VPC and VPC-to-on-premises traffic.

Gateway Load Balancer is deployed in a separate security VPC along with the virtual appliances. The virtual appliances that will inspect the traffic are configured as targets behind the Gateway Load Balancer. Because Gateway Load Balancer endpoints are a routable target, customers can route traffic moving to and from Transit Gateway to the fleet of virtual appliances. To ensure flow symmetry, appliance mode is enabled on the Transit Gateway.

Each spoke VPC has a route table that is associated with the Transit Gateway, which has the default route to the Security VPC attachment as the next-hop.

The centralized Security VPC consists of appliance subnets in each Availability Zone; which have the Gateway Load Balancer endpoints and the virtual appliances. It also has subnets for Transit Gateway attachments in each Availability Zone, as shown in the following figure.

For more information on centralized security inspection with Gateway Load Balancer and Transit Gateway, refer to the [Centralized inspection architecture with AWS Gateway Load Balancer and AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/) blog post.

![A diagram depicting VPC-to-VPC and on-premises-to-VPC traffic inspection using Transit Gateway and AWS Gateway Load Balancer (route table design)](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/vpc-traffic-inspection-2.png)

## Key considerations for AWS Network Firewall and AWS Gateway Load Balancer
<a name="key-considerations-3"></a>
+ Appliance mode should be enabled on the Transit Gateway when doing east-west inspection.
+ You can deploy the same model for inspection of traffic to other AWS Regions using [AWS Transit Gateway Inter-Region peering](https://aws.amazon.com/blogs/networking-and-content-delivery/building-a-global-network-using-aws-transit-gateway-inter-region-peering/).
+ By default, each Gateway Load Balancer deployed in an Availability Zone distributes traffic across the registered targets within the same Availability Zone only. This is called Availability Zone affinity. If you enable [cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html#cross-zone-load-balancing), Gateway Load Balancer distributes traffic across all registered and healthy targets in all enabled Availability Zones. If all targets across all Availability Zones are unhealthy, Gateway Load Balancer fails open. Refer to section 4: Understand appliance and Availability Zone failure scenarios in the [Best practices for deploying Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/) blog post for more details.
+ For multi-Region deployment, AWS recommends that you set up separate inspection VPCs in the respective local Regions to avoid inter-Region dependencies and reduce associated data transfer costs. You should inspect traffic in the local Region instead of centralizing inspection to another Region.
+ Cost of running an additional EC2-based high availability (HA) pair in multi-Region deployments can add up. For more information, refer to the [Best practices for deploying Gateway Load Balancer ](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/) blog post.

### AWS Network Firewall vs. Gateway Load Balancer
<a name="network-firewall-vs-gwlb"></a>

*Table 2 — AWS Network Firewall vs Gateway Load Balancer*

|  Criteria  |  AWS Network Firewall | Gateway Load Balancer |
| --- | --- | --- |
|  Use case  | Stateful, managed, network firewall with intrusion detection and prevention service capability compatible with Suricata. | Managed service which makes it easy to deploy, scale and manage third-party virtual appliances  |
|  Complexity  | AWS managed service. AWS handles the scalability and availability of the service. | AWS managed service. AWS will handle the scalability and availability of the the Gateway Load Balancer service. The customer is responsible for managing the scaling and availability of the virtual appliances behind Gateway Load Balancer. |
|  Scale  | AWS Network Firewall endpoints are powered by AWS PrivateLink. Network Firewall supports up to 100 Gbps of network traffic per firewall endpoint. | Gateway Load Balancer endpoints support maximum bandwidth of up to 100 Gbps per endpoint  |
|  Cost  | AWS Network Firewall endpoint cost \+ Data processing charges  | Gateway Load Balancer \+ Gateway Load Balancer endpoints \+ virtual appliances \+ data processing charges  |
