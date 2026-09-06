---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/scaling-dns-management-across-multiple-accounts-and-vpcs.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scaling DNS management across multiple accounts and VPCs
<a name="scaling-dns-management-across-multiple-accounts-and-vpcs"></a>

 In alignment with AWS best practices, many organizations build out a cloud environment with multiple accounts. Whether you’re using shared VPCs with multiple accounts hosted in a single VPC to share resources, or using the more traditional model where a VPC is tied to a single account, there are architectural considerations to make. This whitepaper focuses on the more traditional model.

 For more information on Shared VPCs, refer to [*Share your VPC with other accounts*](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html).

 While having multiple accounts and VPCs helps provide a reduction of blast radius and granular account-level billing, it can make DNS infrastructure more complex. The Route 53 ability to associate PHZs with VPCs and accounts helps reduce these complexities for both centralized and decentralized architectures. We discuss both centralized and decentralized design paradigms in this section.

## Multi-account centralized
<a name="multi-account-centralized"></a>

 In this type of architecture, Route 53 PHZs are centralized in a shared services VPC. This allows for central DNS management while enabling inbound Route 53 resolver endpoints to natively query the PHZs. This leaves the need for VPC-to-VPC DNS resolution unaddressed. Fortunately, PHZs can be associated with many VPCs. A simple command line interface (CLI) or API request can associate each PHZ with VPCs in accounts outside of the shared services VPC.

 For more information about cross-account PHZ sharing, refer to [Associating an Amazon VPC and a private hosted zone that you created with different AWS accounts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html).

![A diagram depicting a multi-account centralized DNS with Private Hosted Zone sharing.](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/images/centralized-dns.png)

1.  Instances within a VPC use the Route 53 Resolver (Amazon-provided DNS).

1.  PHZs are associated with a shared services VPC.

1.  PHZs are also associated with other VPCs in the environment.

1.  Conditional forward rule(s) from the on-premises DNS servers have an inbound Route 53 Resolver endpoint as their destination.

1.  Rule(s) for on-premises domain names are created that use an outbound Route 53 Resolver endpoint.

 While this architecture includes centralization, you might require each VPC to have its own fully qualified domain name (FQDN) hosted within each account, so that account owners can change and modify their own DNS records. The next section provides more information on how this design paradigm is accomplished.

## Multi-account decentralized
<a name="multi-account-decentralized"></a>

 An organization might want to delegate DNS ownership and management to each AWS account. Advantages of this method include decentralization of control and isolating the blast radius for failure to a specific account. The ability to associate PHZs to VPCs between accounts again becomes useful in this scenario. Each VPC can have its own PHZ(s) and then associate it with multiple other VPCs, across accounts and across Regions. This architecture is depicted in the following diagram. For unified resolution with the on-premises environment, this requires only that the shared services VPC be associated with each VPC hosting a PHZ.

![A diagram depicting multi-account DNS decentralized.](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/images/dns-decentralized.png)

1.  EC2 instances within a VPC use the Route 53 Resolver (Amazon-provided DNS).

1.  PHZs are associated with a shared services VPC.

1.  PHZs are also associated with other VPCs in the environment.

1.  Conditional forward rules from the on-premises DNS servers have an inbound Route 53 Resolver endpoint as their destination.

1.  Create rules for on-premises domain names that use an outbound Route 53 Resolver endpoint.

## Alternative approaches
<a name="alternative-approaches"></a>

 Alternative approaches have historically been to deploy DNS proxy servers in EC2 instances or to reply on Active Directory DNS servers. This centralization was desired, but did not take advantage of the benefits of using the Route 53 Resolver, and can cause scaling and availability constraints.

 A common anti-pattern is to use Route 53 Resolver endpoints to centralize the management of DNS within a shared services VPC or Transit Gateway. This is done by creating both an inbound and an outbound endpoint in the shared services VPC, then creating forwarding rules whose target is the IP address of the inbound endpoint in the centralized VPC. These rules are then associated with other VPCs, which use the inbound endpoint of the central VPC to resolve their DNS queries. This has the effect of allowing spoke VPCs to use the DNS view of the central VPC. For example, if you have an EFS mount in the central VPC, the spoke VPC can resolve the EFS mount’s DNS name by forwarding its query to the inbound endpoint of the VPC where the file system is mounted.

 This approach is not preferred. Cross-account sharing of PHZs is highly available and less costly than query forwarding. This is because PHZ sharing preserves Availability Zone isolation, meaning that your queries in VPC A are answered by an Availability Zone local to VPC A, whereas your queries in VPC B are answered by an Availability Zone local to VPC B. This means that, in the event of an availability problem in VPC A, VPC B's queries would not be affected, as long as they are in two different Availability Zones. There is no additional cost to associate a PHZ with a VPC and you can share a VPC with upwards of 1000 zones.

 Query forwarding is optimized for sending queries to other DNS resolvers located outside the AWS network. It provides a way to allow DNS resolvers from different networks to access each other when they would normally not be visible via a recursive DNS lookup. If you choose to use query forwarding to resolve DNS answers local to another VPC, you would must get an endpoint for every VPC for which you want this view of DNS. Additionally, using endpoints to answer queries between VPCs breaks the previously mentioned Availability Zone isolation. This means that instead of each VPC resolving queries within its local Availability Zone, you have now made several VPCs dependent on the availability of a single VPC.

 Regarding limits, each endpoint ENI has a limit of 10,000 QPS, but keep in mind that if you want to use an endpoint to centralize DNS management, you are forwarding more query volume to a central VPC instead of distributing the query load between multiple VPCs. This anti-pattern is generally not recommended.
