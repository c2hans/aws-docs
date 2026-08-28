---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deletedynamodbtablebackups.html
---

# `AWS-DeleteDynamoDbTableBackups`
<a name="automation-aws-deletedynamodbtablebackups"></a>

 **Description**

Delete DynamoDB table backups based on retention days or count.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DeleteDynamoDbTableBackups)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ LambdaAssumeRole

  Type: String

  Description: (Optional) The ARN of the role that allows Lambda created by Automation to perform the actions on your behalf. If not specified a transient role will be created to run the Lambda function.
+ RetentionCount

  Type: String

  Default: 10

  Description: (Optional) The number of backups to retain for the table. If more than the specified number of backup exist, the oldest backups beyond that number are deleted. Either RetentionCount or RetentionDays can be used, not both.
+ RetentionDays

  Type: String

  Description: (Optional) The number of days to retain backups for the table. Backups older than the specified number of days are deleted. Either RetentionCount or RetentionDays can be used, not both.
+ TableName

  Type: String

  Description: (Required) Name of the DynamoDB table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
