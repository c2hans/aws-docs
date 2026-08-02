---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/on-premises-traffic-inspection.html
---

# VPC-to-on-premises traffic inspection
<a name="on-premises-traffic-inspection"></a>

The following diagram shows the traffic flow if an Amazon Elastic Compute Cloud (Amazon EC2) instance in `Workload spoke VPC1` wants to communicate with an on-premises server.

![The traffic flow between an EC2 instance in spoke VPC 1 and an on-premises server](http://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/images/guide-img/7951faf9-5db9-4729-86ff-47c734d59b19/images/693e5646-fd5f-4e31-9928-1e74affb79d7.png)

The diagram shows the following workflow:

1. A packet from an EC2 instance in `Workload spoke VPC 1` in Availability Zone 1 arrives at the Transit Gateway elastic network interface in Availability Zone 1 in the transit gateway subnet for `Workload spoke VPC 1`. Based on the VPC route table associated to the Transit Gateway elastic network interface subnet, the packet lands on the transit gateway.

1. In the transit gateway, the `Spoke transit gateway route table` is associated with the `Workload spoke VPC 1` attachment and this determines the next hop.

1. The next hop is the appliance VPC. Based on 4-tuple hash for the life of a flow, the Transit Gateway determines which Transit Gateway elastic network interface to send the traffic to.

1. If Transit Gateway chooses the Transit Gateway elastic network interface in Availability Zone 1, it checks the VPC route table associated to the Transit Gateway elastic network interface subnet in Availability Zone 1 in the appliance VPC. Transit Gateway sends the traffic to the Gateway Load Balancer endpoint in Availability Zone 1.

1. The Gateway Load Balancer endpoint is logically connected to the Gateway Load Balancer through AWS PrivateLink that then forwards the traffic to the firewall appliance for traffic inspection. The Gateway Load Balancer creates a GENEVE tunnel between the Gateway Load Balancer and the firewall appliances.

1. If the traffic is allowed, the packet is sent back to the Gateway Load Balancer and the Gateway Load Balancer endpoint in Availability Zone 1.

1. At the Gateway Load Balancer endpoint, the packet checks the VPC route table and the next hop is the transit gateway.

1. The packet arrives at the transit gateway and performs a lookup on the appliance transit gateway route table that is associated to the appliance VPC attachment for the next hop to the `172.16.0.0/16` network.

1. The packet is then sent to the destination server on premises. The response traffic follows the same path but in reverse.
