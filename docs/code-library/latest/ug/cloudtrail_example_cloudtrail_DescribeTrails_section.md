---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudtrail_example_cloudtrail_DescribeTrails_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeTrails` with a CLI
<a name="cloudtrail_example_cloudtrail_DescribeTrails_section"></a>

The following code examples show how to use `DescribeTrails`.

------
#### [ CLI ]

**AWS CLI**
**To describe a trail**
The following `describe-trails` example returns the settings for `Trail1` and `Trail2`.

```
aws cloudtrail describe-trails \
    --trail-name-list {{Trail1}} {{Trail2}}
```
Output:

```
{
    "trailList": [
        {
            "IncludeGlobalServiceEvents": true,
            "Name": "Trail1",
            "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1",
            "LogFileValidationEnabled": false,
            "IsMultiRegionTrail": false,
            "S3BucketName": "amzn-s3-demo-bucket",
            "CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/CloudTrail_CloudWatchLogs_Role",
            "CloudWatchLogsLogGroupArn": "arn:aws:logs:us-east-1:123456789012:log-group:CloudTrail:*",
            "SnsTopicName": "my-topic",
            "HomeRegion": "us-east-1"
        },
        {
            "IncludeGlobalServiceEvents": true,
            "Name": "Trail2",
            "S3KeyPrefix": "my-prefix",
            "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail2",
            "LogFileValidationEnabled": false,
            "IsMultiRegionTrail": false,
            "S3BucketName": "amzn-s3-demo-bucket2",
            "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/4c5ae5ac-3c13-421e-8335-c7868ef6a769",
            "HomeRegion": "us-east-1"
        }
    ]
}
```
+  For API details, see [DescribeTrails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/describe-trails.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns the settings of all trails associated with the current region for your account.**

```
Get-CTTrail
```
**Example 2: Returns the settings for the specified trails.**

```
Get-CTTrail -TrailNameList trail1,trail2
```
**Example 3: Returns the settings for the specified trails that were created in a region other than the current shell default (in this case the Frankfurt (eu-central-1) region).**

```
Get-CTTrail -TrailNameList trailABC,trailDEF -Region eu-central-1
```
+  For API details, see [DescribeTrails](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns the settings of all trails associated with the current region for your account.**

```
Get-CTTrail
```
**Example 2: Returns the settings for the specified trails.**

```
Get-CTTrail -TrailNameList trail1,trail2
```
**Example 3: Returns the settings for the specified trails that were created in a region other than the current shell default (in this case the Frankfurt (eu-central-1) region).**

```
Get-CTTrail -TrailNameList trailABC,trailDEF -Region eu-central-1
```
+  For API details, see [DescribeTrails](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
