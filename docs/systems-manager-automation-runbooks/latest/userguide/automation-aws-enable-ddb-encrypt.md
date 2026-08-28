---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-ddb-encrypt.html
---

# `AWSConfigRemediation-EnableEncryptionOnDynamoDbTable`
<a name="automation-aws-enable-ddb-encrypt"></a>

 **Description**

 The `AWSConfigRemediation-EnableEncryptionOnDynamoDbTable` runbook encrypts an Amazon DynamoDB (DynamoDB) table using the AWS Key Management Service (AWS KMS) customer managed key you specify for the `KMSKeyId` parameter.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableEncryptionOnDynamoDbTable)

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
+ KMSKeyId

  Type: String

   Description: (Required) The ARN of the customer managed key you want to use to encrypt the DynamoDB table you specify in the `TableName` parameter.
+ TableName

  Type: String

  Description: (Required) The name of the DynamoDB table you want to encrypt.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `dynamodb:DescribeTable`
+  `dynamodb:UpdateTable`

 **Document Steps**
+  `aws:executeAwsApi` - Encrypts the DynamoDB table you specify in the `TableName` parameter.
+  `aws:waitForAwsResourceProperty` - Verifies the `Enabled` property for the DynamoDB table's `SSESpecification` is set to `true` .
+  `aws:assertAwsResourceProperty` - Verifies the DynamoDB table is encrypted with the customer managed key specified in the `KMSKeyId` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
