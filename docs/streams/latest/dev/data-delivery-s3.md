---
source_url: https://docs.aws.amazon.com/streams/latest/dev/data-delivery-s3.html
---

# Amazon S3 general purpose delivery
<a name="data-delivery-s3"></a>

 Amazon S3 general purpose delivery writes streaming data from a Amazon Kinesis Data Streams stream directly to a general purpose Amazon S3 bucket. Records are delivered in their original source format with no transformation applied, batched into optimally sized objects with configurable compression and an S3 key structure you define. This is ideal for use cases such as raw log archival, event replay, and downstream batch processing.

**Topics**
+ [How Amazon S3 delivery works](data-delivery-s3-about.md)
+ [Getting started with S3 general purpose delivery](data-delivery-s3-getting-started.md)
+ [Manage Amazon S3 general purpose deliveries](data-delivery-s3-manage.md)
+ [S3 output key template for Amazon S3 delivery](data-delivery-s3-key-template.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
