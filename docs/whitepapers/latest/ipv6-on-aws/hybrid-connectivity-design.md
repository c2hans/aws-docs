---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/hybrid-connectivity-design.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid connectivity design
<a name="hybrid-connectivity-design"></a>

 Hybrid connectivity scenarios are a reality for many customers. We offer two methods for addressing these: AWS Direct Connect and AWS managed Site-to-Site VPN.

 AWS previously published the [Hybrid Connectivity](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/welcome.html) whitepaper, which focused on designs and considerations around these solutions, and most of that content remains relevant. However, that paper does not consider IPv6. This section assumes you are acquainted with the aforementioned document, and it focuses only on the best practices and differences compared to IPv4 implementations.

## AWS Direct Connect
<a name="aws-direct-connect"></a>

 [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) is a cloud service solution that makes it easy to establish a dedicated network connection from customer premises to AWS.

 Different aspects of the Direct Connect service deal with different layers of the OSI model. The choice of IPv6 only affects configuration related to Layer 3, so many aspects of Direct Connect configuration such as physical connections, link aggregation, VLANs, and jumbo frame are no different from IPv4 use cases.

 Where IPv6 does differ is when it comes to addressing and configuration of BGP peerings on top of a virtual network interface (VIF). There are three types of VIFs:
+  Private
+  Transit
+  Public

 The remainder of this section covers all of these.

**Note**
You can provision either 0 or 1 peering per address family on to a given VIF, so it is possible to retrofit IPv6 onto an existing VIF without the need to reprovision or deploy a new one.

 **Transit and Private VIF IPv6 peerings** — Whereas in IPv4 you are free to choose your own addressing for the logical point-to-point, in IPv6, AWS automatically allocates a /125 CIDR for each VIF, and it’s not possible to specify custom IPv6 addresses.

### Advertising IPv6 prefixes from AWS
<a name="advertising-ipv6-prefixes-from-aws"></a>

 When associating a Direct Connect Gateway directly with a Virtual Private Gateway (VGW) you can specify “Allowed Prefixes”. Think of this like a traditional “prefix-list” filter, controlling the prefixes advertised to your customer gateway. With IPv4, specifying no filter equates to `0.0.0.0/0` — no filtering. With IPv6, not specifying a value here results in all advertisements being implicitly blocked.

 Associating a Direct Connect Gateway with Transit Gateway “Allowed Prefixes” acts not as a filter but as static origination of routes advertised to your customer gateway.

**Note**
An “Allowed Prefix” IPv6 CIDR must be of length /64 or less specific, but you cannot specify “`::/0`”.
 VGW and Transit Gateway behave differently in regard to the “Allowed Prefixes” parameter, as previously described.

### Advertising IPv6 prefixes to AWS
<a name="advertising-ipv6-prefixes-to-aws"></a>

 In terms of advertising prefixes from your on-premises facility to AWS, there are no CIDR restrictions, though standard Direct Connect quotas apply. Any prefix advertised is local to your AWS network and not propagated beyond its boundary.

 **Public VIF IPv6 peerings** — As with transit and private VIF peerings, public IPv6 peerings are allocated /125s from AWS owned ranges automatically. These IPs are used to support the BGP peering, and you need to use your own IPv6 prefixes to communicate over the peering.

**Note**
 With IPv4 public VIFs, it’s possible to use the AWS assigned public IPv4 /31 in combination with NAT to enable access from privately addressed on-premises resources (to support use cases where you are not in a position to provide public IPv4 address space). With IPv6, however, you must own and specify an IPv6 prefix at creation. Note that if you specify an IPv6 prefix that you don’t provably own, the VIF will fail to provision and remain in the “verifying” state.

### Routing IPv6 over public and private or transit VIFs
<a name="routing-ipv6-over-public-and-private-or-transit-vifs"></a>

 If you’re using AWS-assigned CIDR blocks for the VPCs, or BYOIPv6 with CIDRs that are marked as *advertisable* by AWS, you will receive over the public VIF peering the summary prefixes that contain the CIDRs of your VPCs. When using public VIFs in conjunction with private/transit VIFs, take into account that your device will receive the same prefixes (the ones for your VPCs) over both types of VIFs. At this point, route filtering on your customer device needs to be taken into consideration, to ensure symmetric flow of traffic over the different virtual interfaces.

![This is a diagram that shows Direct Connect dual-stack support](https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/direct-connect-dual-stack-support.png)

## Amazon-managed VPN
<a name="amazon-managed-vpn"></a>

 AWS Site-to-Site VPN connectivity configuration comprises multiple parts:
+  The customer gateway, which is the logical representation of the on-premises VPN end point
+  The VPN connection
+  The local device configuration on the VPN appliance, represented by the customer gateway

 Any AWS S2S VPN connection consists of two tunnels. It is this connection that defines the IP addressing, ISAKMP, IPsec, and BGP peering parameters.

 **Note:** AWS supports IPv6 for IPsec tunnels terminating in Transit Gateway VPN attachments only.

### Customer gateways
<a name="customer-gateways"></a>

 While AWS supports IPv6 within IPsec tunnels, the underlying connectivity occurs via IPv4. This means that both the AWS and customer VPN terminating devices need to be addressable via public IPv4 addresses. On the AWS side, this IP is automatically allocated from the AWS Region’s public EC2 IP space. On the customer side, this means you require an internet reachable IPv4 address for your appliance.

### VPN connections
<a name="vpn-connections"></a>

 A single VPN connection can carry IPv4 or IPv6 traffic, but not both at the same time. When configuring a connection, you specify either IPv4 or IPv6 for use inside the tunnel. You are free to choose this address, or let Amazon generate it. If you choose to specify a CIDR, it has to be a `/126` taken from the unique-local address range `fd00::/8`. If you don’t specify one Amazon selects a `/128` from this range for you. In either case, the Amazon side of the connection is the first and your side the second usable IPv6 address in the subnet.

 Another element to consider are the local and remote IPv6 Network CIDR ranges. These can either be `::/0` or specific prefixes. This configuration defines the IPsec Phase 2 Security Association (SA) that can be negotiated. If you specify a prefix, be sure to configure your customer gateway appliance to negotiate this accordingly.

**Note**
Even if you specify a `/126`, the console displays the IPv6 tunnel CIDR as a `/128`. While an IPv4 address is always configured, traffic on this range will not be able to flow, as the SA settings specified only permit negotiating the IPv6 SA.

### Customer gateway configuration
<a name="customer-gateway-configuration"></a>

 For device-specific configuration of the customer gateway, AWS recommends you consult the vendor’s documentation on how to set up IPv6 VPNs. There are vendor-independent nuances to IPv6 S2S VPNs not present in IPv4, and the remainder of this section outlines these.

 AWS provides generated configurations for IPsec to download, but currently this covers only IPv4 configuration. Some settings and configuration parameters are independent of IP protocol version. However, settings related to tunnel addressing, phase 2 SA negotiation, and peering configuration do differ.

 When using the AWS templates, be sure to omit IPv4 specific parts, and replace them with the IPv6 equivalents.

 When specifying the local and remote CIDRs, make sure to configure your VPN appliance to negotiate the IPsec Phase 2 SA to match the AWS side. If you want to use BGP rather than static routing on the VPN and use LOCAL REMOTE CIDR ranges to scope the Phase 2 SA, then the P2P IPs must be included in the CIDR block. As a result, it is only possible to delimit SA scope if using `fd00::/8` on both sides of the VPN, and if non-unique local addressing is used, the SA has to be negotiated as `::/0`.

 When using an AWS-generated tunnel IP, or specifying a `/128` CIDR range establishment of the BGP, peering will fail by default. The reason is that a `/128`, like a `/32` in IPv4, is a host route. You will need to define a static route pointing at the AWS side of the tunnel to establish the BGP peering.

![This is a diagram that shows AWS VPN dual-stack configuration.](https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/aws-vpn-dual-stack-configuration.png)
