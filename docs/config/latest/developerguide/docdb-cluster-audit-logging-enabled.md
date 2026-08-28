---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/docdb-cluster-audit-logging-enabled.html
---

# docdb-cluster-audit-logging-enabled
<a name="docdb-cluster-audit-logging-enabled"></a>

Checks if an Amazon DocumentDB (with MongoDB compatibility) instance cluster has CloudWatch log export enabled for audit logs. The rule is NON\_COMPLIANT if an Amazon DocumentDB instance cluster does not have CloudWatch log export enabled for audit logs.

**Identifier:** DOCDB\_CLUSTER\_AUDIT\_LOGGING\_ENABLED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Europe (Stockholm), Middle East (Bahrain), China (Beijing), Asia Pacific (Jakarta), Africa (Cape Town), Asia Pacific (Osaka), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), US West (N. California), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d485c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
