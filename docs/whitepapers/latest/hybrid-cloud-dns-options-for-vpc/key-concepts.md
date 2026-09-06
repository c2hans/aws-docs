---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/key-concepts.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Key concepts
<a name="key-concepts"></a>

 Before we dive into the solutions, it is important to establish a few concepts and configuration options that we’ll reference throughout this whitepaper.

## Amazon VPC DHCP options set
<a name="amazon-vpc-dhcp-options-set"></a>

 The Dynamic Host Configuration Protocol (DHCP) provides a standard for passing configuration information to hosts on a TCP/IP network. The options field of a DHCP message contains configuration parameters such as `domain-name-servers`, `domain- name`, `ntp-servers`, and `netbios-node-type`. In any Amazon VPC, you can create DHCP options sets and specify up to four DNS servers. Currently, these options sets are created and applied per VPC, which means that you can’t have a DNS server list at the Availability Zone level.

 For more information about DHCP options sets and configuration, refer to the [overview of DHCP option sets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html#DHCPOptionSets) in the Amazon VPC Developer Guide.

## Amazon Route 53 Resolver
<a name="amazon-route-53-resolver"></a>

 Route 53 Resolver, also known as the [Amazon DNS Server](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html#AmazonDNS) or Amazon Provided DNS, provides full public DNS resolution, with additional resolution for internal records for the VPC and customer-defined Route 53 private DNS records. Route 53 Resolver maps to a DNS server running on a reserved IP address at the base of the VPC network range, plus two. For example, the DNS Server on a `10.0.0.0/16` network is located at `10.0.0.2`. For VPCs with multiple Classless Inter-Domain Routing (CIDR) blocks, the DNS server IP address is located in the primary CIDR block.

## Elastic Network Interfaces (ENIs)
<a name="elastic-network-interfaces-enis"></a>

 Elastic network interfaces (referred to as *network interfaces* in the Amazon EC2 console) are virtual network interfaces that you can attach to an instance in a VPC. They’re available only for instances running in a VPC. A virtual network interface, like any network adapter, is the interface that a device uses to connect to a network. Each instance in a VPC, depending on the instance type, can have multiple network interfaces attached to it.

 For more information, refer to [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide for Linux Instances*.

### How ENIs work for Route 53 Resolver
<a name="how-enis-work-for-route-53-resolver"></a>

 A Route 53 Resolver endpoint is made up of one or more ENIs, which reside in your VPC. Each endpoint can only forward queries in a single direction.

 *Inbound endpoints* are available as forwarding targets for DNS resolvers and use an IP address from the subnet space of the VPC to which it is attached. Queries forwarded to these endpoints have the DNS view of the VPC to which the endpoints are attached.

 That means that if there are names local to the VPC, such as AWS PrivateLink endpoints, EFS clusters, EKS clusters, PHZs associated, and so on, the query can resolve any of those names. This is also true for any VPCs peered with the VPC that owns the endpoint.

 *Outbound endpoints* serve as the path through which all queries are forwarded out of the VPC. Outbound endpoints are directly attached to the owner VPC and indirectly associated with other VPCs by rules. Therefore, if a forwarding rule is shared with VPC that does not own the outbound endpoint, all queries that match the forwarding rule pass through to the owner VPC and then forward out. It is important to realize this when you use queries to forward from one VPC to another. The outbound endpoint might reside in an entirely different Availability Zone than the VPC that originally sent the query, and there is potential for an Availability Zone outage in the owner VPC to impact query resolution in the VPC using the forwarding rule. This can be avoided by deploying outbound endpoints in multiple Availability Zones.

![A diagram depicting Route 53 Resolver with outbound endpoint.](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/images/outbound-endpoint.jpeg)

 Refer to [Getting Starting with Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) in the *Amazon Route 53 Developer Guide* for more information.

### Route 53 PHZ
<a name="route-53-phz"></a>

 A Route 53 PHZ is a container that holds DNS records that are visible to one or more VPCs. VPCs can be associated to the PHZ at the time of or after the creation of the PHZ.

 For more information, refer to [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) in the *Amazon Route 53 Developer Guide*.

### Connection tracking
<a name="connection-tracking"></a>

 By default, Amazon EC2 security groups use [connection tracking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#security-group-connection-tracking) to track information about traffic to and from the instance. Security group rules are applied based on the connection state of the traffic to determine if the traffic is allowed or denied. This allows security groups to be *stateful*, which means that responses to inbound traffic are allowed to flow out of the instance regardless of outbound security group rules, and vice-versa.

### Linux resolver
<a name="linux-resolver"></a>

 The stub resolver in Linux is responsible for initiating and sequencing DNS queries that ultimately lead to a full resolution. A resolver is configured through a configuration file, `/etc/resolv.conf`. The resolver queries the DNS server listed in the `resolv.conf` in the order they are listed.

 The following is an example resolv.conf:

```
options timeout:1 nameserver 10.0.0.10
nameserver 10.0.1.10
```

### Linux DHCP client
<a name="linux-dhcp-client"></a>

 The Dynamic Host Configuration Protocol (DHCP) client on Linux provides the option to customize the set of DNS servers that the instance uses for DNS resolution. The DNS servers provided in the AWS DHCP options are picked up by this DHCP client to further update the resolv.conf with a list of DNS Server IP addresses. In addition, you can use the *supersede* DHCP client option to replace the DNS servers provided by the AWS DHCP options set with a static list of DNS servers. You do this by modifying the DHCP client configuration file, `/etc/dhcp/dhclient.conf`:

```
interface "eth0"
{
supersede domain-name-servers 10.0.2.10, 10.0.3.10;
}
```

 This example statement replaces DNS servers `10.0.0.10` and `10.0.1.10` in the resolv.conf sample with `10.0.2.10` and `10.0.3.10`. We discuss the use of this option in the [*Zonal forwarders using supersede*](decentralized-conditional-forwarders.md#zonal-forwarders-using-supersede) solution.

### Conditional forwarder: unbound
<a name="conditional-forwarder-unbound"></a>

 A conditional forwarder examines the DNS queries received from instances and forwards them to different DNS servers based on rules set in its configuration, typically using the domain name of the query to select the forwarder. In a hybrid architecture, conditional forwarders play a vital role to bridge name resolution between on-premises and cloud resources. For this particular solution we use *unbound*, which is conditional forwarder and a recursive and caching DNS resolver. Depending on your requirements, this option can act as an alternative or hybrid to forwarding rules in Amazon Route 53 Resolver.

 For instructions on how to set up an Unbound DNS server, refer to the [How to Set Up DNS Resolution Between On-Premises Networks and AWS by Using Unbound](https://aws.amazon.com/blogs/security/how-to-set-up-dns-resolution-between-on-premises-networks-and-aws-by-using-unbound/) blog post in the AWS Security Blog.

 The following is an example `unbound.conf`:

```
forward-zone:
name: "."
forward-addr: 10.0.0.2 # Amazon Provided DNS forward-zone:
name: "example.corp"
forward-addr: 192.168.1.10 # On-premises DNS
```

 In this example, configuration queries to `example.corp` are forwarded to the on-premises DNS server, and the rest are forwarded to Route 53 Resolver.
