---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/transit-gateway-asymmetric-routing.html
---

# AWS Transit Gateway traffic flow and asymmetric routing
<a name="transit-gateway-asymmetric-routing"></a>

Before describing the different traffic inspection use cases, it's important to understand how traffic flows through AWS Transit Gateway. The following diagram shows the flow of traffic through Transit Gateway.

![Architecture diagram of a sample traffic flow through AWS Transit Gateway.](http://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/images/guide-img/7951faf9-5db9-4729-86ff-47c734d59b19/images/fc71c702-597f-42a9-8469-5eaba553cc42.png)

The diagram shows the traffic flow when a source Amazon Elastic Compute Cloud (Amazon EC2) instance in `Workload spoke VPC 1` in Availability Zone 1 sends traffic through Transit Gateway to a destination EC2 instance in `Workload spoke VPC2` in Availability Zone 2:

1. From the source EC2 instance in `Workload spoke VPC1` in Availability Zone 1, the packet goes to the Transit Gateway elastic network interface in `Workload spoke VPC1` in Availability Zone 1.

1. The packet lands on the transit gateway. The packet's next hop is determined based on the VPC route table associated to the subnet.

1. Based on the transit gateway route table associated with the attachment, the traffic is sent to the Transit Gateway elastic network interface in `Workload spoke VPC2` in Availability Zone 1 before being sent to the destination EC2 instance in `Workload spoke VPC2` in Availability Zone 2.

1. The path for return traffic is from the destination EC2 instance in `Workload spoke VPC2` in Availability Zone 2.

1. The packet goes to the Transit Gateway elastic network interface in `Workload spoke VPC2` in Availability Zone 2.

1. The packet reaches the transit gateway.

1. Based on the transit gateway route table associated with the attachment, the traffic is sent to the Transit Gateway elastic network interface in `Workload spoke VPC1` in Availability Zone 2.

1. The traffic arrives at the source EC2 instance in `Workload spoke VPC1` in Availability Zone 1.

By default, Transit Gateway maintains Availability Zone affinity, which means that it uses the same Availability Zone to forward the traffic from where it entered the transit gateway. Although this is appropriate for most use cases, this approach can cause asymmetric routing issues for stateful firewall appliances. Asymmetric routing occurs when the request and response use different network interfaces, which can cause traffic to be dropped. To avoid this, you should turn on appliance mode in the appliance VPC's transit gateway attachment. This resolves asymmetric routing issues in VPC-to-VPC architecture patterns when the source and destination EC2 instances are in two different Availability Zones and across different VPCs. For more information about this, see [Appliance in a shared services VPC](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation.
