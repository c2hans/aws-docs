---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-block-public-s3-bucket.html
---

# `AWSConfigRemediation-ConfigureS3BucketPublicAccessBlock`
<a name="automation-aws-block-public-s3-bucket"></a>

 **Description**

 The `AWSConfigRemediation-ConfigureS3BucketPublicAccessBlock` runbook configures the Amazon Simple Storage Service (Amazon S3) public access block settings for an Amazon S3 bucket based on the values you specify in the runbook parameters.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-ConfigureS3BucketPublicAccessBlock)

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
+ BlockPublicAcls

  Type: Boolean

  Default: true

   Description: (Optional) If set to `true` , Amazon S3 blocks public access control lists (ACLs) for the S3 bucket, and objects stored in the S3 bucket you specify in the `BucketName` parameter.
+ BlockPublicPolicy

  Type: Boolean

  Default: true

   Description: (Optional) If set to `true` , Amazon S3 blocks public bucket policies for the S3 bucket you specify in the `BucketName` parameter.
+ BucketName

  Type: String

  Description: (Required) The name of the S3 bucket you want to configure.
+ IgnorePublicAcls

  Type: Boolean

  Default: true

   Description: (Optional) If set to `true` , Amazon S3 ignores all public ACLs for the S3 bucket you specify in the `BucketName` parameter.
+ RestrictPublicBuckets

  Type: Boolean

  Default: true

   Description: (Optional) If set to `true` , Amazon S3 restricts public bucket policies for the S3 bucket you specify in the `BucketName` parameter.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `s3:GetAccountPublicAccessBlock`
+  `s3:PutAccountPublicAccessBlock`
+  `s3:GetBucketPublicAccessBlock`
+  `s3:PutBucketPublicAccessBlock`

 **Document Steps**
+  `aws:executeAwsApi` - Creates or modifies the `PublicAccessBlock` configuration for the S3 bucket specified in the `BucketName` parameter.
+  `aws:executeScript` - Returns the `PublicAccessBlock` configuration for the S3 bucket specified in the `BucketName` parameter, and verifies the changes were successfully made based on the values specified in the runbook parameters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
