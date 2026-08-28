---
source_url: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/best-practices.html
---

The AWS SDK for Java 1.x reached end-of-support on December 31, 2025. We recommend that you migrate to the [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) to continue receiving new features, availability improvements, and security updates.

# Best Practices for AWS Development with the AWS SDK for Java
<a name="best-practices"></a>

The following best practices can help you avoid issues or trouble as you develop AWS applications with the AWS SDK for Java. We’ve organized best practices by service.

## S3
<a name="s3"></a>

### Avoid ResetExceptions
<a name="s3-avoid-resetexception"></a>

When you upload objects to Amazon S3 by using streams (either through an `AmazonS3` client or `TransferManager`), you might encounter network connectivity or timeout issues. By default, the AWS SDK for Java attempts to retry failed transfers by marking the input stream before the start of a transfer and then resetting it before retrying.

If the stream doesn’t support mark and reset, the SDK throws a [ResetException](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/ResetException.html) when there are transient failures and retries are enabled.

 **Best Practice**

We recommend that you use streams that support mark and reset operations.

The most reliable way to avoid a [ResetException](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/ResetException.html) is to provide data by using a [File](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/File.html) or [FileInputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/FileInputStream.html), which the AWS SDK for Java can handle without being constrained by mark and reset limits.

If the stream isn’t a [FileInputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/FileInputStream.html) but does support mark and reset, you can set the mark limit by using the `setReadLimit` method of [RequestClientOptions](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/RequestClientOptions.html). Its default value is 128 KB. Setting the read limit value to *one byte greater than the size of stream* will reliably avoid a [ResetException](https://docs.aws.amazon.com/sdk-for-java/v1/reference/com/amazonaws/ResetException.html).

For example, if the maximum expected size of a stream is 100,000 bytes, set the read limit to 100,001 (100,000 \+ 1) bytes. The mark and reset will always work for 100,000 bytes or less. Be aware that this might cause some streams to buffer that number of bytes into memory.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
