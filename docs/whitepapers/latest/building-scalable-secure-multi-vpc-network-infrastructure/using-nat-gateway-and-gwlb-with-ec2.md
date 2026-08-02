---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/using-nat-gateway-and-gwlb-with-ec2.html
---

# Using the NAT gateway and Gateway Load Balancer with Amazon EC2 instances for centralized IPv4 egress
<a name="using-nat-gateway-and-gwlb-with-ec2"></a>

Using a software-based virtual appliance (on Amazon EC2) from AWS Marketplace and AWS Partner Network as an exit point is similar to the NAT gateway setup. This option can be used if you want to use the advanced layer 7 ﬁrewall/Intrusion Prevention/Detection System (IPS/IDS) and deep packet inspection capabilities of the various vendor offerings.

In the following figure, in addition to NAT gateway, you deploy virtual appliances using EC2 instances behind a Gateway Load Balancer (GWLB). In this setup, the GWLB, Gateway Load Balancer Endpoint (GWLBE), virtual appliances and NAT gateways are deployed in a centralized VPC which is connected to Transit Gateway using VPC attachment. The spoke VPCs are also connected to the Transit Gateway using a VPC Attachment. Because GWLBEs are a routable target, you can route traffic moving to and from Transit Gateway to the fleet of virtual appliances that are configured as targets behind a GWLB. GWLB acts as a bump-in-the-wire and transparently passes all Layer 3 traffic through third-party virtual appliances, and thus invisible to the source and destination of the traffic. Therefore, this architecture allows you to centrally inspect all of your egress traffic traversing through Transit Gateway.

For more information on how the traffic flows from the applications in the VPCs to the internet and back through this setup, refer to [Centralized inspection architecture with AWS Gateway Load Balancer and AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/).

You can enable appliance mode on Transit Gateway to maintain flow symmetry through virtual appliances. This means the bidirectional traffic is routed through the same appliance and the Availability Zone for the life of the flow. This setting is particularly important for stateful firewalls performing deep packet inspection. Enabling appliance mode removes the need for complex workarounds, such as source network address translation (SNAT), to force traffic to return to the correct appliance to maintain symmetry. Refer to [Best practices for deploying Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/) for details.

It is also possible to deploy GWLB endpoints in a distributed manner without Transit Gateway to enable egress inspection. Learn more about this architectural pattern in the [Introducing AWS Gateway Load Balancer: Supported architecture patterns](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-gateway-load-balancer-supported-architecture-patterns/) blog post.

![A diagram depicting Centralized egress with Gateway Load Balancer and EC2 instance (route table design)](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/centralized-egress-gwlb-and-ec2.png)

## High availability
<a name="high-availabilty-2"></a>

AWS recommends deploying Gateway Load Balancers and virtual appliances in multiple Availability Zones for higher availability.

Gateway Load Balancer can perform health checks to detect virtual appliance failures. In case of an unhealthy appliance, GWLB reroutes the new flows to healthy appliances. Existing flows always go to the same target regardless of health status of target. This allows for connection draining and accommodate health check failures due to CPU spikes on appliances. For more details, refer to section 4: Understand appliance and Availability Zone failure scenarios in the blog post [Best practices for deploying Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/). Gateway Load Balancer can use auto scaling groups as targets. This benefit takes out the heavy lifting of managing availability and scalability of the appliance fleets.

## Advantages
<a name="advantages"></a>

Gateway Load Balancer and Gateway Load Balancer endpoints are powered by AWS PrivateLink, which allows for the exchange of traffic across VPC boundaries securely without the need to traverse the public internet.

Gateway Load Balancer is a managed service that removes undifferentiated heavy lifting of managing, deploying, scaling virtual security appliances so that you can focus on the things that matter. Gateway Load Balancer can expose the stack of firewalls as an endpoint service for customers to subscribe to using the [AWS Marketplace](https://aws.amazon.com/marketplace). This is called Firewall as a Service (FWaaS); it introduces a simplified deployment and removes the need to rely on BGP and ECMP to distribute traffic across multiple Amazon EC2 instances.

## Key considerations
<a name="key-considerations-2"></a>
+ The appliances need to support [Geneve](https://datatracker.ietf.org/doc/html/rfc8926) encapsulation protocol to integrate with GWLB.
+ Some third-party appliances can support SNAT and overlay routing ([two-arm mode](https://networkgeekstuff.com/networking/basic-load-balancer-scenarios-explained/)) therefore eliminating the need to create NAT gateways for saving costs. However, consult with an AWS partner of your choice before using this mode as this is dependent on vendor support and implementation.
+  Take a note of [GWLB idle timeout](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html#idle-timeout). This can result in connection timeouts on clients. You can tune your timeouts on client, server, ﬁrewall, and OS level to avoid this. Refer to *Section 1: Tune TCP keep-alive or timeout values to support long-lived TCP ﬂows* in the [Best practices for deploying Gateway Load Balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-for-deploying-gateway-load-balancer/) blog post for more information.
+ GWLBE are powered by AWS PrivateLink, so AWS PrivateLink charges will be applicable. You can learn more in the [AWS PrivateLink pricing page](https://aws.amazon.com/privatelink/pricing/). If you are using the centralized model with Transit Gateway, the TGW data processing charges will be applicable.
+ Consider deploying Transit Gateway and egress VPC in a separate Network Services account to segregate access based on delegation of duties, such as only network administrators can access Network Services Account.
