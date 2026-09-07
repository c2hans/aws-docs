---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-perimeter-zone-apps-network-firewall/architecture.html
---

# Architecture
<a name="architecture"></a>

## Traditional perimeter zone architecture
<a name="traditional-perimeter-zone-architecture"></a>

In many organizations, internet-facing applications are "walled off" in a perimeter zone that's separated from an on-premises environment. As the following diagram shows, the application traffic is routed to the perimeter zone through a firewall, and the applications in the perimeter zone are separated from other applications and the network by another firewall.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-perimeter-zone-apps-network-firewall/images/guide-img/e9c77201-9323-4f46-9aa2-8c71588f3ec4/images/80b5b03d-65e4-4ddd-a4d4-9af53bd5fff9.png)

## Perimeter zone architecture based on Network Firewall
<a name="perimeter-zone-applications-network-firewall"></a>

The following diagram shows an example network architecture of a perimeter zone application in the AWS Cloud:

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-perimeter-zone-apps-network-firewall/images/guide-img/e9c77201-9323-4f46-9aa2-8c71588f3ec4/images/b4c5a0aa-4b81-4733-8c89-05e60219c305.png)

In the above network architecture example, the application is protected through the following mechanisms:
+ A web application firewall from Amazon CloudFront serves as the first layer of protection against attacks on the application endpoint.
+ In the public subnet, Network Firewall inspects all the traffic that's routed to the application endpoint (through the Application Load Balancer). To ensure that all the traffic goes through the endpoints of Network Firewall, you must update the routing table, as the diagram shows.

We recommend that you route all the egress traffic from the application to Transit Gateway through the network firewall. This helps to vet all the traffic in the account before routing that traffic to the protected network.

## Traffic data flow
<a name="traffic-data-flow"></a>

The following diagram shows the data flow of traffic through a perimeter zone architecture that's based on Network Firewall:

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-perimeter-zone-apps-network-firewall/images/guide-img/e9c77201-9323-4f46-9aa2-8c71588f3ec4/images/52f994a2-42a2-41a8-a3a9-bc5b938fe958.png)

The diagram shows the following workflow:

1. Users access your application over the internet through CloudFront. You can use the default DNS in CloudFront or the DNS supported by [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html).

1. Internet gateway routing logic forwards all the incoming requests intended for the Application Load Balancer to Network Firewall over the firewall's network interface through the routing table configuration. This is illustrated by **Route table IGW** in the diagram from the *Perimeter zone architecture based on Network Firewall* section of this guide.

1. The received traffic is either blocked or forwarded based on the rules in Network Firewall. It's also possible to create rules for sending alerts. Network Firewall is completely transparent to the incoming or outgoing traffic flow and doesn't perform network address translation.

1. The incoming traffic that passes the firewall reaches the Application Load Balancer without changes. When the Application Load Balancer responds again, it forwards the requests (based on the routing table logic) to the network firewall. This is illustrated by **Route table endpoint A **and **Route table endpoint B **in the diagram from the *Perimeter zone architecture based on Network Firewall* section of this guide.

## Network components
<a name="network-components"></a>

We recommend that you include the following components in the perimeter zone architecture that you design for the AWS Cloud:
+ [Amazon CloudFront and AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)** **– CloudFront works with AWS WAF to provide distributed denial of service (DDoS) protection, web application firewalls, IP allow lists (if required), and content delivery. CloudFront must use SSL certificates only for accepting HTTPS connections (encryption in transit).
+ [Internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) – Use internet gateway to connect your VPC to the internet. Based on the route tables (see **Route table IGW** in the diagram from the *Perimeter zone architecture based on Network Firewall* section of this guide), all the incoming traffic intended for the endpoint subnet (that is, for the load balancer) is routed first to Network Firewall over its elastic network interface. This is illustrated by **eni-id-sec1 **and** eni-id-sec2 **in the diagram from the *Perimeter zone architecture based on Network Firewall* section of this guide.
+ [Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) – Network Firewall is an autoscaling firewall that provides firewalling and monitoring capabilities for ingress and egress traffic. You can attach Network Firewall to your VPC over the Gateway Load Balancer endpoint type. Place the endpoints in a public facing network to allow traffic to and from the internet gateway to be routed to Network Firewall. This is illustrated by **Route table security **in the diagram from the *Perimeter zone architecture based on Network Firewall* section of this guide.
+ [Endpoint subnet and Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) – Use an internet-facing Application Load Balancer to make your application accessible over the internet. You must have a protected subnet that's exposed to the internet over Network Firewall only. This routing is defined by the route table configurations. The route table allows only one route with source **0.0.0.0/0**, so you must have two route tables for each subnet and firewall network interface combination. This is illustrated by **Route table endpoint A** and **Route table endpoint B** in the diagram from the *Perimeter zone architecture based on Network Firewall* section of this guide. To have encryption in transit, you must enable the load balancer with SSL.
+ [Transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) – A transit gateway provides access to other networks, such as on-premises networks or other VPCs. In the network architecture presented in this guide, the transit gateway is exposed through a network interface in the endpoint's subnet. This implementation ensures that the transit gateway receives traffic that's originating from the web application (that is, the private subnet).
+ [Application subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) – This is a private subnet where the application is running on Amazon Elastic Compute Cloud (Amazon EC2) instances.
+ [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) – The architecture example in this guide doesn't include a NAT gateway. If your network architecture requires a NAT gateway, then we recommend that you add a NAT gateway in each subnet. In that case, we also recommend that the route table for your application has destination **0.0.0.0/0** mapped to the NAT gateway's network interface.

## Migrating perimeter zone applications
<a name="migrating-perimeter-zone-applications"></a>

The discovery process is critical to the success of your migration. When you use discovery tools, such as AWS Application Discovery Service, we recommend that you ensure that the tools can be installed on both your perimeter network and internal network. We also recommend that you verify that you can correctly capture the data flow. It's a best practice to supplement the automated discovery done by your tooling with a manual discovery process. For example, as part of the manual discovery process, you can interview the application team to get a deeper understanding of your application's technical requirements and considerations. The manual process can also help you identify edge cases that can impact the design of your application in the AWS Cloud.

We recommend that you identify the following as part of the discovery process:

1. Network dependencies between the client in the untrusted network and perimeter network

1. Dependencies between the perimeter network and application components in a secure network

1. Any third-party connections made directly through the VPN to the secure network

1. Any existing web application firewalls

1. Any intrusion detection systems and intrusion prevention systems that are in-place and their respective rules for detection (where possible)
