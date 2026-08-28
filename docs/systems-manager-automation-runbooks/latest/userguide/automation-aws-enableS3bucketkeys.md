---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-enableS3bucketkeys.html
---

# `AWS-EnableS3BucketKeys`
<a name="automation-aws-enableS3bucketkeys"></a>

 **Description**

The `AWS-EnableS3BucketKeys` runbook enables Bucket Keys on the Amazon Simple Storage Service (Amazon S3) bucket you specify. This bucket level key creates data keys for new objects during its lifecycle. If you don't specify a value for the `KmsKeyId` parameter, server-side encryption using Amazon S3 managed keys (SSE-S3) are used for the default encryption configuration.

**Note**
Amazon S3 Bucket Keys aren't supported for dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys (DSSE-KMS).

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-EnableS3BucketKeys)

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
+ BucketName

  Type: String

  Description: (Required) The name of the S3 bucket you want to enable Bucket Keys for.
+ KMSKeyId

  Type: String

   Description: (Optional) The Amazon Resource Name (ARN), key ID, or the key alias of the AWS Key Management Service (AWS KMS) customer managed key you want to use for server-side encryption.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ssm:StartAutomationExecution`
+ `ssm:GetAutomationExecution`
+ `s3:GetEncryptionConfiguration`
+ `s3:PutEncryptionConfiguration`

 **Document Steps**
+ ChooseEncryptionType (aws:branch) - Evaluates the value provided for the `KmsKeyId` parameter to determine if SSE-S3 (AES256) or SSE-KMS will be used.
+ PutBucketKeysKMS (aws:executeAwsApi) - Sets the `BucketKeyEnabled` property to `true` for the specified S3 bucket using the specified `KmsKeyId`.
+ PutBucketKeysAES256 (aws:executeAwsApi) - Sets the `BucketKeyEnabled` property to `true` for the specified S3 bucket with AES256 encryption.
+ VerifyS3BucketKeysEnabled (aws:assertAwsResourceProperty) - Verifies that the Bucket Keys are enabled on the target S3 bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
