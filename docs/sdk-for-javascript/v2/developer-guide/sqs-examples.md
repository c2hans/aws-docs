---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/sqs-examples.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Amazon SQS Examples
<a name="sqs-examples"></a>

Amazon Simple Queue Service (Amazon SQS) is a fast, reliable, scalable, fully managed message queuing service. Amazon SQS lets you decouple the components of a cloud application. Amazon SQS includes standard queues with high throughput and at-least-once processing, and FIFO queues that provide FIFO (first-in, first-out) delivery and exactly-once processing.

![Relationship between JavaScript environments, the SDK, and Amazon SQS](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/images/code-samples-sqs.png)

The JavaScript API for Amazon SQS is exposed through the `AWS.SQS` client class. For more information about using the Amazon SQS client class, see [`Class: AWS.SQS`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SQS.html) in the API reference.

**Topics**
+ [Using Queues in Amazon SQS](sqs-examples-using-queues.md)
+ [Sending and Receiving Messages in Amazon SQS](sqs-examples-send-receive-messages.md)
+ [Managing Visibility Timeout in Amazon SQS](sqs-examples-managing-visibility-timeout.md)
+ [Enabling Long Polling in Amazon SQS](sqs-examples-enable-long-polling.md)
+ [Using Dead Letter Queues in Amazon SQS](sqs-examples-dead-letter-queues.md)
