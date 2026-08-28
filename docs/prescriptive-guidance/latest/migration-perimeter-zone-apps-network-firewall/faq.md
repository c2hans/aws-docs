---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-perimeter-zone-apps-network-firewall/faq.html
---

# FAQ
<a name="faq"></a>

## Do I need a load balancer to route internet traffic through a firewall in a multi-AZ deployment?
<a name="do-i-need-a-load-balancer-to-route-internet-traffic-through-a-firewall-in-a-multi-az-deployment-.13f524c7-b4e3-56b2-926f-d4c103af899b"></a>

Network Firewall is transparent to incoming and outgoing traffic and doesn't require a load balancer for itself. A load balancer is only required for the application (as in a standard multi-AZ deployment). In this guide's perimeter zone architecture, Network Firewall is inserted through route tables and the corresponding network interfaces in the public subnet.

## If the Application Load Balancer isn't in a public subnet (routed to an internet gateway), then is it an internal Application Load Balancer?
<a name="if-the-9999999999999999alb--isn-t-in-a-public-subnet--routed-to-an-internet-gateway---then-is-it-an-internal-9999999999999999alb--.094cd567-156f-591f-a130-9cce966ab6b0"></a>

The Application Load Balancer isn't an internal Application Load Balancer. The Application Load Balancer continues to the external, internet-facing subnet, even if the subnet isn't directly connected to the internet. The subnet is transparently available to the internet because the routing from the endpoint's subnet to the public subnet is based on the network interface of Network Firewall.

## Does Network Firewall need its own security subnet?
<a name="does-9999999999999999nwfw--need-its-own-security-subnet-.84ee413b-82df-561a-b2bd-28438c36fe29"></a>

Yes, Network Firewall needs its own security subnet. The security subnet (public) is required to ensure that the routing of the traffic from and to the Application Load Balancer can be controlled through the route tables.

## Is the target architecture valid for both ingress and egress traffic firewalling?
<a name="is-the-target-architecture-valid-for-both-ingress-and-egress-traffic-firewalling-.bd9951d9-bcaf-5794-b94a-10903a4fc921"></a>

Yes, the target architecture is valid for both ingress and egress traffic firewalling. If a connection is initiated from the application to outside the VPC, then you must add a NAT gateway to the endpoint's subnet. Also, you must forward the traffic from the application's subnet to the NAT gateway by using a route table (as illustrated by** Route table app **in the diagram from the *Perimeter zone architecture based on Network Firewall* section of this guide.). Then, no further changes are required because all the outgoing traffic still goes through Network Firewall.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
