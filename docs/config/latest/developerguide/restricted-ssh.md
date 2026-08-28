---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html
---

# restricted-ssh
<a name="restricted-ssh"></a>

**Important**
For this rule, the rule identifier (INCOMING\_SSH\_DISABLED) and rule name (restricted-ssh) are different.

Checks if the incoming SSH traffic for the security groups is accessible. The rule is COMPLIANT if the IP addresses of the incoming SSH traffic in the security groups are restricted (CIDR other than 0.0.0.0/0 or ::/0). Otherwise, NON\_COMPLIANT.

**Identifier:** INCOMING\_SSH\_DISABLED

**Resource Types:** AWS::EC2::SecurityGroup

**Trigger type:** Configuration changes and Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d969c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
