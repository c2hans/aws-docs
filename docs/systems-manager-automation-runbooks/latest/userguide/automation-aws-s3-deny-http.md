---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-s3-deny-http.html
---

# `AWSConfigRemediation-RestrictBucketSSLRequestsOnly`
<a name="automation-aws-s3-deny-http"></a>

 **Description**

 The `AWSConfigRemediation-RestrictBucketSSLRequestsOnly` runbook creates an Amazon Simple Storage Service (Amazon S3) bucket policy statement that explicitly denies HTTP requests to the Amazon S3 bucket you specify.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-RestrictBucketSSLRequestsOnly)

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
+ BucketName

  Type: String

  Description: (Required) The name of the S3 bucket that you want to deny HTTP requests.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `s3:DeleteBucketPolicy`
+  `s3:GetBucketPolicy`
+  `s3:PutEncryptionConfiguration`
+  `s3:PutBucketPolicy`

 **Document Steps**
+  `aws:executeScript` - Creates a bucket policy for the S3 bucket specified in the `BucketName` parameter that explicitly denies HTTP requests.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
