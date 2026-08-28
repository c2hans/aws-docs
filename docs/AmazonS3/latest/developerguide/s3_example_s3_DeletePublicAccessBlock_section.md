---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/developerguide/s3_example_s3_DeletePublicAccessBlock_section.html
---

# Use `DeletePublicAccessBlock` with a CLI
<a name="s3_example_s3_DeletePublicAccessBlock_section"></a>

The following code examples show how to use `DeletePublicAccessBlock`.

------
#### [ CLI ]

**AWS CLI**
**To delete the block public access configuration for a bucket**
The following `delete-public-access-block` example removes the block public access configuration on the specified bucket.

```
aws s3api delete-public-access-block \
    --bucket {{amzn-s3-demo-bucket}}
```
This command produces no output.
+  For API details, see [DeletePublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-public-access-block.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This command turns off the block public access setting for the given bucket.**

```
Remove-S3PublicAccessBlock -BucketName 'amzn-s3-demo-bucket' -Force -Select '^BucketName'
```
**Output:**

```
amzn-s3-demo-bucket
```
+  For API details, see [DeletePublicAccessBlock](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This command turns off the block public access setting for the given bucket.**

```
Remove-S3PublicAccessBlock -BucketName 'amzn-s3-demo-bucket' -Force -Select '^BucketName'
```
**Output:**

```
amzn-s3-demo-bucket
```
+  For API details, see [DeletePublicAccessBlock](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
