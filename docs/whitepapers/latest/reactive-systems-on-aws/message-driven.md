---
source_url: https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/message-driven.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Message driven
<a name="message-driven"></a>

 A message-driven architecture uses messages to communicate between decoupled services and is common in modern applications built with microservices, since asynchronous message-passing between loosely coupled services helps to ensure isolation and provides location transparency. The following section discusses different messaging patterns and how these can be implemented on AWS.

## Event sourcing and CQRS
<a name="cqrs"></a>

 In the context of microservices architectures, event sourcing decouples different parts of an application by using a publish/subscribe pattern, and it feeds the same event data into different data models for separate microservices. Event sourcing is frequently used in conjunction with the Command Query Responsibility Segregation (CQRS) pattern to decouple read from write workloads and optimize both for performance, scalability, and security. Updates and queries are conventionally completed using a single datastore. You can use CQRS to separate these two workloads if they have different access patterns for throughput, latency, or consistency. When you separate command and query functions, you can scale them independently.

## AWS messaging services
<a name="aws-msg-services"></a>

AWS messaging services enable different software systems and end devices - often using different programming languages, and on different platforms - to communicate and exchange information. Amazon Kinesis Data Streams is a scalable and durable real-time *data streaming* service. A data stream is a logical grouping of shards, each shard is an append-only log and a unit of streaming capability. It contains an ordered sequence of records ordered by arrival time. In the example architecture Kinesis Data Streams is used to decouple services. Another option would be to use Amazon Managed Streaming for Apache Kafka (Amazon MSK), a fully-managed service that enables you to build and run applications that use Apache Kafka to process streaming data. Amazon MSK provides the control-plane operations, such as those for creating, updating, and deleting clusters. It lets you use Apache Kafka data-plane operations, such as those for producing and consuming data. One of the major advantages of services like Kinesis Data Streams or Amazon MSK is the ability to replay events within a defined *retention period.*

 A different pattern is *publish/subscribe* (pub/sub) *messaging*. It is a form of asynchronous service-to-service communication used in serverless and microservices architectures. In a pub/sub model, any message published to a topic is immediately received by all of the subscribers to the topic. Amazon SNS is a fully managed pub/sub messaging service that enables message delivery to millions of subscribers. Amazon SQS is a message queue service used by distributed applications to exchange messages through a polling model, and can be used to decouple sending and receiving components—without requiring each component to be concurrently available. Using Amazon SNS and Amazon SQS together, messages can be delivered to applications that require immediate notification of an event, and also persisted in an Amazon SQS queue for other applications to process at a later time. When you subscribe one or more Amazon SQS queues to an Amazon SNS topic, you can publish a message to the topic and Amazon SNS sends an Amazon SQS message to each of the subscribed queues.

![Diagram showing Pub/Sub with Amazon SNS and Amazon SQS](https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/images/pub-sub.png)

 If you already have applications designed to use industry standard APIs and protocols for messaging, including JMS, NMS, AMQP 1.0 and 0.9.1, STOMP, MQTT, and WebSocket. Amazon offers [Amazon MQ](https://aws.amazon.com/amazon-mq/), a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud. For brand new applications in the cloud, it is recommended you consider Amazon SQS and Amazon SNS. Amazon SQS and SNS are lightweight, fully managed message queue and topic services that scale almost infinitely. For existing applications using industry standard APIs and protocols, Amazon MQ is a proposed service.

## Fanout
<a name="fanout"></a>

The *Fanout* scenario is when a message published is replicated and pushed to multiple endpoints, which allows for parallel asynchronous processing. For example, you can develop an application that publishes a message to an SNS topic whenever an order is placed for a product. Then, Amazon Simple Queue Service (Amazon SQS) queues that are subscribed to the [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) topic receive identical notifications for the new order. A service attached to one of the SQS queues can handle the processing or fulfillment of the order.

## Filtering
<a name="filtering"></a>

 By default, an Amazon SNS topic subscriber receives every message published to the topic. To receive a subset of the messages, a subscriber must assign a *filter policy* to the topic subscription. A filter policy is a simple JSON object containing attributes that define which messages the subscriber receives. When you publish a message to a topic, Amazon SNS compares the message attributes to the attributes in the filter policy for each of the topic's subscriptions. If any of the attributes match, Amazon SNS sends the message to the subscriber. Otherwise, Amazon SNS skips the subscriber without sending the message.
