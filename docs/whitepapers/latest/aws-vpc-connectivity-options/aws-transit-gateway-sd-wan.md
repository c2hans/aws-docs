---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway-sd-wan.html
---

# AWS Transit Gateway \+ SD-WAN solutions
<a name="aws-transit-gateway-sd-wan"></a>

 Software Defined Wide Area Networks (SD-WANs) are used to connect your data centers, offices, or colocation environments over different transit networks (such as the public internet, MPLS networks, or the AWS backbone using AWS Direct Connect), managing the traffic automatically and dynamically across the most appropriate and efficient path based on network conditions, application type or quality of service (QoS) requirements.

 Use this approach if you have a complex network topology, with several data centers, offices, or colocation environments that need to communicate between themselves and with AWS. SD-WAN solutions can help you to efficiently manage this type of network.

 When talking about the connection of an SD-WAN network to AWS, AWS Transit Gateway provides a managed highly-available and scalable regional network transit hub to interconnect VPCs and your SD-WAN network. [Transit Gateway connect attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html) provide a native way to connect your SD-WAN infrastructure and appliances with AWS. This makes it easy to extend your SD-WAN into AWS without having to set up IPsec VPNs.

 Transit Gateway connect attachments support Generic Routing Encapsulation (GRE) for higher bandwidth performance compared to a VPN connection. It supports Border Gateway Protocol (BGP) for dynamic routing, and removes the need to configure static routes. This simplifies network design and reduces the associated operational costs. In addition, its integration with [Transit Gateway Network Manager](https://docs.aws.amazon.com/vpc/latest/tgwnm/what-is-network-manager.html) provides advanced visibility through global network topology, attachment level performance metrics, and telemetry data.

 When integrating your SD-WAN network to Transit Gateway using connect attachments, you have two common patterns. The first one is placing virtual appliances of the SD-WAN network in a VPC within AWS. Then, you use a VPC attachment as underlying transport for the Transit Gateway connect attachment between the virtual appliances and the Transit Gateway, as can be shown in the following figure.

![A diagram that shows using a VPC attachment as underlying transport.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/sd-wan-connectivity-with-transit-gateway.png)

 Alternatively, you can extend and segment your SD-WAN traffic to AWS without adding extra infrastructure. You can create Transit Gateway connect attachments using an AWS Direct Connect connection as underlying transport, as can be shown in the following figure.

![A diagram that shows using a VPC attachment as underlying transport.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/sd-wan-connectivity-with-transit-gateway-2.png)

 There are some considerations to be aware when using Transit Gateway connect attachments:
+  You can create a connect attachments on existing Transit Gateways.
+  Third-party appliances must be configured with a GRE tunnel in order to send and receive traffic from Transit Gateway using connect attachments. The appliance must be configured with BGP for dynamic route updates and health checks.
+  Connect attachments do not support static routes.
+  Transit Gateway connect attachments support a maximum bandwidth of five Gbps per GRE tunnel. Bandwidth above five Gbps can achieved by advertising the same prefixes across multiple Connect peer (GRE tunnels) for the same Connect attachment.
+  A maximum of four Connect peers are supported for each connect attachment.
+  Transit Gateway connect attachments support IPv6 and dynamic route advertisements through Multiprotocol Extensions for BGP (MBGP or MP-BGP).

## Additional resources
<a name="additional-resources-7"></a>
+  [Transit gateway peering attachments](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPN_CloudHub.html)
+  [Requirements and considerations ](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+  [Blog post: Simplify SD-WAN connectivity with AWS Transit Gateway Connect](https://aws.amazon.com/blogs/networking-and-content-delivery/simplify-sd-wan-connectivity-with-aws-transit-gateway-connect/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
