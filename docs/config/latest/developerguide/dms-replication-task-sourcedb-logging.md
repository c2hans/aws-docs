---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-task-sourcedb-logging.html
---

# dms-replication-task-sourcedb-logging
<a name="dms-replication-task-sourcedb-logging"></a>

Checks if logging is enabled with a valid severity level for AWS DMS replication tasks of a source database. The rule is NON\_COMPLIANT if logging is not enabled or logs for DMS replication tasks of a source database have a severity level that is not valid.

**Identifier:** DMS\_REPLICATION\_TASK\_SOURCEDB\_LOGGING

**Resource Types:** AWS::DMS::ReplicationTask

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d479c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
