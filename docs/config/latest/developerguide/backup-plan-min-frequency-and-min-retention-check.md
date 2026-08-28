---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/backup-plan-min-frequency-and-min-retention-check.html
---

# backup-plan-min-frequency-and-min-retention-check
<a name="backup-plan-min-frequency-and-min-retention-check"></a>

Checks if a backup plan has a backup rule that satisfies the required frequency and retention period. The rule is NON\_COMPLIANT if recovery points are not created at least as often as the specified frequency or expire before the specified period.

**Identifier:** BACKUP\_PLAN\_MIN\_FREQUENCY\_AND\_MIN\_RETENTION\_CHECK

**Resource Types:** AWS::Backup::BackupPlan

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

requiredFrequencyValue (Optional)Type: intDefault: 1
Numerical value for required backup frequency. Maximum of 24 for hours, 31 for days.

requiredRetentionDays (Optional)Type: intDefault: 35
Required retention period in days.

requiredFrequencyUnit (Optional)Type: StringDefault: days
Unit of time for required backup frequency. Accepted values: 'hours', 'days'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d247c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
