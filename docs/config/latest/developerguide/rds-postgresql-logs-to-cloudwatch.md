---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/rds-postgresql-logs-to-cloudwatch.html
---

# rds-postgresql-logs-to-cloudwatch
<a name="rds-postgresql-logs-to-cloudwatch"></a>

Checks if an Amazon PostgreSQL DB instance is configured to publish logs to Amazon CloudWatch Logs. The rule is NON\_COMPLIANT if the DB instance is not configured to publish logs to Amazon CloudWatch Logs.

**Identifier:** RDS\_POSTGRESQL\_LOGS\_TO\_CLOUDWATCH

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Canada West (Calgary) Region

**Parameters:**

logTypes (Optional)Type: CSV
Comma-separated list of log types to be published to CloudWatch Logs. Valid values are: 'postgresql', 'upgrade'. Default value is 'postgresql'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1273c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
