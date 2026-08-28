---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/planning-ipv6-adoption-in-the-aws-cloud-network.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Planning IPv6 adoption in the AWS Cloud network
<a name="planning-ipv6-adoption-in-the-aws-cloud-network"></a>

 Elastic network interfaces in an IP network could operate in three different modes:
+  **IPv4-only mode** — Your resources can communicate over IPv4, and if communicating to IPv6 nodes, require an interoperability layer.
+  **IPv6-only mode** — Your resources can communicate over IPv6, they do not require an IPv4 address, and if they are communicating to IPv4 nodes, they require an interoperability layer achieved through NAT64 and DNS64.
+  **Dual-stack mode** — Your resources can communicate over both IPv4 and IPv6. A separate interoperability layer is not required.

## IPv6 addressing plan on AWS
<a name="ipv6-addressing-plan-on-aws"></a>

 Coming up with an IPv6 addressing plan is one of the most important initial tasks for any organization proceeding with IPv6 adoption. For most organizations, IPv6 is deployed in parallel with IPv4 in existing IPv4 AWS and hybrid networks. IPv4 addressing plans tend to grow over time, and consequently may be highly fragmented, not contiguous, or not big enough. Simply duplicating the IPv4 addressing scheme in some fashion in IPv6 might initially prove advantageous. However, any temporary advantage gained by such a shortcut will ultimately be surpassed by the ease and efficiency of operation and design offered by a proper IPv6 addressing plan that incorporates the key benefits of the larger allocations possible with IPv6.

 The virtually limitless scale of the IPv6 address space allows for an addressing plan no longer constrained by the scarcity of IPv4 addresses. Techniques like Variable Length Subnet Masking (VLSM) (previously required in IPv4 to economically match subnet size to host count on a given network segment) can be seen as unnecessary and obsolete in IPv6. Instead, it’s possible to adopt a consistent addressing plan by assigning significance to groups of VPCs according to network and segmentation needs.

 In AWS, IPv6 address space assigned to VPCs is assigned from the *globally unique unicast* address range. There are two options for IPv6 address assignment:
+  AWS-assigned IPv6 VPC classless inter-domain routings (CIDRs)
+  Bring your own IPv6 CIDR Blocks (BYOIPv6)

**Note**
[Amazon VPC now supports unique local address (ULA) CIDRs and private global unicast addresses (GUA).](https://aws.amazon.com/about-aws/whats-new/2024/08/aws-private-ipv6-addressing-vpcs-subnets/)

 **Amazon VPC IP Address Manager (IPAM)**

 Amazon VPC IPAM is a VPC feature that makes it easier for you to plan, track, and monitor IP addresses for your AWS workloads. You can also use IPAM's automated workflows to more efficiently manage both IPv4 and IPv6 addresses. With IPAM, you can track and have an inventory of the AWS-supplied IPv6, and you can also have granular control over your IPv6 prefixes configured in AWS with the Bring Your Own IPv6 (BYOIPv6) feature. Choosing AWS-assigned IPv6 addresses or BYOIPv6 addresses influences your ability to summarize prefixes, as well as to control the multi-account, multi-region addressing scheme. For more information, refer to [IPAM documentation](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) and the [Managing IP pools across VPCs and Regions using Amazon VPC IP Address Manager](https://aws.amazon.com/blogs/networking-and-content-delivery/managing-ip-pools-across-vpcs-and-regions-using-amazon-vpc-ip-address-manager/) blog post.

## AWS-assigned IPv6 VPC CIDR
<a name="aws-assigned-ipv6-vpc-cidr"></a>

 By default, Amazon provides one fixed size (/56) IPv6 CIDR block to a VPC. This range is assigned by the service, and consequently, you can’t assign contiguous IPv6 CIDR blocks to VPCs in the same Region or based on other custom-defined criteria.

 For customers that have a large VPC footprint in AWS and prefer to use IP route summarization to simplify their overall environment, bring your own IPv6 (BYOIPv6) described, in the next section, may be the preferred solution.

## BYOIPv6 VPC CIDR
<a name="byoipv6-vpc-cidr"></a>

 Alternatively, if you own an IPv6 address space, you can import it into AWS using the Bring Your Own IPv6 service. The smallest IPv6 address range that you can bring is /48 for CIDRs that are publicly advertised by AWS, and /56 for CIDRs that are not publicly advertised by AWS. You can also choose to bring a /48 and mark it as non-advertisable, keeping control of IP advertisements on your on-premises setup. After importing it, you can assign /56 ranges from the space to individual VPCs in the same account.

 For the process on how to “Bring Your Own IP (BYOIP),” refer to [Configure your BYOIP address range](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-requirements).

 As summarization can be easily configured with contiguous IPv6 blocks, for multi-Region deployments, you can bring one or more /48 or larger prefixes to each Region. Consider route summarization at the VPC route table level, as well as when using AWS connectivity options such as [AWS Transit Gateway](https://aws.amazon.com/transit-gateway), [AWS Direct Connect](https://aws.amazon.com/directconnect/), and [Site-to-Site VPN](https://aws.amazon.com/vpn/).

## VPC subnet addressing
<a name="vpc-subnet-addressing"></a>

 Although you can assign one /56 IPv6 CIDR block to a VPC, the VPC subnets are /64 fixed in length. This yields to the interface ID being /64 in length, in accordance with the general format of the IPv6 unicast addresses. Given the fixed size of the VPC CIDR and the subnet prefix, you have 8 bits for subnet allocation in the VPC, enabling you to create 256 subnets in the VPC. You can allocate IPv6 /64 CIDRs to dual-stack subnets (which allow you to run both IPv4 and IPv6 workloads), and to IPv6-only subnets (which allow you to run IPv6-only enabled resources).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
