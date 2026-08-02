---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/aws-cloud-wan.html
---

# AWS Cloud WAN
<a name="aws-cloud-wan"></a>

 AWS Cloud WAN is a new way to connect networks together that we were previously able to do with Transit Gateways, VPC Peering, and IPSEC VPN tunnels. Previously you would configure one or more VPCs, connect them together with one of the previous methods, and use IPSEC VPN or Direct Connect to connect to on-premises networks. You would have your network and security posture constructs defined in one place, and your networks in another. Cloud WAN allows you to centralize all of these constructs in a single place. By policy, you can segment your networks to determine who can talk to who, and isolate production traffic via these segments from development or test workloads, or your on premises networks.

![A diagram depicting AWS Cloud WAN connectivity](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/cloud-wan-diagram.png)

 Manage your global network through the AWS Network Manager user interface and APIs. The global network is the root-level container for all your network objects; the core network is the part of your global network managed by AWS. A core network policy (CNP) is a single versioned policy document that defines all aspects of your core network. Attachments are any connections or resources you wand to add to your core network. A core network edge (CNE) is a local connection point for attachments that comply with the policy. Network segments are routing domains which, by default, allow communication only within a segment.

 To use CloudWAN:

1.  In AWS Network Manager, create a global network and associated core network.

1.  Create a CNP that defines segments, ASN range, AWS Regions and tags to be used to attach to segments.

1.  Apply the network policy.

1.  Share the core network with your users, accounts, or organizations using the resource access manager.

1.  Create and tag attachments.

1.  Update routes in your attached VPCs to include the core network.

 Cloud WAN was designed to simplify the process of connecting your AWS infrastructure globally. It allows you to segment traffic with a centralized permissions policy and use your existing infrastructure at your company locations. Cloud WAN also connects your VPCs, SD-WANs, Client VPNs, firewalls, VPNs, and data center resources to connect to Cloud WAN. For more information, see [AWS Cloud WAN blog posts](https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/aws-cloud-wan/).

 AWS Cloud WAN enables a unified network connecting cloud and on-premises environments. Organizations use next-gen firewalls (NGFWs) and intrusion prevention systems (IPSs) for security. The [AWS Cloud WAN and Transit Gateway migration and interoperability patterns](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-cloud-wan-and-aws-transit-gateway-migration-and-interoperability-patterns/) blog post describes architectural patterns for centrally managing and inspecting outbound network traffic in a Cloud WAN network, including single-Region and multi-Region networks, and configures route tables. These architectures ensure data and applications remain safe while maintaining a secure cloud environment.

 For more information about Cloud WAN, see the [Centralized outbound inspection architecture in AWS Cloud WAN](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-outbound-inspection-architecture-in-aws-cloud-wan/) blog post.
