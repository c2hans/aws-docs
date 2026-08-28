---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-configures3bucketversioning.html
---

# `AWS-ConfigureS3BucketVersioning`
<a name="automation-aws-configures3bucketversioning"></a>

 **Description**

Configure versioning for an Amazon Simple Storage Service (Amazon S3) bucket.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ConfigureS3BucketVersioning)

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

  Description: (Required) The name of the Amazon S3 bucket you want to configure versioning for.
+ VersioningState

  Type: String

  Valid values: Enabled \| Suspended

  Default: Enabled

   Description: (Optional) Applied to the VersioningConfiguration.Status. When set to 'Enabled', this process enables versioning for the objects in the bucket, all objects added to the bucket receive a unique version ID. When set to `Suspended` , this process disables versioning for the objects in the bucket. All objects added to the bucket receive the version ID `null` .

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
