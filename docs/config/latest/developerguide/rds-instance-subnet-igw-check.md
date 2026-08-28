---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-subnet-igw-check.html
---

# rds-instance-subnet-igw-check
<a name="rds-instance-subnet-igw-check"></a>

Checks if RDS DB instances are deployed in a public subnet with a route to the internet gateway. The rule is NON\_COMPLIANT if RDS DB instances is deployed in a public subnet

**Identifier:** RDS\_INSTANCE\_SUBNET\_IGW\_CHECK

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1251c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
