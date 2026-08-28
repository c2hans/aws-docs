---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/enable-cloudtrail-kms-encryption.html
---

# `AWS-EnableCloudTrailKmsEncryption`
<a name="enable-cloudtrail-kms-encryption"></a>

**Description**

This runbook updates the configuration of one or more AWS CloudTrail trails to use AWS Key Management Service (AWS KMS) encryption.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableCloudTrailKmsEncryption)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ KMSKeyId

  Type: String

  Description: (Required) The key ID of the of the customer managed key you want to use to encrypt the trail you specify in the `TrailName` parameter. The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, or a fully specified ARN to a key.
+ TrailNames

  Type: StringList

  Description: (Required) A comma separated list of the trails you want to update to be encrypted.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudtrail:UpdateTrail`
+ `kms:DescribeKey`
+ `kms:ListKeys`

**Document Steps**
+ `aws:executeScript` - Enables AWS KMS encryption on the trails you specify in the `TrailName` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
