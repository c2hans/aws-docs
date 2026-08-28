---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_DeletePublicAccessBlock_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
