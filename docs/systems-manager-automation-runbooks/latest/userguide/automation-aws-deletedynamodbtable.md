---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-deletedynamodbtable.html
---

# `AWSConfigRemediation-DeleteDynamoDbTable`
<a name="automation-aws-deletedynamodbtable"></a>

 **Description**

 The `AWSConfigRemediation-DeleteDynamoDbTable` runbook deletes the Amazon DynamoDB (DynamoDB) table you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteDynamoDbTable)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ TableName

  Type: String

  Description: (Required) The name of the DynamoDB table you want to delete.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `dynamodb:DeleteTable`
+  `dynamodb:DescribeTable`

 **Document Steps**
+  `aws:executeScript` - Deletes the DynamoDB table specified in the `TableName` parameter.
+  `aws:executeScript` - Verifies the DynamoDB table has been deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
