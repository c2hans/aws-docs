---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/sqs.html
---

# Amazon SQS
<a name="sqs"></a>

[Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) supports standard queues, which do not guarantee ordering, and FIFO queues, which do guarantee ordering within a given *message group*.

Queues are a common method for choreographing microservices and provide durable storage for messages for up to 14 days. Queues are populated by producers and drained by consumers. When you use AWS Lambda as a consumer, you can configure an SQS queue as an event source. In this case, the Lambda service event source mapping (ESM) polls the queue for you and delivers messages to your Lambda function when they become available. Microservices that run on other types of compute services, such as Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Compute Cloud (Amazon EC2), have to implement their own polling mechanism to fetch new messages from the queue, when they become available.

Lambda ESM for Amazon SQS also supports message filtering, which enables you to process only a subset of messages in a queue based on the contents of the message body.

## Polling
<a name="sqs-polling"></a>

Amazon SQS supports short polling and long polling of messages. Short polling queries a subset of servers to find available messages and returns them immediately. However, it might not return all available messages. This is useful when your application needs to consume messages as quickly as possible or cannot tolerate waiting for a longer period of time.

Long polling waits until a configurable amount of time has passed or a configurable number of messages have been received before returning the messages. This might reduce the number of *empty polls*, that is, the number of polls where no messages are returned, especially for queues that do not receive many messages. Reducing the number of empty polls can reduce your Amazon SQS costs, because this service charges for each request, and each polling operation is a request.

## Guidance
<a name="sqs-guidance"></a>

Queues are a good choice when:
+ You want to decouple components and do not need synchronous communication between them.
+ You are communicating between components that have different availability service-level agreements (SLAs) or service-level objectives (SLOs).
+ You generally have a single consumer for a set of messages.

Consider an alternate option if:
+ You need synchronous communication.
+ You need complicated routing logic to send messages to the correct consumer.
