---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_DeleteBucketAnalyticsConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteBucketAnalyticsConfiguration` with a CLI
<a name="s3_example_s3_DeleteBucketAnalyticsConfiguration_section"></a>

The following code examples show how to use `DeleteBucketAnalyticsConfiguration`.

------
#### [ CLI ]

**AWS CLI**
**To delete an analytics configuration for a bucket**
The following `delete-bucket-analytics-configuration` example removes the analytics configuration for the specified bucket and ID.

```
aws s3api delete-bucket-analytics-configuration \
    --bucket {{amzn-s3-demo-bucket}} \
    --id {{1}}
```
This command produces no output.
+  For API details, see [DeleteBucketAnalyticsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-analytics-configuration.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: The command removes the analytics filter with name 'testfilter' in the given S3 bucket.**

```
Remove-S3BucketAnalyticsConfiguration -BucketName 'amzn-s3-demo-bucket' -AnalyticsId 'testfilter'
```
+  For API details, see [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: The command removes the analytics filter with name 'testfilter' in the given S3 bucket.**

```
Remove-S3BucketAnalyticsConfiguration -BucketName 'amzn-s3-demo-bucket' -AnalyticsId 'testfilter'
```
+  For API details, see [DeleteBucketAnalyticsConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
