---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/aurora-mysql-cluster-audit-logging.html
---

# aurora-mysql-cluster-audit-logging
<a name="aurora-mysql-cluster-audit-logging"></a>

Checks if Amazon Aurora MySQL DB clusters have audit logging enabled. The rule is NON\_COMPLIANT if a DB cluster does not have audit logging enabled.

**Identifier:** AURORA\_MYSQL\_CLUSTER\_AUDIT\_LOGGING

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d225c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
