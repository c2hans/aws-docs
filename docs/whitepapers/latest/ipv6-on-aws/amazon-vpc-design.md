---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/amazon-vpc-design.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon VPC design
<a name="amazon-vpc-design"></a>

 Planning and implementing network connectivity in AWS is usually one of the foundational tasks you perform when deploying workloads in AWS. Following are some of the aspects typically considered:
+  Amount and nature of Amazon VPCs required
+  Amazon VPC CIDR range and IP address allocation including Bring Your Own IP (BYOIP) for public connectivity
+  Number and type of subnets
+  Number of availability zones to cover
+  Permitted traffic paths
+  Internet incoming and outgoing traffic options
+  Hybrid connectivity
+  Inter-VPC connectivity
+  Scalability and expansion

 Although most of these aspects apply equally to both IPv4 and IPv6, existing literature is mostly written in the context of IPv4 only. This section augments these existing resources by providing IPv6 specifics. AWS recommends you read the existing, IPv4-centric material first to get the most out of this content.

## VPC IP address assignment
<a name="vpc-ip-address-assignment"></a>

 Your VPC can operate in dual-stack mode—your resources can communicate over IPv4, IPv6, or both. IPv4 and IPv6 communication are independent of each other. You cannot disable IPv4 support for your VPC, but you can have IPv6-only subnets in your dual-stack VPC. To enable dual-stack operation for your VPC, you can associate up to five IPv6 CIDR block ranges per VPC.

### Subnet address assignment
<a name="subnet-address-assignment"></a>

 After you have associated an IPv6 prefix to a VPC, you can begin to assign one /64 IPv6 prefix to each subnet. Note that these assignments are configured on a per-subnet basis, and it’s possible to have a mix of dual-stack IPv6, IPv4-only, and IPv6-only subnets within the same VPC. This is useful in scenarios where you require IPv6 capability for a subset of the network as described in the drivers for adoption section, and you need to maintain dual-stack and backwards-compatible deployments in the same VPC.

 The address assignment of resource within a subnet occurs at two levels:
+  The Amazon VPC elastic network interface construct configuration
+  A resource’s networking stack configuration

### IP addressing of the elastic network interface
<a name="ip-addressing-of-the-elastic-network-interface"></a>

 Network-addressable resources deployed within a VPC must have an elastic network interface. Examples of resources include:
+  [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instances
+  Interface VPC endpoints
+  [AWS Lambda](https://aws.amazon.com/lambda/) functions (deployed in VPCs)
+  [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) database instances

 Elastic network interfaces are logical constructs in the VPC which represent a resource’s network adapter at runtime. Each elastic network interface may have one or more IPv4 addresses as well as one or more IPv6 addresses. This means you are not required to provision separate elastic network interfaces for IPv4 and IPv6, and there is no need to configure additional elastic network interfaces on your workloads to enable IPv6.

 An elastic network interface placed into an IPv6 enabled subnet may be created with and modified to have an IPv6 address assigned. You can configure this behavior per elastic network interface, and you can choose to either have AWS auto assign one for you or specify an unused address in the subnet’s allocated range. In either case, the address configured remains constant throughout the elastic network interface’s life unless explicitly modified.

![This is a diagram that shows a dual-stack Amazon VPC with two availability zones and four subnets.](http://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/dual-stack-amazon-VPC.png)

### IP addressing at the resource’s networking stack
<a name="ip-addressing-at-the-resources-networking-stack"></a>

 In IPv4, the preferred method for assigning IPv4 addresses is to use Dynamic Host Configuration Protocol (DHCP). DHCP is based on IPv4’s broadcast mechanism that allows hosts to announce themselves to DHCP servers. These servers can then offer an IP address lease to the client. IPv6 has no concept of broadcast (refer to the [Brief IPv6 overview](brief-ipv6-overview.md) section of this document) and initially did not feature DHCP capability. However, the community has become used to DHCP, and so [RFC 8415](https://datatracker.ietf.org/doc/html/rfc8415) was developed to introduce DHCPv6. In the absence of broadcast capability, DHCPv6 makes use of the well-known multicast address for all DHCP servers/relays, `ff02::1:2`.

 Amazon VPC has built in support for address assignment via DHCP for both IPv4 and IPv6. Address allocation works similar to static address reservation in traditional DHCP servers: the IP address assigned to the elastic network interface construct determines the IP address the VPC DHCP infrastructure offers the resource requesting an address. Amazon VPC also offers the ability to configure DHCP option sets which can be used to provide additional configuration information such as domain name or DNS servers to use. In a dual-stack design all IP addresses used in an option set need to be IPv4.

**Note**
Be aware that if you’re trying to add IPv6 to an existing or migrated workload, the host OS may not yet be set up to use DHCPv6. Consult the [documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html#vpc-migrate-ipv6-dhcpv6) to learn how to enable and verify DHCPv6 operation for your chosen operating system. Also, for the IPv6-only EC2 instances in IPv6-only subnets, you need to verify that the OS and AMI you’re using can operate under the specific conditions, without an IPv4 address from the VPC CIDR(s).

**Note**
The use of DHCP is optional, and you may statically configure the host OS with an IP address. However, the VPC anti-spoofing mechanism enforces the IP address configured on the network interface controller (NIC) to match the one configured on the underlying elastic network interface. AWS recommends enabling DHCP, even for resources that require static IP addresses, and managing static IP assignment at the elastic network interface level.

 The EC2 instances launched in IPv6-only subnets and the Elastic Network Interfaces (ENIs) attached to them are also assigned IPv6 addresses through the DHCPv6 options set, from the IPv6 CIDR block of your subnet. These instances do not require private IPv4 addresses to be assigned.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
