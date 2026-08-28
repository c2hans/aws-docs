---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/virtualmachine-last-backup-recovery-point-created.html
---

# virtualmachine-last-backup-recovery-point-created
<a name="virtualmachine-last-backup-recovery-point-created"></a>

Checks if a recovery point was created for AWS Backup-Gateway VirtualMachines. The rule is NON\_COMPLIANT if an AWS Backup-Gateway VirtualMachines does not have a corresponding recovery point created within the specified time period.

**Identifier:** VIRTUALMACHINE\_LAST\_BACKUP\_RECOVERY\_POINT\_CREATED

**Resource Types:** AWS::BackupGateway::VirtualMachine

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

resourceTags (Optional)Type: String
Tags of AWS Backup-Gateway VirtualMachines for the rule to check, in JSON format `{"tagkey" : "tagValue"}`.

resourceId (Optional)Type: String
ID of AWS Backup-Gateway VirtualMachine for the rule to check.

recoveryPointAgeValue (Optional)Type: intDefault: 1
Numerical value for maximum allowed age. No more than 744 for hours, 31 for days.

recoveryPointAgeUnit (Optional)Type: StringDefault: days
Unit of time for maximum allowed age. Accepted values: 'hours', 'days'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1593c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
