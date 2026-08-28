---
source_url: https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html
---

# Publishing large messages with Amazon SNS and Amazon S3
<a name="large-message-payloads"></a>

To publish large Amazon SNS messages, you can use the [Amazon SNS Extended Client Library for Java](https://github.com/awslabs/amazon-sns-java-extended-client-lib/), or the [Amazon SNS Extended Client Library for Python](https://github.com/awslabs/amazon-sns-python-extended-client-lib). These libraries are useful for messages that are larger than the current maximum of 256 KB, with a maximum of 2 GB. Both libraries save the actual payload to an Amazon S3 bucket, and publish the reference of the stored Amazon S3 object to the Amazon SNS topic. Subscribed Amazon SQS queues can use the [Amazon SQS Extended Client Library for Java](https://github.com/awslabs/amazon-sqs-java-extended-client-lib) to de-reference and retrieve payloads from Amazon S3. Other endpoints such as Lambda can use the [Payload Offloading Java Common Library for AWS](https://github.com/awslabs/payload-offloading-java-common-lib-for-aws) to de-reference and retrieve the payload.

**Note**
The Amazon SNS Extended Client Libraries are compatible with both standard and FIFO topics.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
