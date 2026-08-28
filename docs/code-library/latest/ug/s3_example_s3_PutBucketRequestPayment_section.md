---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/s3_example_s3_PutBucketRequestPayment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutBucketRequestPayment` with a CLI
<a name="s3_example_s3_PutBucketRequestPayment_section"></a>

The following code examples show how to use `PutBucketRequestPayment`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To enable ``requester pays`` configuration for a bucket**
The following `put-bucket-request-payment` example enables `requester pays` for the specified bucket.

```
aws s3api put-bucket-request-payment \
    --bucket {{amzn-s3-demo-bucket}} \
    --request-payment-configuration '{{{"Payer":"Requester"}}}'
```
This command produces no output.
**Example 2: To disable ``requester pays`` configuration for a bucket**
The following `put-bucket-request-payment` example disables `requester pays` for the specified bucket.

```
aws s3api put-bucket-request-payment \
    --bucket {{amzn-s3-demo-bucket}} \
    --request-payment-configuration '{{{"Payer":"BucketOwner"}}}'
```
This command produces no output.
+  For API details, see [PutBucketRequestPayment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-request-payment.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Updates the request payment configuration for the bucket named 'amzn-s3-demo-bucket' so that the person requesting downloads from the bucket will be charged for the download. By default the bucket owner pays for downloads. To set the request payment back to the default use 'BucketOwner' for the RequestPaymentConfiguration\_Payer parameter.**

```
Write-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket -RequestPaymentConfiguration_Payer Requester
```
+  For API details, see [PutBucketRequestPayment](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Updates the request payment configuration for the bucket named 'amzn-s3-demo-bucket' so that the person requesting downloads from the bucket will be charged for the download. By default the bucket owner pays for downloads. To set the request payment back to the default use 'BucketOwner' for the RequestPaymentConfiguration\_Payer parameter.**

```
Write-S3BucketRequestPayment -BucketName amzn-s3-demo-bucket -RequestPaymentConfiguration_Payer Requester
```
+  For API details, see [PutBucketRequestPayment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
