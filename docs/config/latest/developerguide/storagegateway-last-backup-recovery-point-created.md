---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/storagegateway-last-backup-recovery-point-created.html
---

# storagegateway-last-backup-recovery-point-created
<a name="storagegateway-last-backup-recovery-point-created"></a>

Checks if a recovery point was created for AWS Storage Gateway volumes. The rule is NON\_COMPLIANT if the Storage Gateway volume does not have a corresponding recovery point created within the specified time period.

**Identifier:** STORAGEGATEWAY\_LAST\_BACKUP\_RECOVERY\_POINT\_CREATED

**Resource Types:** AWS::StorageGateway::Volume

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

resourceTags (Optional)Type: String
Tags of Storage Gateway volumes for the rule to check, in JSON format `{"tagkey" : "tagValue"}`.

resourceId (Optional)Type: String
ID of Storage Gateway volume for the rule to check.

recoveryPointAgeValue (Optional)Type: intDefault: 1
Numerical value for maximum allowed age. No more than 744 for hours, 31 for days.

recoveryPointAgeUnit (Optional)Type: StringDefault: days
Unit of time for maximum allowed age. Accepted values: 'hours', 'days'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1559c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
