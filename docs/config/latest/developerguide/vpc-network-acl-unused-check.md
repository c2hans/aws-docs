---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/vpc-network-acl-unused-check.html
---

# vpc-network-acl-unused-check
<a name="vpc-network-acl-unused-check"></a>

Checks if there are unused network access control lists (network ACLs). The rule is COMPLIANT if each network ACL is associated with a subnet. The rule is NON\_COMPLIANT if a network ACL is not associated with a subnet.

**Identifier:** VPC\_NETWORK\_ACL\_UNUSED\_CHECK

**Resource Types:** AWS::EC2::NetworkAcl

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1605c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
