---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-audit-logging-enabled.html
---

# redshift-audit-logging-enabled
<a name="redshift-audit-logging-enabled"></a>

Checks if Amazon Redshift clusters are logging audits to a specific bucket. The rule is NON\_COMPLIANT if audit logging is not enabled for a Redshift cluster or if the '`bucketNames`' parameter is provided but the audit logging destination does not match.

**Identifier:** REDSHIFT\_AUDIT\_LOGGING\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

bucketNames (Optional)Type: CSV
Comma-separated list of Amazon S3 bucket names for storing audit logs.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1291c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
