---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/using-sqs-with-go-sdk.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Amazon SQS Examples Using the AWS SDK for Go
<a name="using-sqs-with-go-sdk"></a>

Amazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications. The AWS SDK for Go examples can integrate Amazon SQS into your applications. The examples assume you have already set up and configured the SDK (that is, you’ve imported all required packages and set your credentials and region). For more information, see [Getting Started with the AWS SDK for Go](setting-up.md) and [Configuring the AWS SDK for Go](configuring-sdk.md).

You can download complete versions of these example files from the [aws-doc-sdk-examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/go/example_code/sqs) repository on GitHub.

**Topics**
+ [Using Amazon SQS Queues](sqs-example-create-queue.md)
+ [Sending and Receiving Messages in Amazon SQS](sqs-example-receive-message.md)
+ [Managing Visibility Timeout in Amazon SQS Queues](sqs-example-managing-visibility-timeout.md)
+ [Enabling Long Polling in Amazon SQS Queues](sqs-example-enable-long-polling.md)
+ [Using Dead Letter Queues in Amazon SQS](sqs-example-dead-letter-queues.md)
