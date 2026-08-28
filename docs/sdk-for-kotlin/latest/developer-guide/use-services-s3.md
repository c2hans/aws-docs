---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/use-services-s3.html
---

# Work with Amazon S3 using the AWS SDK for Kotlin
<a name="use-services-s3"></a>

Your main interface to the Amazon Simple Storage Service for the Kotlin SDK is the [S3Client](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/index.html). Use the [`S3Client`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/index.html) like other service clients in the SDK to make [requests](making-requests.md) to Amazon S3.

Resources to help you use the Kotlin SDK with S3 are:
+ the Kotlin SDK [API reference for S3](/sdk-for-kotlin/api/latest/s3/index.html).
+ the [S3 service User Guide](/AmazonS3/latest/userguide/Welcome.html) and [service API reference](/AmazonS3/latest/API/Welcome.html).

The following topics present guided code examples for select Kotlin SDK APIs that work with S3.

**Topics**
+ [Data integrity protection with checksums](s3-checksums.md)
+ [Work with Multi-Region Access Points](use-services-s3-mrap.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
