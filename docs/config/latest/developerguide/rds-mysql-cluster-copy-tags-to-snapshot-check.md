---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-mysql-cluster-copy-tags-to-snapshot-check.html
---

# rds-mysql-cluster-copy-tags-to-snapshot-check
<a name="rds-mysql-cluster-copy-tags-to-snapshot-check"></a>

Checks if Amazon Relational Database Service (Amazon RDS) MySQL DB clusters are configured to copy tags to snapshots. The rule is NON\_COMPLIANT if an Amazon RDS MySQL DB cluster is not configured to copy tags to snapshots.

**Identifier:** RDS\_MYSQL\_CLUSTER\_COPY\_TAGS\_TO\_SNAPSHOT\_CHECK

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), US West (N. California), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1265c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
