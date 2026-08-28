---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-cluster-iam-authentication-enabled.html
---

# rds-cluster-iam-authentication-enabled
<a name="rds-cluster-iam-authentication-enabled"></a>

Checks if an Amazon Relational Database Service (Amazon RDS) cluster has AWS Identity and Access Management (IAM) authentication enabled. The rule is NON\_COMPLIANT if an Amazon RDS Cluster does not have IAM authentication enabled.

**Identifier:** RDS\_CLUSTER\_IAM\_AUTHENTICATION\_ENABLED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1231c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
