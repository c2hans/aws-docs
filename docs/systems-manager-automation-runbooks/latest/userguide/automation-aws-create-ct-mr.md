---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-create-ct-mr.html
---

# `AWSConfigRemediation-CreateCloudTrailMultiRegionTrail`
<a name="automation-aws-create-ct-mr"></a>

 **Description**

 The `AWSConfigRemediation-CreateCloudTrailMultiRegionTrail` runbook creates an AWS CloudTrail (CloudTrail) trail that delivers log files from multiple AWS Regions to the Amazon Simple Storage Service (Amazon S3) bucket of your choice.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-CreateCloudTrailMultiRegionTrail)

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

  Description: (Required) The name of the Amazon S3 bucket you want to upload logs to.
+ KeyPrefix

  Type: String

  Description: (Optional) The Amazon S3 key prefix that comes after the name of the bucket you designated for log file delivery.
+ TrailName

  Type: String

  Description: (Required) The name of the CloudTrail trail to be created.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `cloudtrail:CreateTrail`
+  `cloudtrail:StartLogging`
+  `cloudtrail:GetTrail`
+  `s3:PutObject`
+  `s3:GetBucketAcl`
+  `s3:PutBucketLogging`
+  `s3:ListBucket`

 **Document Steps**
+  `aws:executeAwsApi` - Accepts the trail name and the Amazon S3 bucket name as input and creates a CloudTrail trail.
+  `aws:executeAwsApi` - Enables logging on the created trail and starts log delivery to the Amazon S3 bucket you specified.
+  `aws:assertAwsResourceProperty` - Verifies that the CloudTrail trail has been created.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
