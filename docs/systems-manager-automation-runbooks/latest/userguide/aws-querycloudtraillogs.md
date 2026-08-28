---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/aws-querycloudtraillogs.html
---

# `AWS-QueryCloudTrailLogs`
<a name="aws-querycloudtraillogs"></a>

 **Description**

 The `AWS-QueryCloudTrailLogs` runbook creates an Amazon Athena table from the Amazon Simple Storage Service (Amazon S3) bucket of your choice containing AWS CloudTrail (CloudTrail) logs. After creating the table, the automation runs SQL queries you specify and then deletes the table.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-QueryCloudTrailLogs)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Databases

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ Query

  Type: String

  Description: (Required) The SQL query you want to run.
+ SourceBucketPath

  Type: String

  Description: (Required) The name of the Amazon S3 bucket containing the CloudTrail log files you want to query.
+ TableName

  Type: String

  Description: (Optional) The name of the Athena table created by the automation.

  Default: cloudtrail\_logs

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `athena:GetQueryResults`
+  `athena:GetQueryExecution`
+  `athena:StartQueryExecution`
+  `glue:CreateTable`
+  `glue:DeleteTable`
+  `glue:GetDatabase`
+  `glue:GetPartitions`
+  `glue:GetTable`
+  `s3:AbortMultipartUpload`
+  `s3:CreateBucket`
+  `s3:GetBucketLocation`
+  `s3:GetObject`
+  `s3:ListBucket`
+  `s3:ListBucketMultipartUploads`
+  `s3:ListMultipartUploadParts`
+  `s3:PutObject`

 **Document Steps**
+  `aws:executeAwsApi` - Creates an Athena table.
+  `aws:executeAwsApi` - Runs the query string you specify in the `Query` parameter.
+  `aws:executeScript` - Polls and waits for the query to complete.
+  `aws:executeAwsApi` - Gets the results of the query.
+  `aws:executeAwsApi` - Deletes the table created by the automation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
