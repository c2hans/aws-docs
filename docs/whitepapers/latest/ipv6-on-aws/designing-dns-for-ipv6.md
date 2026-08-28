---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/designing-dns-for-ipv6.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Designing DNS for IPv6
<a name="designing-dns-for-ipv6"></a>

 The core concept of DNS is unchanged from IPv4. From a Layer 3 perspective, DNS is just another application, and therefore, by virtue of the OSI/ISO model provided abstraction, agnostic to the chosen network layer protocol.

 Regardless of the IP version, there is a deep link between DNS and the IP layer. The DNS specification has adapted and introduced an additional type to accommodate IPv6 addresses. In IPv6 the equivalent of the IPv4 “A” records are AAAA records. This means that it is possible to use IPv4 as the network protocol to connect to a DNS server and resolve an IPv6 (AAAA) record.

## PTR records
<a name="ptr-records"></a>

 A pointer (PTR) record translates an IP address to its domain name. IPv6 addresses are reverse mapped under the domain IP6.ARPA. IPv6 reverse maps use a sequence of nibbles separated by dots with the suffix “.IP6.ARPA” as defined in RFC 3596. For example, the reverse lookup domain name corresponding to the address `2001:db8:1234:1a00:1:2:3:4` would be `4.0.0.0.3.0.0.0.2.0.0.0.1.0.0.0.0.0.a.1.4.3.2.1.8.b.d.0.1.0.0.2.ip6.arpa`.

## Alias records
<a name="alias-records"></a>

 [Amazon Route 53](https://aws.amazon.com/route53/) supports alias records. Route 53 alias records are mapped internally to the DNS name of alias targets such as AWS resources. Route 53 monitors the IP address associated with an alias target's DNS name for scaling actions and software updates. The authoritative response from Route 53 name servers contains an A record (for IPv4 addresses) or AAAA record (for IPv6 addresses) with the IP address of the alias target.

## DNS resolution within a host
<a name="dns-resolution-within-a-host"></a>

 External configuration aside it is up to a host’s networking stack at runtime to resolve DNS records. When configured as dual-stack, most modern operating systems default to** **preferring IPv6. In other words, when a query for a FQDN returns both an A and AAAA record the OS prefers to use the AAAA record and establishes IPv6 connectivity to the target.

**Note**
It is up to an IPv6 enabled host’s operating system and network stack whether it will attempt to map a given FQDN to an IPv4 or IPv6 address. Ensure that IPv6-enabled hosts are able to resolve AAAA records, and that the network between it and its destination is routable to IPv6. A commonly observed misconfiguration in dual-stack setups is hosts resolving FQDNs to IPv6 addresses, but no end-to-end IPv6 routable path existing between source and destination. [Happy Eyeballs ](https://datatracker.ietf.org/doc/html/rfc6555)(Fast Fallback) is an algorithm published by the IETF which can make dual-stack applications (those that understand both IPv4 and IPv6) more responsive to users by attempting to connect using both IPv4 and IPv6 at the same time (preferring IPv6). This avoids the usual problems faced by users with imperfect IPv6 connections or setups.

## Amazon Route 53 DNS records
<a name="amazon-route-53-dns-records"></a>

 In AWS, [Amazon Route 53](https://aws.amazon.com/route53/) provides DNS capabilities. Route 53 provides features for two use cases:
+  Public DNS for externally hosted content
+  DNS capability within a VPC both from a resolver and authoritative name server standpoint

## Public IPv6 DNS resolution
<a name="public-ipv6-dns-resolution"></a>

 For externally queryable DNS, you can use Route 53 public hosted zones, with both A and AAAA records. Route 53 health checks support health checking IPv6 services. The name servers exist both for IPv4 and IPv6, meaning clients wanting to resolve a FQDN hosted on Route 53 public hosted zone can do so natively.

## DNS resolution within a VPC
<a name="dns-resolution-within-a-vpc"></a>

 Amazon VPC comes with Route 53 Resolver, which provides a built-in capability for resolving DNS names. This resolver is reachable either on `169.254.169.253` or `VPC_CIDR_NETWORK + 2` for IPv4 and `fd00:ec2::253` for Nitro-based IPv6 hosts. Requests sent to this resolver are resolved against the combination of private hosted zones associated with the VPC, and any (shared) resolver rules. For more information, refer to [Resolving DNS queries between VPCs and your network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html).

 **Note:** By default, a VPC’s DHCP option set will specify these VPC Route 53 DNS resolvers to DHCP clients. However, if you don’t want to use AWS provided DNS resolvers, you can change the DHCP options to point clients at self-hosted or third-party DNS resolvers.

## Private DNS resolution
<a name="private-dns-resolution"></a>

 Amazon Route 53 can be configured to act as an authoritative name server for one or more zones. You can configure this by creating Private Hosted Zones (PHZs) and associating it with one or more VPCs. Route 53 supports the creation of AAAA records so that it can be used to resolve FQDNs to IPv6 addresses.

 For more information, refer to [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html).

## DNS64 and NAT64
<a name="dns64-and-nat64"></a>

### DNS64
<a name="dns64"></a>

 Your IPv6-only workloads running in VPCs can only send and receive IPv6 network packets. Without DNS64, a DNS query for an IPv4-only service will yield an IPv4 destination address in response and your IPv6-only client cannot communicate with it. To bridge this communication gap, you can enable DNS64 for a subnet and it applies to all the AWS resources within that subnet. With DNS64, the Amazon Route 53 Resolver looks up the DNS record for the service you queried for and does one of the following:
+  If the record contains an IPv6 address, it returns the original record and the connection is established without any translation over IPv6.
+  If there is no IPv6 address associated with the destination in the DNS record, the Route 53 Resolver synthesizes one by prepending the well-known /96 prefix, defined in [RFC 6052](https://datatracker.ietf.org/doc/html/rfc6052) (`64:ff9b::/96`), to the IPv4 address in the record. Your IPv6-only client sends network packets to the synthesized IPv6 address. You will then need to route this traffic to the NAT gateway, which performs the necessary translation on the traffic to allow IPv6 clients in your subnet to access IPv4 services outside that subnet.

 DNS64 is a subnet-level setting, which you can enable or disable on IPv6-only subnets using the [modify-subnet-attribute](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-nat64-dns64-walkthrough) using the AWS CLI or with the VPC console. DNS64 works in conjunction with NAT64, which comes built into the Amazon VPC NAT Gateway service.

### NAT64
<a name="nat64"></a>

 NAT64 enables your IPv6-only clients in Amazon VPCs to communicate with IPv4-only services in the same VPC (in different subnets), or connected VPCs, in your on-premises networks, or the internet. NAT64 is automatically available on your existing NAT gateways or on any new NAT gateways you create. It's not a feature you enable or disable. Once you have enabled DNS64 and your IPv6-only service sends network packets to the synthesized IPv6 address through the NAT gateway, the following happens:
+  From the `64:ff9b::/96` prefix, the NAT gateway recognizes that the original destination is IPv4 and translates the IPv6 packets to IPv4 by replacing:
  +  Source IPv6 with its own private IPv4, which is translated to the Elastic IP address by the internet gateway.
  +  Destination IPv6 to IPv4 by truncating the `64:ff9b::/96` prefix.
+  The NAT gateway sends the translated IPv4 packets to the destination through the internet gateway, VPC peering, virtual private gateway, or transit gateway, and initiates a connection.
+  The IPv4-only host sends back IPv4 response packets. Once a connection is established, NAT gateway accepts the response IPv4 packets from the external hosts.
+  The response IPv4 packets are destined for NAT gateway, which receives the packets and de-NATs them by replacing its IP (destination IP) with the host’s IPv6 address and prepending back `64:ff9b::/96` to the source IPv4 address. The packet then flows to the host following the local route.

 The NAT gateway enables your IPv6-only workloads in an Amazon VPC subnet to communicate with IPv4-only services anywhere outside the subnet.

![This is a diagram that shows DNS64 and NAT64.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/dns64-and-nat64.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
