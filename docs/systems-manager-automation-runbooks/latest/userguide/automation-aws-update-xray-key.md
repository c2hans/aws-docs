---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-update-xray-key.html
---

# `AWSConfigRemediation-UpdateXRayKMSKey`
<a name="automation-aws-update-xray-key"></a>

 **Description**

 The `AWSConfigRemediation-UpdateXRayKMSKey` runbook enables encryption on your AWS X-Ray data using an AWS Key Management Service (AWS KMS) key. This runbook should only be used as a baseline to ensure that your AWS X-Ray data is encrypted according to minimum recommended security best practices. We recommend encrypting multiple sets of data with different KMS keys.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-UpdateXRayKMSKey)

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

  Description: (Required) The Amazon Resource Name (ARN), key ID, or the key alias of the KMS key you want AWS X-Ray to use to encrypt data.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `kms:DescribeKey`
+  `xray:GetEncryptionConfig`
+  `xray:PutEncryptionConfig`

 **Document Steps**
+  `aws:executeAwsApi` - Enables encryption on your X-Ray data using the KMS key you specify in the `KeyId` parameter.
+  `aws:waitForAwsResourceProperty` - Waits for the encryption configuration status of your X-Ray to be `ACTIVE` .
+  `aws:executeAwsApi` - Gathers the ARN of the key you specify in the `KeyId` parameter.
+  `aws:assertAwsResourceProperty` - Verifies encryption has been enabled on your X-Ray.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
