---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-disables3bucketpublicreadwrite.html
---

# `AWS-DisableS3BucketPublicReadWrite`
<a name="automation-aws-disables3bucketpublicreadwrite"></a>

 **Description**

 Use Amazon Simple Storage Service (Amazon S3) `Block Public Access` to disable read and write access for a public S3 bucket. For more information, see [Using Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) in the *Amazon Simple Storage Service User Guide* .

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-DisableS3BucketPublicReadWrite)

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
+ S3BucketName

  Type: String

  Description: (Required) S3 bucket on which you want to restrict access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
