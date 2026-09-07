---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/sqs-apis-intro.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Messaging using Amazon SQS
<a name="sqs-apis-intro"></a>

The AWS SDK for .NET supports [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/), which is a message queuing service that handles messages or workflows between components in a system.

Amazon SQS queues provide a mechanism that enables you to send, store, and receive messages between software components such as microservices, distributed systems, and serverless applications. This enables you to decouple such components and frees you from the need to design and operate your own messaging system. For information about how queues and messages work in Amazon SQS, see [Amazon SQS tutorials](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-other-tutorials.html) and [Basic Amazon SQS architecture](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-architecture.html) in the [Amazon Simple Queue Service Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/).

**Important**
Due to the distributed nature of queues, Amazon SQS can't guarantee that you'll receive messages in the precise order they're sent. If you need to preserve message order, use an [Amazon SQS FIFO queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html).

## APIs
<a name="w2aac19c15c29b9"></a>

The AWS SDK for .NET provides APIs for Amazon SQS clients. The APIs enable you to work with Amazon SQS features such as queues and messages. This section contains a small number of examples that show you the patterns you can follow when working with these APIs. To view the full set of APIs, see the [AWS SDK for .NET API Reference](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/) (and scroll to "Amazon.SQS").

The Amazon SQS APIs are provided by the [AWSSDK.SQS](https://www.nuget.org/packages/AWSSDK.SQS) NuGet package.

## Prerequisites
<a name="w2aac19c15c29c11"></a>

Before you begin, be sure you have [set up your environment](net-dg-config.md) and [configured your project](configuring-the-sdk.md). Also review the information in [Using the SDK](net-dg-sdk-features.md).

## Topics
<a name="w2aac19c15c29c13"></a>

**Topics**
+ [APIs](#w2aac19c15c29b9)
+ [Prerequisites](#w2aac19c15c29c11)
+ [Topics](#w2aac19c15c29c13)
+ [Creating queues](CreateQueue.md)
+ [Updating queues](UpdateSqsQueue.md)
+ [Deleting queues](DeleteSqsQueue.md)
+ [Sending messages](SendMessage.md)
+ [Receiving messages](ReceiveMessage.md)
