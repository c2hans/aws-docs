---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_DeleteBucketMetricsConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteBucketMetricsConfiguration` with a CLI
<a name="s3_example_s3_DeleteBucketMetricsConfiguration_section"></a>

The following code examples show how to use `DeleteBucketMetricsConfiguration`.

------
#### [ CLI ]

**AWS CLI**
**To delete a metrics configuration for a bucket**
The following `delete-bucket-metrics-configuration` example removes the metrics configuration for the specified bucket and ID.

```
aws s3api delete-bucket-metrics-configuration \
    --bucket {{amzn-s3-demo-bucket}} \
    --id {{123}}
```
This command produces no output.
+  For API details, see [DeleteBucketMetricsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-metrics-configuration.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: The command removes the metrics filter with name 'testmetrics' in the given S3 bucket.**

```
Remove-S3BucketMetricsConfiguration -BucketName 'amzn-s3-demo-bucket' -MetricsId 'testmetrics'
```
+  For API details, see [DeleteBucketMetricsConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: The command removes the metrics filter with name 'testmetrics' in the given S3 bucket.**

```
Remove-S3BucketMetricsConfiguration -BucketName 'amzn-s3-demo-bucket' -MetricsId 'testmetrics'
```
+  For API details, see [DeleteBucketMetricsConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
