---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/vpc-design.html
---

# VPC design
<a name="vpc-design"></a>

## Design guidelines
<a name="design-guidelines"></a>

 Deploy WorkSpaces Applications into a dedicated VPC. When designing the WorkSpaces Applications VPC, size for forecasted growth. Reserve IP address capacity for new use cases, and additional Availability Zones (AZs) that may be added at a later time. A fundamental design point of WorkSpaces Applications is that only one user can consume a WorkSpaces Applications instance. When allocating IP space, think one user as one IP address per WorkSpaces Applications instance. With WorkSpaces Applications, it is possible for a user to consume multiple WorkSpaces Applications instances. Therefore, planning IP space must also account for use cases that require additional WorkSpaces Applications instances.

 Although the maximum size of a VPC Classless Inter-Domain Routing (CIDR) is /16, AWS recommends not over-allocating private IP addresses. It is possible to extend the [*size of the VPC through additional CIDRs*](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#vpc-resize), but there is a limit to this; therefore, allocate what is needed from the onset.

 If the WorkSpaces Applications deployment is joined to an Active Directory domain, the [*DHCP options set*](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) for the VPC must have the domain DNS configured. The domain name server should specify the DNS IP addresses that are either authoritative for the Active Directory domain, or the DNS should forward DNS requests to the authoritative DNS instances for the Active Directory domain. Also, the VPC must have `enableDnsHostnames` and `EnableDnsSupport` configured.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
