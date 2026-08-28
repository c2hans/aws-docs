---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cw-loggroup-retention-period-check.html
---

# cw-loggroup-retention-period-check
<a name="cw-loggroup-retention-period-check"></a>

Checks if an Amazon CloudWatch LogGroup retention period is set to greater than 365 days or else a specified retention period. The rule is NON\_COMPLIANT if the retention period is less than `MinRetentionTime`, if specified, or else 365 days.

**Note**
If the retention setting is "Never expire" for a log group, the rule is marked as COMPLIANT.

**Identifier:** CW\_LOGGROUP\_RETENTION\_PERIOD\_CHECK

**Resource Types:** AWS::Logs::LogGroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

LogGroupNames (Optional)Type: CSV
A comma-separated list of Log Group name prefixes to check the retention period.

MinRetentionTime (Optional)Type: int
Specify the retention time in days. Valid values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653. The default retention period is 365 days.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d437c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
