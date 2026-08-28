---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-managing-large-messages.html
---

# Managing large Amazon SQS messages with Extended Client Library and Amazon Simple Storage Service
<a name="sqs-managing-large-messages"></a>

Use the [Amazon SQS Extended Client Library for Java](https://github.com/awslabs/amazon-sqs-java-extended-client-lib) and [Amazon SQS Extended Client Library for Python](https://github.com/awslabs/amazon-sqs-python-extended-client-lib/) to send large messages, especially for payloads between 256 KB and 2 GB. These libraries store the message payload in an Amazon S3 bucket and send a reference to the stored object in the Amazon SQS queue.

**Note**
 The Amazon SQS Extended Client Libraries are compatible with both standard and FIFO queues.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Queue Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSSimpleQueueService` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
