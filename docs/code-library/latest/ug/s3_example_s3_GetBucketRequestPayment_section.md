---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_GetBucketRequestPayment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetBucketRequestPayment` with a CLI
<a name="s3_example_s3_GetBucketRequestPayment_section"></a>

The following code examples show how to use `GetBucketRequestPayment`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve the request payment configuration for a bucket**
The following `get-bucket-request-payment` example retrieves the requester pays configuration for the specified bucket.

```
aws s3api get-bucket-request-payment \
    --bucket {{amzn-s3-demo-bucket}}
```
Output:

```
{
    "Payer": "BucketOwner"
}
```
+  For API details, see [GetBucketRequestPayment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-request-payment.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns the request payment configuration for the bucket named 'amzn-s3-demo-bucket'. By default, the bucket owner pays for downloads from the bucket.**

```
Get-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket
```
+  For API details, see [GetBucketRequestPayment](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns the request payment configuration for the bucket named 'amzn-s3-demo-bucket'. By default, the bucket owner pays for downloads from the bucket.**

```
Get-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket
```
+  For API details, see [GetBucketRequestPayment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
