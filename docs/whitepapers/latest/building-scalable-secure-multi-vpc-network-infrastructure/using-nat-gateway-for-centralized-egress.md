---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/using-nat-gateway-for-centralized-egress.html
---

# Using the NAT gateway for centralized IPv4 egress
<a name="using-nat-gateway-for-centralized-egress"></a>

NAT gateway is a managed network address translation service. Deploying a NAT gateway in every spoke VPC can become cost prohibitive because you pay an hourly charge for every NAT gateway you deploy (refer to [Amazon VPC pricing](http://aws.amazon.com/vpc/pricing/)). Centralizing NAT gateways can be a viable option to reduce costs. To centralize, you create a separate egress VPC in the network services account, deploy NAT gateways in the egress VPC, and route all egress traffic from the spoke VPCs to the NAT gateways residing in the egress VPC using Transit Gateway or CloudWAN, as shown in the following figure.

**Note**
When you centralize NAT gateway using Transit Gateway, you pay an extra Transit Gateway data processing charge — compared to the decentralized approach of running a NAT gateway in every VPC. In some edge cases when you send huge amounts of data through NAT gateway from a VPC, keeping the NAT local in the VPC to avoid the Transit Gateway data processing charge might be a more cost-effective option.

![A diagram depicting a decentralized high availability NAT gateway architecture](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/decentralized-ha-nat-gateway.png)

![A diagram depicting a centralized NAT gateway using Transit Gateway (overview)](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/centralized-nat-gateway-tg.png)

![A diagram depicting a centralized NAT gateway using Transit Gateway (route table design)](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/nat-gateway-tg-rt.png)

In this setup, spoke VPC attachments are associated with Route Table 1 (RT1) and are propagated to Route Table 2 (RT2). There is a [Blackhole](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) route to disallow the two VPCs from communicating with each other. If you want to allow inter-VPC communication, you can remove the `10.0.0.0/8 -> Blackhole` route entry from RT1. This allows them to communicate via the transit gateway. You can also propagate the spoke VPC attachments to RT1 (or alternatively, you can use one route table and associate/propagate everything to that), enabling direct traffic ﬂow between the VPCs using Transit Gateway.

You add a static route in RT1 pointing all traffic to egress VPC. Because of this static route, Transit Gateway sends all internet traffic through its ENIs in the egress VPC. Once in the egress VPC, traffic follows the routes deﬁned in the subnet route table where these Transit Gateway ENIs are present. You add a route in subnet route tables pointing all traffic towards the respective NAT gateway in the same Availability Zone to minimize cross-Availability Zone (AZ) traffic. The NAT gateway subnet route table has internet gateway (IGW) as the next hop. For return traffic to ﬂow back, you must add a static route table entry in the NAT gateway subnet route table pointing all spoke VPC bound traffic to Transit Gateway as the next hop.

## High availability
<a name="HA-1"></a>

 For high availability, you should use more than one NAT gateway (one in each Availability Zone). If a NAT gateway is unavailable, traffic might be dropped in that Availability Zone that is traversing the affected NAT gateway. If one Availability Zone is unavailable, the Transit Gateway endpoint along with NAT gateway in that Availability Zone will fail, and all traffic will flow via the Transit Gateway and NAT gateway endpoints in the other Availability Zone.

## Security
<a name="Security-1"></a>

You can rely on security groups on the source instances, blackhole routes in the Transit Gateway route tables, and the network ACL of the subnet in which the NAT gateway is located. For example, customers can use ACLs on the NAT Gateway public subnet(s) to allow or block source or destination IP addresses. Alternatively, you can use NAT Gateway with AWS Network Firewall for centralized egress described in the next section to meet this requirement.

## Scalability
<a name="Scalability-1"></a>

A single NAT gateway can support up to 55,000 simultaneous connections per assigned IP address to each unique destination. You can request a quota adjustment to allow up to eight assigned IP addresses, allowing for 440,000 simultaneous connections to a single destination IP and port. NAT gateway provides 5 Gbps of bandwidth and automatically scales to 100 Gbps. Transit Gateway generally does not act as a load balancer and would not distribute your traffic evenly across NAT gateways in the multiple Availability Zones. The traffic across the Transit Gateway will stay within an Availability Zone, if possible. If the Amazon EC2 instance initiating traffic is in Availability Zone 1, traffic will ﬂow out of the Transit Gateway elastic network interface in the same Availability Zone 1 in the egress VPC and will ﬂow to the next hop based on that subnet route table that elastic network interface resides in. For a complete list of rules, refer to [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the Amazon Virtual Private Cloud documentation.

 For more information, refer to the [Creating a single internet exit point from multiple VPCs Using AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-a-single-internet-exit-point-from-multiple-vpcs-using-aws-transit-gateway/) blog post.
