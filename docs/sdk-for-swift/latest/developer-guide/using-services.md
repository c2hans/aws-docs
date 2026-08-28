---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-services.html
---

# Working with AWS services using the AWS SDK for Swift
<a name="using-services"></a>

This chapter contains information about how to work with AWS services by using the SDK for Swift.

**Contents**
+ [Amazon S3](using-services-s3.md)
  + [Multipart uploads](using-multipart-uploads.md)
    + [Overview](using-multipart-uploads.md#multipart-overview)
    + [The multipart upload process](using-multipart-uploads.md#multipart-process)
    + [Starting a multipart upload](using-multipart-uploads.md#multipart-example-start)
    + [Uploading the parts](using-multipart-uploads.md#multipart-example-parts)
    + [Completing a multipart upload](using-multipart-uploads.md#multipart-example-complete)
    + [Additional information](using-multipart-uploads.md#multipart-additional-information)
  + [Binary streaming](using-binary-streaming.md)
    + [Overview](using-binary-streaming.md#binary-streaming-overview)
    + [Streaming incoming data](using-binary-streaming.md#binary-streaming-downloads)
    + [Streaming outgoing data](using-binary-streaming.md#binary-streaming-uploads)
  + [Data integrity protection with checksums](s3-checksums.md)
    + [Upload an object](s3-checksums.md#use-service-S3-checksum-upload)
      + [Use a pre-calculated checksum value](s3-checksums.md#use-service-S3-checksum-upload-pre)
      + [Multipart uploads](s3-checksums.md#use-service-S3-checksum-upload-multi)
    + [Download an object](s3-checksums.md#use-service-S3-checksum-download)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
