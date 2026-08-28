---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-cancel-key-deletion.html
---

# `AWSConfigRemediation-CancelKeyDeletion`
<a name="automation-aws-cancel-key-deletion"></a>

 **Description**

 The `AWSConfigRemediation-CancelKeyDeletion` runbook cancels deletion of the AWS Key Management Service (AWS KMS) customer managed key that you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-CancelKeyDeletion)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.
+ KeyId

  Type: String

  Description: (Required) The ID of the customer managed key that you want to cancel deletion for.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `kms:CancelKeyDeletion`
+  `kms:DescribeKey`

 **Document Steps**
+  `aws:executeAwsApi` - Cancels deletion for the customer managed key you specify in the `KeyId` parameter.
+  `aws:assertAwsResourceProperty` - Confirms key deletion is disabled on your customer managed key.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
