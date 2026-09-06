---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/vpc-to-vpc-traffic-inspection.html
---

# VPC-to-VPC traffic inspection
<a name="vpc-to-vpc-traffic-inspection"></a>

VPC-to-VPC traffic inspection occurs when traffic originates from one VPC and is destined for another VPC. The traffic is redirected to an appliance VPC for traffic inspection before arriving at the destination VPC. The following diagram shows how traffic flows if an Amazon Elastic Compute Cloud (Amazon EC2) instance in `Workload spoke VPC1` needs to communicate with an EC2 instance in `Workload spoke VPC2`.

![Architecture diagram of traffic inspection between two spoke VPCs and an appliance VPC](http://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/images/guide-img/7951faf9-5db9-4729-86ff-47c734d59b19/images/8656b746-f214-4329-8b26-de61ead6f3a5.png)

1. The packet from an EC2 instance in `Workload spoke VPC1` in Availability Zone 1 goes to the Transit Gateway elastic network interface in the transit gateway subnet in Availability Zone 1.

1. Based on the default route defined in the VPC route table, the packet lands on the transit gateway.

1. In the transit gateway, the spoke transit gateway route table is associated with the `Workload spoke VPC1` attachment that determines the next hop.

1. The next hop is the appliance VPC. Because the appliance VPC attachment has appliance mode turned on, the transit gateway determines which Transit Gateway elastic network interface to forward the traffic to, based on the 4-tuples of the IP packet.

1. If Transit Gateway chooses the Transit Gateway elastic network interface in Availability Zone 1 in the `Appliance VPC`, the traffic sticks to Availability Zone 1 for both the request and the response traffic.

1. The traffic is sent to `Gateway Load Balancer endpoint 1` in Availability Zone 1.

1. The Gateway Load Balancer endpoint is logically connected to Gateway Load Balancer using AWS PrivateLink. The Gateway Load Balancer uses the 4-tuple hash algorithm to pick a firewall appliance for the life of the flow and then forwards the traffic for inspection to that appliance in the `Appliance VPC` in Availability Zone 1. The Gateway Load Balancer creates a GENEVE tunnel between it and the firewall appliance.

1. The traffic is inspected based on the firewall policy.

1. After the packet is successfully inspected, the packet is sent back to the Gateway Load Balancer and then to Gateway Load Balancer endpoint in the `Appliance VPC` in Availability Zone 1.

1. At the Gateway Load Balancer endpoint, the packet is sent to the transit gateway based on the VPC route table.

1. After the packet arrives at the transit gateway, it examines the route table associated for the `10.2.0.0/16` network, which is the destination network.

1. The packet is sent to the Transit Gateway elastic network interface in `Workload spoke VPC2` in Availability Zone 1 before arriving at the destination EC2 instance. Return traffic follows the same path but in reverse.

**Note**
Transit Gateway maintains Availability Zone affinity and uses the same Availability Zone that the original requests was created in. For example, if an EC2 instance in `Workload spoke VPC2` in Availability Zone 2 initiated the request, the packet is forwarded to the Transit Gateway elastic network interface subnet in `Workload spoke VPC2` in Availability Zone 2, lands on the transit gateway, and is then forwarded to the Transit Gateway elastic network interface subnet in Availability Zone 2 in the destination VPC. By turning on appliance mode in the appliance VPC, you can ensure that the flow of symmetry is maintained using the 4-tuple hash for the life of traffic.
