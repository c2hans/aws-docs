---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment.html
---

# Set up DNS resolution for hybrid networks in a multi-account AWS environment
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment"></a>

*Anvesh Koganti, Amazon Web Services*

## Summary
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-summary"></a>

This pattern provides a comprehensive solution for setting up DNS resolution in hybrid network environments that include multiple Amazon Web Services (AWS) accounts. It enables bidirectional DNS resolution between on-premises networks and the AWS environment through Amazon Route 53 Resolver endpoints. The pattern presents two solutions to enable DNS resolution in a [multi-account, centralized architecture](https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/scaling-dns-management-across-multiple-accounts-and-vpcs.html#multi-account-centralized):
+ *Basic setup* doesn't use Route 53 Profiles. It helps optimize costs for small to medium deployments of lower complexity.
+ *Enhanced setup* uses Route 53 Profiles to simplify operations. It is best for larger or more complex DNS deployments.

**Note**
Review the *Limitations* section for service limitations and quotas before implementation. Consider factors such as management overhead, costs, operational complexity, and team expertise when you make your decision.

## Prerequisites and limitations
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-prereqs"></a>

**Prerequisites **
+ An AWS multi-account environment with Amazon Virtual Private Cloud (Amazon VPC) deployed across Shared Services and workload accounts (preferably set up through [AWS Control Tower by following AWS best practices](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html) for account structure).
+ Existing hybrid connectivity (AWS Direct Connect or AWS Site-to-Site VPN) between your on-premises network and the AWS environment.
+ Amazon VPC peering, AWS Transit Gateway, or AWS Cloud WAN for Layer 3 network connectivity between VPCs. (This connectivity is required for application traffic. It is not required for DNS resolution to work. DNS resolution operates independently of network connectivity between the VPCs.)
+ DNS servers running in the on-premises environment.

**Limitations**
+ Route 53 Resolver endpoints, rules, and Profiles are Regional constructs and might require replication in multiple AWS Regions for global organizations.
+ For a comprehensive list of service quotas for Route 53 Resolver, private hosted zones, and Profiles, see [Quotas](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html) in the Route 53 documentation.

## Architecture
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-architecture"></a>

**Target technology stack  **
+ Route 53 outbound and inbound endpoints
+ Route 53 Resolver rules for conditional forwarding
+ AWS Resource Access Manager (AWS RAM)
+ Route 53 private hosted zone

**Target architecture **

**Outbound and inbound endpoints**

The following diagram shows the DNS resolution flow from AWS to on premises. This is the connectivity setup for outbound resolutions where the domain is hosted on premises. Here is a high-level overview of the process involved in setting this up. For details, see the [Epics](#set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-epics) section.

1. Deploy outbound Route 53 Resolver endpoints in the Shared Services VPC.

1. Create Route 53 Resolver rules (forwarding rules) in the Shared Services account for domains that are hosted on premises.

1. Share and associate the rules with VPCs in other accounts that host resources that need to resolve on-premises hosted domains. This can be done in different ways depending on your use case, as described later in this section.

![Inbound and outbound endpoints in an AWS to on premises DNS resolution flow.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01e700cd-be8c-4a5d-bc89-b901a260d045/images/d69d4cad-5e2c-4481-9370-2708e8a4f8c1.png)

After you set up connectivity, the steps involved in the outbound resolution are as follows:

1. The Amazon Elastic Compute Cloud (Amazon EC2) instance sends a DNS resolution request for `db.onprem.example.com` to the VPC's Route 53 Resolver at the VPC\+2 address.

1. Route 53 Resolver checks the Resolver rules and forwards the request to the on-premises DNS server IPs by using the outbound endpoint.

1. The outbound endpoint forwards the request to the on-premises DNS IPs. The traffic goes over the established hybrid network connectivity between the Shared Services VPC and the on-premises data center.

1. The on-premises DNS server responds back to the outbound endpoint, which then forwards the response back to the VPC's Route 53 Resolver. The Resolver returns the response to the EC2 instance.

The next diagram shows the DNS resolution flow from the on-premises environment to AWS. This is the connectivity setup for inbound resolutions where the domain is hosted on AWS. Here is a high-level overview of the process involved in setting this up. For details, see the [Epics](#set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-epics) section.

1. Deploy inbound Resolver endpoints in the Shared Services VPC.

1. Create private hosted zones in the Shared Services account (centralized approach).

1. Associate the private hosted zones with the Shared Services VPC. Share and associate these zones with cross-account VPCs for VPC-to-VPC DNS resolution. This can be done in different ways depending on your use case, as described later in this section.

![Inbound and outbound endpoints in an on premises to AWS DNS resolution flow.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01e700cd-be8c-4a5d-bc89-b901a260d045/images/a6f5348c-2041-453e-8939-2b4ee0b7ebd8.png)

After you set up connectivity, the steps involved in the inbound resolution are as follows:

1. The on-premises resource sends a DNS resolution request for `ec2.prod.aws.example.com` to the on-premises DNS server.

1. The on-premises DNS server forwards the request to the inbound Resolver endpoint in the Shared Services VPC over the hybrid network connection.

1. The inbound Resolver endpoint looks up the request in the associated private hosted zone with the help of the VPC Route 53 Resolver and gets the appropriate IP address.

1. These IP addresses are sent back to the on-premises DNS server, which returns the response to the on-premises resource.

This configuration enables on-premises resources to resolve AWS private domain names by routing queries through the inbound endpoints to the appropriate private hosted zone. In this architecture, private hosted zones are centralized in a Shared Services VPC, which allows for central DNS management by a single team. These zones can be associated with many VPCs to address the VPC-to-VPC DNS resolution use case. Alternatively, you might want to delegate DNS domain ownership and management to each AWS account. In that case, each account manages its own private hosted zones and associates each zone with the central Shared Services VPC for a unified resolution with the on-premises environment. This decentralized approach is outside the scope of this pattern. For more information, see [Scaling DNS management across multiple accounts and VPCs](https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/scaling-dns-management-across-multiple-accounts-and-vpcs.html) in the *Hybrid Cloud DNS Options for Amazon VPC* whitepaper.

When you establish the fundamental DNS resolution flows by using Resolver endpoints, you need to determine how to manage the sharing and association of Resolver rules and private hosted zones across your AWS accounts. You can approach this in two ways: through self-managed sharing by using AWS RAM to share Resolver rules and direct private hosted zone associations, as detailed in the *Basic setup* section, or through Route 53 Profiles, as discussed in the *Enhanced setup* section. The choice depends on your organization's DNS management preferences and operational requirements. The following architecture diagrams illustrate a scaled environment that includes multiple VPCs across different accounts, which represents a typical enterprise deployment.

**Basic setup**

In basic setup, the implementation for hybrid DNS resolution in a multi-account AWS environment uses AWS RAM to share Resolver forwarding rules and private hosted zone associations to manage DNS queries between on-premises and AWS resources. This method uses centralized Route 53 Resolver endpoints in a Shared Services VPC that's connected to your on-premises network to handle both inbound and outbound DNS resolution efficiently.
+ For outbound resolution, Resolver forwarding rules are created in the Shared Services account and then shared with other AWS accounts by using AWS RAM. This sharing is limited to accounts within the same Region. The target accounts can then associate these rules with their VPCs and enable the resources in those VPCs to resolve on-premises domain names.
+ For inbound resolution, private hosted zones are created in the Shared Services account and associated with the Shared Services VPC. These zones can then be associated with VPCs in other accounts by using the Route 53 API, AWS SDKs, or the AWS Command Line Interface (AWS CLI). The resources in associated VPCs can then resolve DNS records defined in the private hosted zones, which creates a unified DNS view across your AWS environment.

The following diagram shows DNS resolution flows in this basic setup.

![Using basic setup for hybrid DNS resolution in a multi-account AWS environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01e700cd-be8c-4a5d-bc89-b901a260d045/images/258e4bcd-e9c6-43b5-bab8-856ca22206b9.png)

This setup works well when you work with DNS infrastructure on a limited scale. However, it can become challenging to manage as your environment grows. The operational overhead of managing how private hosted zone and Resolver rules are shared and associated with VPCs individually increases significantly with scale. Additionally, service quotas such as the 300 VPC association limit per private hosted zone can become constraining factors in large-scale deployments. Enhanced setup addresses these challenges.

**Enhanced setup**

Route 53 Profiles offer a streamlined solution for managing DNS resolution in hybrid networks across multiple AWS accounts. Instead of managing private hosted zones and Resolver rules individually, you can group DNS configurations into a single container that can be easily shared and applied across multiple VPCs and accounts in a Region. This setup maintains the centralized Resolver endpoint architecture in a Shared Services VPC while significantly simplifying the management of DNS configurations.

The following diagram shows DNS resolution flows in an enhanced setup.

![Using advanced setup with Route 53 Profiles for hybrid DNS resolution in a multi-account AWS environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/01e700cd-be8c-4a5d-bc89-b901a260d045/images/55b9681d-ddb4-4a55-b4ec-fc9afa9870fa.png)

Route 53 Profiles let you package private hosted zone associations, Resolver forwarding rules, and DNS firewall rules into a single, shareable unit. You can create Profiles in the Shared Services account and share them with member accounts by using AWS RAM. When a profile is shared and applied to target VPCs, all necessary associations and configurations are automatically handled by the service. This significantly reduces the operational overhead of DNS management and provides excellent scalability for growing environments.

**Automation and scale**

Use infrastructure as code (IaC) tools such as CloudFormation or Terraform to automatically provision and manage Route 53 Resolver endpoints, rules, private hosted zones, and Profiles. Integrate DNS configuration with continuous integration and continuous delivery (CI/CD) pipelines for consistency, repeatability, and rapid updates.

## Tools
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-tools"></a>

**AWS services**
+ [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you securely share your resources across AWS accounts to reduce operational overhead and provide visibility and auditability.
+ [Amazon Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) responds recursively to DNS queries from AWS resources and is available by default in all VPCs. You can create Resolver endpoints and conditional forwarding rules to resolve DNS namespaces between your on-premises data center and your VPCs.
+ [Amazon Route 53 private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) is a container that holds information about how you want Route 53 to respond to DNS queries for a domain and its subdomains.
+ [Amazon Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html) allow you to apply and manage DNS-related Route 53 configurations across many VPCs and in different AWS accounts in a simplified manner.

## Best practices
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-best-practices"></a>

This section provides some of the best practices for optimizing Route 53 Resolver. These represent a subset of Route 53 best practices. For a comprehensive list, see [Best practices for Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices.html).

**Avoid loop configurations with Resolver endpoints**
+ Design your DNS architecture to prevent recursive routing by carefully planning VPC associations. When a VPC hosts an inbound endpoint, avoid associating it with Resolver rules that could create circular references.
+ Use AWS RAM strategically when you share DNS resources across accounts to maintain clean routing paths.

For more information, see [Avoid loop configurations with Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoints.html) in the Route 53 documentation.

**Scale Resolver endpoints**
+ For environments that require a high number of queries per second (QPS), be aware that there is a limit of 10,000 QPS per ENI in an endpoint. More ENIs can be added to an endpoint to scale DNS QPS.
+ Amazon CloudWatch provides `InboundQueryVolume` and `OutboundQueryVolume` metrics (see the [CloudWatch documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-resolver-with-cloudwatch.html)). We recommend that you set up monitoring rules that alert you if the threshold exceeds a certain value (for example, 80 percent of 10,000 QPS).
+ Configure stateful security group rules for Resolver endpoints to prevent connection tracking limits from causing DNS query throttling during high-volume traffic. To learn more about how connection tracking works in security groups, see [Amazon EC2 security group connection tracking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html) in the Amazon EC2 documentation.

For more information, see [Resolver endpoint scaling](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-scaling.html) in the Route 53 documentation.

**Provide high availability for Resolver endpoints**
+ Create inbound endpoints with IP addresses in at least two Availability Zones for redundancy.
+ Provision additional network interfaces to ensure availability during maintenance or traffic surges.

For more information, see [High availability for Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoint-high-availability.html) in the Route 53 documentation.

## Epics
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-epics"></a>

### Deploy Route 53 Resolver endpoints
<a name="deploy-r53r-endpoints"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy an inbound endpoint. | Route 53 Resolver uses the inbound endpoint to receive DNS queries from on-premises DNS resolvers. For instructions, see [Forwarding inbound DNS queries to your VPCs ](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html)in the Route 53 documentation. Make a note of the inbound endpoint IP address. | AWS administrator, Cloud administrator |
| Deploy an outbound endpoint. | Route 53 Resolver uses the outbound endpoint to send DNS queries to on-premises DNS resolvers. For instructions, see [Forwarding outbound DNS queries to your network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html) in the Route 53 documentation. Make a note of the output endpoint ID. | AWS administrator, Cloud administrator |

### Configure and share Route 53 private hosted zones
<a name="configure-and-share-r53-private-hosted-zones"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a private hosted zone for a domain that’s hosted on AWS. | This zone holds the DNS records for resources in an AWS-hosted domain (for example, `prod.aws.example.com`) that should be resolved from the on-premises environment. For instructions, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) in the Route 53 documentation.<br />When you create a private hosted zone, you must associate a VPC with the hosted zone owned by the same account. Select the Shared Services VPC for this purpose. | AWS administrator, Cloud administrator |
| Basic setup: Associate the private hosted zone with VPCs in other accounts. | If you're using basic setup (see the [Architecture](#set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-architecture) section):<br />To enable resources in the member account VPCs to resolve DNS records in this private hosted zone, you must associate your VPCs with the hosted zone. You must authorize the association and then make the association programmatically. For instructions, see [Associating an Amazon VPC and a private hosted zone that you created with different AWS accounts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html) in the Route 53 documentation. | AWS administrator, Cloud administrator |
| Enhanced setup: Configure and share Route 53 Profiles. | If you're using enhanced setup (see the [Architecture](#set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-architecture) section):1. Create a Route 53 Profile and associate the relevant private hosted zones with it. For instructions, see [Creating Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-create.html) in the Route 53 documentation.<br />2. Use AWS RAM to share the profile with member accounts and then associate the shared profile with target VPCs. For instructions, see [Sharing a Route 53 Profile](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sharing-profiles.html#sharing-share) and [Associate a Route 53 Profile to VPCs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-associate-vpcs.html) in the Route 53 documentation.Depending on your organization's structure and DNS requirements, you might need to create and manage multiple Profiles for different accounts or workloads. | AWS administrator, Cloud administrator |

### Configure and share Route 53 Resolver forwarding rules
<a name="configure-and-share-r53r-forwarding-rules"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a forwarding rule for a domain that’s hosted on premises. | This rule will instruct Route 53 Resolver to forward any DNS queries for on-premises domains (such as `onprem.example.com`) to on-premises DNS resolvers. To create this rule, you need the IP addresses of the on-premises DNS resolvers and the outbound endpoint ID. For instructions, see [Creating forwarding rules ](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing-creating-rules.html)in the Route 53 documentation. | AWS administrator, Cloud administrator |
| Basic setup: Share and associate the forwarding rule with your VPCs in other accounts. | If you're using basic setup:<br />For the forwarding rule to take effect, you must share and associate the rule with your VPCs in other accounts. Route 53 Resolver then takes the rule into consideration when it resolves a domain. For instructions, see [Sharing Resolver rules with other AWS accounts and using shared rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing-sharing.html) and [Associating forwarding rules with a VPC ](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing-associating-rules.html)in the Route 53 documentation. | AWS administrator, Cloud administrator |
| Enhanced setup: Configure and share Route 53 Profiles. | If you're using enhanced setup:1. If you've already created a Route 53 Profile in the previous steps, you can use the same Profile. If not, create a Route 53 Profile and associate relevant Resolver forwarding rules with it. For instructions, see [Creating Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-create.html) in the Route 53 documentation.<br />2. Use AWS RAM to share the profile with member accounts, and then associate the shared profile with target VPCs. For instructions, see [Sharing a Route 53 Profile](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/sharing-profiles.html#sharing-share) and [Associate a Route 53 Profile to VPCs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-associate-vpcs.html) in the Route 53 documentation.Depending on your organization's structure and DNS requirements, you might need to create and manage multiple Profiles for different accounts or workloads. | AWS administrator, Cloud administrator |

### Configure on-premises DNS resolvers for AWS integration
<a name="configure-on-premises-dns-resolvers-for-aws-integration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Configure conditional forwarding in the on-premises DNS resolvers. | For DNS queries to be sent to AWS from the on-premises environment for resolution, you must configure conditional forwarding in the on-premises DNS resolvers to point to the inbound endpoint IP address. This instructs the DNS resolvers to forward all DNS queries for the AWS-hosted domain (for example, for `prod.aws.example.com`) to the inbound endpoint IP address for resolution by Route 53 Resolver.  | Network administrator |

### Verify end-to-end DNS resolution in a hybrid environment
<a name="verify-end-to-end-dns-resolution-in-a-hybrid-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test DNS resolution from AWS to the on-premises environment. | From an instance in a VPC that has the forwarding rule associated with it, perform a DNS query for an on-premises hosted domain (for example, for `db.onprem.example.com`). | Network administrator |
| Test DNS resolution from the on-premises environment to AWS. | From an on-premises server, perform DNS resolution for an AWS-hosted domain (for example, for `ec2.prod.aws.example.com`). | Network administrator |

## Related resources
<a name="set-up-dns-resolution-for-hybrid-networks-in-a-multi-account-aws-environment-resources"></a>
+ [Hybrid Cloud DNS Options for Amazon VPC](https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/hybrid-cloud-dns-options-for-vpc.html) (AWS whitepaper)
+ [Working with private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) (Route 53 documentation)
+ [Getting started with Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) (Route 53 documentation)
+ [Simplify DNS management in a multi-account environment with Route 53 Resolver](https://aws.amazon.com/blogs/security/simplify-dns-management-in-a-multiaccount-environment-with-route-53-resolver/) (AWS blog post)
+ [Unify DNS management using Amazon Route 53 Profiles with multiple VPCs and AWS accounts](https://aws.amazon.com/blogs/aws/unify-dns-management-using-amazon-route-53-profiles-with-multiple-vpcs-and-aws-accounts/) (AWS blog post)
+ [Migrating your multi-account DNS environment to Amazon Route 53 Profiles](https://aws.amazon.com/blogs/networking-and-content-delivery/migrating-your-multi-account-dns-environment-to-amazon-route-53-profiles/) (AWS blog post)
+ [Using Amazon Route 53 Profiles for scalable multi-account AWS environments](https://aws.amazon.com/blogs/networking-and-content-delivery/using-amazon-route-53-profiles-for-scalable-multi-account-aws-environments/) (AWS blog post)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
