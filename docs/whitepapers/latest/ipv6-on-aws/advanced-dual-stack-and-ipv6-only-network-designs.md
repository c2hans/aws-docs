---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/advanced-dual-stack-and-ipv6-only-network-designs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Advanced dual-stack and IPv6-only network designs
<a name="advanced-dual-stack-and-ipv6-only-network-designs"></a>

## AWS Transit Gateway Connect attachment
<a name="aws-transit-gateway-connect-attachment"></a>

 AWS Transit Gateway Connect simplifies the branch connectivity through native integration of Software-Defined Wide Area Network (SD-WAN) network virtual appliances into AWS Transit Gateway using Generic Route Encapsulation (GRE) tunnels. For dynamic route exchange over the GRE tunnels AWS Transit Gateway Connect supports the following modes of BGP:
+  Exterior BGP (eBGP)
+  Interior BGP (iBGP)
+  Multi-protocol extension for BGP (MP-BGP)

 Multi-protocol BGP (MP-BGP) is an extension to BGP that enables BGP to carry routing information for multiple Network Layer protocols. The types of traffic that BGP can carry are known as *address families*, and the advantage of MP-BGP is being able to route multiple address families over one peering. This also means you can retrofit IPv6 connectivity on an existing connection. Refer to the [Integrate SD-WAN devices with AWS Transit Gateway and AWS Direct Connect](https://aws.amazon.com/blogs/networking-and-content-delivery/integrate-sd-wan-devices-with-aws-transit-gateway-and-aws-direct-connect/) blog post to learn how.

## Centralized internet outbound traffic with IPv6
<a name="centralized-internet-outbound-traffic-with-ipv6"></a>

 Centralized outbound traffic is a popular pattern with IPv4 as described in [Centralized egress to internet](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-to-internet.html). A similar pattern can be implemented with two different approaches:
+  Transparent proxy with IPv6 using a technology called *IPv6-to-IPv6 Network Prefix Translation* (NPTv6 or NAT66).
+  Explicit forward proxy configured in your OS or application settings.

 The first pattern requires use of AWS Transit Gateway and an EC2-based router appliance to perform the NAT66 function. The following figure shows a high-level configuration using a Linux-based NAT66 instance. Traffic from a client follows the default route to the Transit Gateway from where it is forwarded to a centralized outgoing traffic VPC.

 Once inside the outbound traffic VPC, it is forwarded to the NAT66 instance which translates the packet’s source IP to its own. For additional security, the NAT66 instance may provide firewall functionality. To achieve high availability, you can add multiple Availability Zones, or attach routing appliances using Transit Gateway Connect.

![This is a diagram that illustrates centralized internet outbound traffic with NAT66.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/centralized-internet-outbound-traffic-with-nat66.png)

**Note**
Centralized outbound traffic is applicable if you require centralized traffic inspection. With an outbound traffic only internet gateway, AWS makes it easy to achieve distributed outbound traffic. However, if there is an outbound traffic inspection requirement and it cannot be done in each VPC, the centralized pattern is useful.

 The second pattern requires a set of explicit proxies which can be configured in a centralized outbound traffic VPC. [Squid proxy](https://wiki.squid-cache.org/Features/IPv6) is a commonly used open-source proxy solution. After forward proxy is configured, and OS or applications settings are updated, you will be able to connect to IPv6 resources on the internet.

 **Using TGW with IPv6 to work around IPv4 address overlap**

 Transit gateways can attach to VPCs with overlapping IP address CIDRs. This is because the TGW isn’t affected by the address space used in a VPC apart from when it comes to configuring routes. While it is possible to attach a TGW to VPCs with overlapping CIDRs it is not possible to have conflicting routes. However, because IPv6 prefixes are globally unique it can provide connectivity between hosts residing in VPCs with overlapping IP CIDRs.

![This is a diagram that illustrates IPv6-only routing with AWS Transit Gateway.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/ipv6-only-routing-with-aws-transit-gateway.png)

 **Amazon EKS IPv6 clusters**

 To avoid IP address exhaustion, minimize latency at scale, and simplify routing configuration, the solution is to use IPv6 address space. There are a few advantages to using Amazon EKS clusters with an IPv6 network:

 First, you can run more pods on one single host or subnet without the risk of exhausting all available IPv4 addresses available in your VPC.

 Second, it allows for lower-latency communications with other IPv6 services, running on-premises, on AWS, or on the internet, by avoiding an extra NAT hop.

 Third, it relieves you of the burden of maintaining complex routing configurations.

 Also, pod networking is configured so that the pods can communicate with IPv4-based applications outside the cluster, allowing you to adopt the benefits of IPv6 on Amazon EKS without requiring that all dependent services deployed across your organization are first migrated to IPv6. For more information, refer to [Amazon EKS launches IPv6 support](https://aws.amazon.com/blogs/containers/amazon-eks-launches-ipv6-support/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
