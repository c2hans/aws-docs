---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-meets-restore-time-target.html
---

# dynamodb-meets-restore-time-target
<a name="dynamodb-meets-restore-time-target"></a>

Checks if the restore time of Amazon DynamoDB Tables meets the specified duration. The rule is NON\_COMPLIANT if LatestRestoreExecutionTimeMinutes of a DynamoDB Table is greater than maxRestoreTime minutes.

**Identifier:** DYNAMODB\_MEETS\_RESTORE\_TIME\_TARGET

**Resource Types:** AWS::DynamoDB::Table

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

maxRestoreTimeType: int
Numerical value for the maximum allowed restore runtime.

resourceTags (Optional)Type: String
Tags of the DynamoDB Tables for the rule to check, in JSON format.

resourceId (Optional)Type: String
Name of DynamoDB Table for the rule to check.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d503c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
