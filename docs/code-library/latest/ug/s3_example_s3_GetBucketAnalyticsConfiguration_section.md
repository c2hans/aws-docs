---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_GetBucketAnalyticsConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetBucketAnalyticsConfiguration` with a CLI
<a name="s3_example_s3_GetBucketAnalyticsConfiguration_section"></a>

The following code examples show how to use `GetBucketAnalyticsConfiguration`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve the analytics configuration for a bucket with a specific ID**
The following `get-bucket-analytics-configuration` example displays the analytics configuration for the specified bucket and ID.

```
aws s3api get-bucket-analytics-configuration \
    --bucket {{amzn-s3-demo-bucket}} \
    --id {{1}}
```
Output:

```
{
    "AnalyticsConfiguration": {
        "StorageClassAnalysis": {},
        "Id": "1"
    }
}
```
+  For API details, see [GetBucketAnalyticsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-analytics-configuration.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This command returns the details of the analytics filter with the name 'testfilter' in the given S3 bucket.**

```
Get-S3BucketAnalyticsConfiguration -BucketName 'amzn-s3-demo-bucket' -AnalyticsId 'testfilter'
```
+  For API details, see [GetBucketAnalyticsConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This command returns the details of the analytics filter with the name 'testfilter' in the given S3 bucket.**

```
Get-S3BucketAnalyticsConfiguration -BucketName 'amzn-s3-demo-bucket' -AnalyticsId 'testfilter'
```
+  For API details, see [GetBucketAnalyticsConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
