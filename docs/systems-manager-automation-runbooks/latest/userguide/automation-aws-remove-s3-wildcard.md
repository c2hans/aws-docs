---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-remove-s3-wildcard.html
---

# `AWSConfigRemediation-RemovePrincipalStarFromS3BucketPolicy`
<a name="automation-aws-remove-s3-wildcard"></a>

 **Description**

 The `AWSConfigRemediation-RemovePrincipalStarFromS3BucketPolicy` runbook removes principal policy statements that have wildcards ( `Principal: *` or `Principal: "AWS": *` ) for `Allow` actions from your Amazon Simple Storage Service (Amazon S3) bucket policy. Policy statements with conditions are also removed.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-RemovePrincipalStarFromS3BucketPolicy)

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

  Description: (Required) The name of the Amazon S3 bucket whose policy you want to modify.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `s3:DeleteBucketPolicy`
+  `s3:GetBucketPolicy`
+  `s3:PutBucketPolicy`

 **Document Steps**
+  `aws:executeScript` - Modifies the bucket policy and verifies principal policy statements with wildcards have been removed from the Amazon S3 bucket you specify in the `BucketName` parameter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
