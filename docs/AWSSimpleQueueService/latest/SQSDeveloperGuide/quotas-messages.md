---
source_url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html
---

# Amazon SQS message quotas
<a name="quotas-messages"></a>

The following table lists quotas related to messages.

- **Batched message ID**
  - A batched message ID can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens (-), and underscores (\_).

- **Message attributes**
  - A message can contain up to 10 metadata attributes.

- **Message batch**
  - A single message batch request can include a maximum of 10 messages. For more information, see [Configuring AmazonSQSBufferedAsyncClient](sqs-client-side-buffering-request-batching.md#configuring-buffered-async-client) in the [Amazon SQS batch actions](sqs-batch-api-actions.md) section.

- **Message content**
  - A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed: `#x9` \| `#xA` \| `#xD` \| `#x20` to `#xD7FF` \| `#xE000` to `#xFFFD` \| `#x10000` to `#x10FFFF`<br />Any characters not included in this list are rejected. For more information, see the [W3C specification for characters](https://www.w3.org/TR/REC-xml/#charsets).

- **Message group ID**
  - `MessageGroupId` is required for FIFO queues. If you don't provide a `MessageGroupId` when sending a message to a FIFO queue, the action fails. In standard queues, using `MessageGroupId` enables [fair queues](sqs-fair-queues.md). We recommend that you include a `MessageGroupId` in all messages when using fair queues.<br />The length of `MessageGroupId` is 128 characters. Valid values: alphanumeric characters and punctuation `(!"#$%&'()*+,-./:;<=>?@[\]^_`{\|}~)`.

- **Message retention**
  - By default, a message is retained for 4 days. The minimum is 60 seconds (1 minute). The maximum is 1,209,600 seconds (14 days).

- **Message throughput**
  - **[Standard queues](standard-queues.md)**<br />Standard queues support a very high, nearly unlimited number of API calls per second, per action ([https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html), [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html), or [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html)). This high throughput makes them ideal for use cases that require processing large volumes of messages quickly, such as real-time data streaming or large-scale applications. While standard queues scale automatically with demand, it is essential to monitor usage patterns to ensure optimal performance, especially in regions with higher workloads.
  - **[FIFO queues ](sqs-fifo-queues.md)**[See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html)<br />**[High throughput for FIFO queues ](high-throughput-fifo.md)**<br />Amazon SQS FIFO limits are based on the number of API requests, not message limits. For high throughput mode, these API request limits are as follows:<br />**Transaction throughput limits (Non-batching API calls)**<br />These limits define how frequently each API operation (such as [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html), [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html), or [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html)) can be performed independently, ensuring efficient system performance within the allowed transactions per second (TPS).<br /> The following limits are based on non-batched API calls:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html)<br />**Maximizing throughput with batching**<br />Processes multiple messages in a single API call, which significantly increasing efficiency. Instead of handling each message individually, batching allows you to send, receive, or delete up to 10 messages in a single API request. This reduces the total number of API calls, allowing you to process more messages per second while staying within the transaction limits (TPS) for the region, maximizing throughput and system performance. For more information, see [Increasing throughput using horizontal scaling and action batching with Amazon SQS](sqs-throughput-horizontal-scaling-and-batching.md).<br />The following limits are based on batched API calls:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html)<br />**Optimizing throughput beyond batching**<br />While batching can greatly increase throughput, it’s important to consider other strategies for optimizing FIFO performance:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html)

- **Message timer**
  - The default (minimum) delay for a message is 0 seconds. The maximum is 15 minutes.

- **Message size**
  - The minimum message size is 1 byte (1 character). The maximum is 1,048,576 bytes (1 MiB).<br />To send messages larger than 1 MiB, you can use the [Amazon SQS Extended Client Library for Java](https://github.com/awslabs/amazon-sqs-java-extended-client-lib) and the [Amazon SQS Extended Client Library for Python](https://github.com/awslabs/amazon-sqs-python-extended-client-lib). This library allows you to send an Amazon SQS message that contains a reference to a message payload in Amazon S3. The maximum payload size is 2 GB. This extended library works only for synchronous clients.

- **Message visibility timeout**
  - The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours.

- **Policy information**
  - The maximum quota is 8,192 bytes, 20 statements, 50 principals, or 10 conditions. For more information, see [Amazon SQS policy quotas](quotas-policies.md).
