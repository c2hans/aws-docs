---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createdynamodbbackup.html
---

# `AWS-CreateDynamoDBBackup`
<a name="automation-aws-createdynamodbbackup"></a>

 **Description**

Create a backup of an Amazon DynamoDB table.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateDynamoDBBackup)

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
+ BackupName

  Type: String

  Description: (Required) Name of the backup to create.
+ LambdaAssumeRole

  Type: String

  Description: (Optional) The ARN of the role that allows Lambda created by Automation to perform the actions on your behalf. If not specified a transient role will be created to run the Lambda function.
+ TableName

  Type: String

  Description: (Required) Name of the DynamoDB table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
