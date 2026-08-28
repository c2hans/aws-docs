---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-cluster-multi-az-enabled.html
---

# rds-cluster-multi-az-enabled
<a name="rds-cluster-multi-az-enabled"></a>

Checks if Multi-Availability Zone (Multi-AZ) replication is enabled on Amazon Aurora and Multi-AZ DB clusters managed by Amazon Relational Database Service (Amazon RDS). The rule is NON\_COMPLIANT if an Amazon RDS instance is not configured with Multi-AZ.

**Identifier:** RDS\_CLUSTER\_MULTI\_AZ\_ENABLED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1233c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
