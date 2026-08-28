---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/dg-ota-bucket.html
---

# Create an Amazon S3 bucket to store your update
<a name="dg-ota-bucket"></a>

OTA update files are stored in Amazon S3 buckets.

If you're using Code Signing for AWS IoT, the command that you use to create a code-signing job takes a source bucket (where the unsigned firmware image is located) and a destination bucket (where the signed firmware image is written). You can specify the same bucket for the source and destination. The file names are changed to GUIDs so the original files are not overwritten.<a name="create-bucket"></a>

**To create an Amazon S3 bucket**

1. Sign in to the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Create bucket**.

1. Enter a **bucket name**.

1. Under **Bucket settings for Block Public Access** keep **Block all public access** selected to accept the default permissions.

1. Under **Bucket Versioning**, select **Enable** to keep all versions in the same bucket.

1. Choose **Create bucket**.

For more information about Amazon S3, see [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
