---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway-vpn.html
---

# AWS Transit Gateway \+ AWS Site-to-Site VPN
<a name="aws-transit-gateway-vpn"></a>

 [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is an AWS managed high availability and scalability regional network transit hub used to interconnect VPCs and customer networks. AWS Transit Gateway \+ VPN, using the [Transit Gateway VPN attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html), provides the option of creating an IPsec VPN connection between your remote network and the Transit Gateway over the internet, as shown in the following figure.

![Diagram showing a managed IPsec VPN connection between your remote network and the Transit Gateway.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/transit-gateway-and-site-to-site-vpn.png)

 Consider using this approach when you want to take advantage of an AWS-managed VPN endpoint for connecting to multiple VPCs in the same region without the additional cost and management of multiple IPsec VPN connections to multiple Amazon VPCs.

 AWS Transit Gateway also supports and encourages multiple user gateway connections so that you can implement redundancy and failover on your side of the VPN connection as shown in the following figure.

![Diagram showing redundancy and failover.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/transit-gateway-and-redundant-vpn.png)

 Both dynamic and static routing options are provided to give you flexibility in your routing configuration on the Transit Gateway VPN IPsec attachment. Dynamic routing uses BGP peering to exchange routing information between AWS and these remote endpoints. With dynamic routing, you can also specify routing priorities, policies, and weights (metrics) in your BGP advertisements and influence the network path between your networks and AWS. It’s important to note that when you use BGP, both the IPsec and the BGP sessions must be terminated on the same user gateway device, so it must be capable of terminating both IPsec and BGP sessions.

Per VPN connection, you can achieve 1.25 Gbps of throughput and 140,000 packets per second. When terminating the VPN connections in the Transit Gateway, you can use Equal Cost Multi-Path (ECMP) routing to get a higher VPN bandwidth by aggregating multiple VPN tunnels. To use ECMP, you need to configure dynamic routing in the VPN connections – ECMP is not supported using static routing.

 In addition, you can enable acceleration in your AWS Site-to-Site VPN connections. An accelerated VPN connection uses [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) to route traffic from your network to an AWS edge location that is closest to your customer gateway device. You can use this option to avoid network disruptions that might occur when the traffic is routed over the public internet. Acceleration is only supported for VPN connections that are attached to a Transit Gateway, as shown in the following figure:

![Diagram that shows acceleration on VPN connections that are attached to a Transit Gateway.](http://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/accelerated-site-to-site-vpn.png)

 Last, regarding IP addressing, Site-to-Site VPN connections on an AWS Transit Gateway support both IPv4 and IPv6 traffic. The following rules apply:
+  IPv6 is only supported for the inside IP addresses of the VPN tunnel. The outside IP address for the AWS endpoints are public IPv4 addresses. The customer gateway IP address should be a public IPv4 address.
+  A Site-to-Site VPN connection cannot support both IPv4 and IPv6 traffic. If your hybrid connectivity requires dual-stack communication, you should create different VPN tunnels for the IPv4 and IPv6 traffic.

## Additional resources
<a name="additional-resources-1"></a>
+  [Transit gateway VPN attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html)
+  [ Customer gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html)
+  [Working with Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/working-with-site-site.html)
+  [Accelerated Site-to-Site VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html)
