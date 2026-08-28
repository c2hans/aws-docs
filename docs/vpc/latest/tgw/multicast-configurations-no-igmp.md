---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/multicast-configurations-no-igmp.html
---

# Example: Manage static source configurations in AWS Transit Gateway
<a name="multicast-configurations-no-igmp"></a>

This example statically adds multicast sources to a group. Hosts do not use the IGMP protocol to join or leave multicast groups. You need to statically add the group members that receive the multicast traffic.

 Use the following steps to complete the configuration:

1. Create a VPC. For more information, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the *Amazon VPC User Guide*.

1. Create a subnet in the VPC. For more information, see [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) in the *Amazon VPC User Guide*.

1. Create a transit gateway configured for multicast traffic. For more information, see [Create a transit gateway in AWS Transit Gateway](create-tgw.md).

1. Create a VPC attachment. For more information, see [Create a VPC attachment in AWS Transit Gateway](create-vpc-attachment.md).

1. Create a multicast domain configured for no IGMP support, and support for statically adding sources. For more information, see [Create a static source multicast domain in AWS Transit Gateway](create-tgw-domain.md).

   Use the following settings:
   + Disable **IGMPv2 support**.
   + To manually add sources, enable **Static sources support**.

     The sources are the only resources that can send multicast traffic when the attribute is enabled. Otherwise, any instances that are in subnets associated with the multicast domain can send multicast traffic, and the group members receive the multicast traffic.

1. Create an association between subnets in the transit gateway VPC attachment and the multicast domain. For more information see [Associating VPC attachments and subnets with a multicast domain in AWS Transit Gateway](associate-attachment-to-domain.md).

1. If you enable **Static sources support**, add the source to the multicast group. For more information, see [Register sources with a multicast group in AWS Transit Gateway](add-source-multicast-group.md).

1. Add the members to the multicast group. For more information, see [Register members with a multicast group in AWS Transit Gateway](add-members-multicast-group.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
