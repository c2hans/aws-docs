---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/kinesis-stream-backup-retention-check.html
---

# kinesis-stream-backup-retention-check
<a name="kinesis-stream-backup-retention-check"></a>

Checks if an Amazon Kinesis Data Stream has its data record retention period set to a specific number of hours. The rule is NON\_COMPLIANT if the property `RetentionPeriodHours` is set to a value less than the value specified by the parameter.

**Identifier:** KINESIS\_STREAM\_BACKUP\_RETENTION\_CHECK

**Resource Types:** AWS::Kinesis::Stream

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Israel (Tel Aviv), Canada West (Calgary) Region

**Parameters:**

minimumBackupRetentionPeriod (Optional)Type: String
Minimum hours data records should be retained. Valid values are 24 to 8760, default value is 168.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1045c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
