---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/messaging.html
---

# Messaging
<a name="messaging"></a>

As discussed in the [Communication patterns](communication-patterns.md) section, you can use messaging to communicate either synchronously or asynchronously between services. There are many AWS serverless services to choose from, and your choice should be based on your integration needs. For example, if you require an ordered delivery of messages, you should choose a service such as Amazon Simple Queue Service (Amazon SQS) or Amazon Simple Notification Service (Amazon SNS). Both services support first in first out (FIFO) delivery, as opposed to Amazon EventBridge, which does not.

The following sections discuss these services in more detail.
