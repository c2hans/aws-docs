---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/developerguide/s3_example_s3_GetBucketLogging_section.html
---

# Use `GetBucketLogging` with a CLI
<a name="s3_example_s3_GetBucketLogging_section"></a>

The following code examples show how to use `GetBucketLogging`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve the logging status for a bucket**
The following `get-bucket-logging` example retrieves the logging status for the specified bucket.

```
aws s3api get-bucket-logging \
    --bucket {{amzn-s3-demo-bucket}}
```
Output:

```
{
    "LoggingEnabled": {
        "TargetPrefix": "",
        "TargetBucket": "amzn-s3-demo-bucket-logs"
          }
}
```
+  For API details, see [GetBucketLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-logging.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This command returns the logging status for the specified bucket.**

```
Get-S3BucketLogging -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
TargetBucketName   Grants TargetPrefix
----------------   ------ ------------
testbucket1        {}     testprefix
```
+  For API details, see [GetBucketLogging](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This command returns the logging status for the specified bucket.**

```
Get-S3BucketLogging -BucketName 'amzn-s3-demo-bucket'
```
**Output:**

```
TargetBucketName   Grants TargetPrefix
----------------   ------ ------------
testbucket1        {}     testprefix
```
+  For API details, see [GetBucketLogging](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
