---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudtrail_example_cloudtrail_UpdateTrail_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateTrail` with a CLI
<a name="cloudtrail_example_cloudtrail_UpdateTrail_section"></a>

The following code examples show how to use `UpdateTrail`.

------
#### [ CLI ]

**AWS CLI**
**To update a trail**
The following `update-trail` example updates a trail to use an existing bucket for log delivery.

```
aws cloudtrail update-trail \
    --name {{Trail1}} \
    --s3-bucket-name {{amzn-s3-demo-bucket}}
```
Output:

```
{
    "IncludeGlobalServiceEvents": true,
    "Name": "Trail1",
    "TrailARN": "arn:aws:cloudtrail:us-west-2:123456789012:trail/Trail1",
    "LogFileValidationEnabled": false,
    "IsMultiRegionTrail": true,
    "S3BucketName": "amzn-s3-demo-bucket"
}
```
+  For API details, see [UpdateTrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-trail.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Updates the specified trail so that global service events (such as those from IAM) are recorded and changes the common key prefix of the log files going forwards to be 'globallogs'.**

```
Update-CTTrail -Name "awscloudtrail-example" -IncludeGlobalServiceEvents $true -S3KeyPrefix "globallogs"
```
**Example 2: Updates the specified trail so notifications about new log deliveries are sent to the specified SNS topic.**

```
Update-CTTrail -Name "awscloudtrail-example" -SnsTopicName "mlog-deliverytopic2"
```
**Example 3: Updates the specified trail so logs are delivered to a different bucket.**

```
Update-CTTrail -Name "awscloudtrail-example" -S3BucketName "otherlogs"
```
+  For API details, see [UpdateTrail](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Updates the specified trail so that global service events (such as those from IAM) are recorded and changes the common key prefix of the log files going forwards to be 'globallogs'.**

```
Update-CTTrail -Name "awscloudtrail-example" -IncludeGlobalServiceEvents $true -S3KeyPrefix "globallogs"
```
**Example 2: Updates the specified trail so notifications about new log deliveries are sent to the specified SNS topic.**

```
Update-CTTrail -Name "awscloudtrail-example" -SnsTopicName "mlog-deliverytopic2"
```
**Example 3: Updates the specified trail so logs are delivered to a different bucket.**

```
Update-CTTrail -Name "awscloudtrail-example" -S3BucketName "otherlogs"
```
+  For API details, see [UpdateTrail](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
