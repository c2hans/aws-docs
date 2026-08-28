---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshot-encrypted.html
---

# rds-snapshot-encrypted
<a name="rds-snapshot-encrypted"></a>

Checks if Amazon Relational Database Service (Amazon RDS) DB snapshots are encrypted. The rule is NON\_COMPLIANT if the Amazon RDS DB snapshots are not encrypted.

**Identifier:** RDS\_SNAPSHOT\_ENCRYPTED

**Resource Types:** AWS::RDS::DBClusterSnapshot, AWS::RDS::DBSnapshot

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1283c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
