---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/introduction.html
---

# Implementing inline traffic inspection using third-party security appliances
<a name="introduction"></a>

*Pooja Banerjee, Amazon Web Services*

This guide describes how to implement inline traffic inspection architectures by using third-party firewall appliances, [AWS Transit Gateway](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway.html), and [Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html) on the AWS Cloud. This guide also explains how to design and architect your virtual private clouds (VPCs) to meet traffic inspection requirements and understand traffic flow based on network traffic inspection scenarios.

Inline traffic inspection helps you screen and secure traffic to protect your workloads from malicious actors. By using firewalls, you can inspect network traffic in real time as it flows from source to destination and then allow or deny traffic based on the firewall policies. This guide is intended for network and security engineers who are responsible for managing enterprise-wide networks. The guide discusses the following traffic inspection use cases:
+ Inspecting traffic between two workload VPCs
+ Monitoring traffic going to the internet from an existing workload VPC
+ Monitoring traffic from a workload VPC to on premises through an AWS Direct Connect connection

Several traffic inspection deployments are currently available, including an active or standby setup, a sandwich model that uses source network address translation (SNAT) with load balancers on each side of the inspection firewalls, and a VPN overlay model. Although these options can have drawbacks in terms of scalability, high availability (HA), or over-complexity, you can resolve these issues by using a Gateway Load Balancer.

Gateway Load Balancers work at layer 3 and layer 4 of the Open Systems Interconnection (OSI) model. At layer 3, a Gateway Load Balancer transparently routes the packet from source to third-party appliances before sending it to the destination in a symmetrical manner. At layer 4, a Gateway Load Balancer provides highly-available and scalable load balancing capability to the endpoints, in addition to performing health checks. Because firewalls are stateful appliances, the flow from source to destination and the traffic's return flow must remain on the same firewall appliance.

This guide provides a traffic inspection solution for the following three use cases:
+ [VPC-to-VPC traffic inspection](vpc-to-vpc-traffic-inspection.md)
+ [VPC-to-on-premises traffic inspection](on-premises-traffic-inspection.md)
+ [Outbound traffic inspection through a NAT gateway and internet gateway](outbound-inspection-through-a-nat-and-internet-gateway.md)
