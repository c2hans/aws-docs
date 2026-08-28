---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/outbound-inspection-through-a-nat-and-internet-gateway.html
---

# Outbound inspection through a NAT and internet gateway
<a name="outbound-inspection-through-a-nat-and-internet-gateway"></a>

The following diagram shows the workflow if you need to inspect outbound traffic originating from a VPC to the internet.

![Inspecting traffic from a VPC to the internet through a NAT gateway and internet gateway](http://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/images/guide-img/7951faf9-5db9-4729-86ff-47c734d59b19/images/dc1ee160-2546-472d-8001-de273e07e1a7.png)

The diagram shows the following workflow:

1. The packet from an Amazon Elastic Compute Cloud (Amazon EC2) instance in `Workload spoke VPC1` in Availability Zone 1 arrives at the Transit Gateway elastic network interface in Availability Zone 1. According to the `Workload spoke VPC1` route table that is associated with the source, the packet arrives at the Transit Gateway.

1. In Transit Gateway, the spoke transit gateway route table is associated with the `Workload spoke VPC1` attachment, which determines the next hop.

1. The next hop is the `Appliance VPC`. The Transit Gateway determines which Transit Gateway elastic network interface to send the traffic to based on 4-tuple hash.

1. If Transit Gateway chooses the Transit Gateway elastic network interface in Availability Zone 2, it then checks the VPC route table associated to the Transit Gateway elastic network interface subnet in Availability Zone 2 for the `Appliance VPC` and then sends the traffic to the Gateway Load Balancer endpoint based on the default route.

1. The Gateway Load Balancer endpoint is logically connected to Gateway Load Balancer through AWS PrivateLink, which forwards the traffic to the firewall appliance for traffic inspection. Gateway Load Balancer creates a GENEVE tunnel between it and the firewall appliances.

1. If the traffic is allowed then the packet is sent back to the Gateway Load Balancer and the Gateway Load Balancer endpoint in Availability Zone 1 from where it came from based on metadata attached to the payload.

1. At the Gateway Load Balancer endpoint in Availability Zone 1, the packet checks the VPC route table to determine the next hop.

1. The packet arrives at `NAT gateway 1` and looks at the NAT gateway's route table, with the default route being the internet gateway.

1. The packet is then sent to its destination through the internet gateway. The return traffic follows the same path but in reverse.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
