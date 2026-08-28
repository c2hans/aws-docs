---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enable-ebs-encryption.html
---

# `AWSConfigRemediation-EnableEbsEncryptionByDefault`
<a name="automation-aws-enable-ebs-encryption"></a>

 **Description**

 The `AWSConfigRemediation-EnableEbsEncryptionByDefault` runbook enables encryption on all new Amazon Elastic Block Store (Amazon EBS) volumes in the AWS account and AWS Region where you run the automation. Volumes that were created before you run the automation are not encrypted.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-EnableEbsEncryptionByDefault)

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

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ec2:EnableEbsEncryptionByDefault`
+  `ec2:GetEbsEncryptionByDefault`
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`

 **Document Steps**
+  `aws:executeAwsApi` - Enables the default Amazon EBS encryption setting in the current account and Region.
+  `aws:assertAwsResourceProperty` - Verifies that the default Amazon EBS encryption setting has been enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
