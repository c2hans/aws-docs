---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-s3-with-go-sdk.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Amazon S3 Examples Using the AWS SDK for Go
<a name="using-s3-with-go-sdk"></a>

Amazon Simple Storage Service (Amazon S3) is storage for the internet. The AWS SDK for Go examples can integrate Amazon S3 into your applications. The examples assume you have already set up and configured the SDK (that is, you’ve imported all required packages and set your credentials and region). For more information, see [Getting Started with the AWS SDK for Go](setting-up.md) and [Configuring the AWS SDK for Go](configuring-sdk.md).

You can download complete versions of these example files from the [aws-doc-sdk-examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/go/example_code/s3) repository on GitHub.

**Topics**
+ [Performing Basic Amazon S3 Bucket Operations](s3-example-basic-bucket-operations.md)
+ [Creating Pre-Signed URLs for Amazon S3 Buckets](s3-example-presigned-urls.md)
+ [Using an Amazon S3 Bucket as a Static Web Host](s3-example-static-web-host.md)
+ [Working with Amazon S3 CORS Permissions](s3-example-cors.md)
+ [Working with Amazon S3 Bucket Policies](s3-example-bucket-policy.md)
+ [Working with Amazon S3 Bucket ACLs](s3-example-bucket-acls.md)
+ [Encrypting Amazon S3 Bucket Items](s3-examples-encryption.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
