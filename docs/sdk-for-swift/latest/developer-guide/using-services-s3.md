---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-services-s3.html
---

# Working with Amazon S3 using the AWS SDK for Swift
<a name="using-services-s3"></a>

Your main interface to the Amazon Simple Storage Service for the SDK for Swift is the [`S3Client`](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client). Use the `S3Client` like other service clients in the SDK to make [requests](making-requests.md) to Amazon S3.

Resources to help you use the SDK for Swift with S3 are:
+ The [AWS SDK for Swift API reference for S3](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3).
+ The [S3 service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and [service API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html).

The following topics present guided code examples for select SDK for Swift APIs that work with S3.

**Topics**
+ [Multipart uploads](using-multipart-uploads.md)
+ [Binary streaming](using-binary-streaming.md)
+ [Data integrity protection with checksums](s3-checksums.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
