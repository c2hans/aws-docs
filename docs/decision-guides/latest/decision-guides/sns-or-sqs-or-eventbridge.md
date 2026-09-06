---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/sns-or-sqs-or-eventbridge.html
---

# Amazon SQS, Amazon SNS, or Amazon EventBridge?
<a name="sns-or-sqs-or-eventbridge"></a>

**Understand the differences and pick the one that's right for you**

|  |  |
| --- |--- |
| **Purpose** | Understand the differences between Amazon SQS, Amazon SNS, and EventBridge and determine which service is the best fit for your needs. |
| **Last updated** | November, 2025 |
| **Covered services** |  +  [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) <br />+  [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) <br />+  [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)   |

## Introduction
<a name="introduction"></a>

 This decision guide helps you to choose the best AWS service for message handling, event-driven architectures, and decoupling components for your application. AWS offers three key services for these purposes:
+  **Amazon SQS** is a fully managed message queuing service that enables decoupling and scaling of microservices, distributed systems, and serverless applications.
+  **Amazon SNS** is a fully managed publish-subscribe (pub/sub) messaging model that delivers messages to subscribed endpoints such as HTTP/HTTPS endpoints, email addresses, SMS, Amazon SQS queues, and AWS Lambda functions.
+  **Amazon EventBridge**(formerly known as CloudWatch Events) is a fully managed event bus service for event-driven architectures that can send and receive event data from a variety of sources including Lambda functions, Amazon SQS queues, Amazon SNS topics, and integrated SaaS applications.

All three of these services facilitate communication between decoupled components, but differ in underlying architecture, use cases, and capabilities.

The following table compares these services at a high level.

|  **Category**  |  **Amazon SQS**  |  **Amazon SNS**  |  **EventBridge**  |
| --- | --- | --- | --- |
|  Communication model  |  Pull-based (consumers poll messages from the queue)  |  Push-based (subscribers receive messages when published)  |  Event-driven (rules match events and route to targets)  |
|  Persistence  |  Messages persist until consumed or expired  |  Messages do not persist; delivered in real-time to subscribers  |  Events do not persist; processed in real-time  |
|  Delivery guarantees  |  At-least-once delivery  |  At-least-once delivery for HTTP/S, exactly-once for Lambda and Amazon SQS  |  At-least-once delivery  |
|  Message ordering  |  FIFO (First-In-First-Out) queues ensure strict ordering  |  Amazon SNS FIFO topics guarantee order  |  No ordering guarantees  |
|  Message filtering  |  Amazon SQS can’t decide consumer based on message. Use Amazon SNS message filtering with Amazon SQS to achieve.  |  Message filtering using subscription filter policies based on message metadata and for FIFO topics, message content  |  Complex event pattern matching and content-based filtering  |
|  Supported subscribers  |  Pull-based consumers (such as Amazon EC2 or Lambda)  |  HTTP/S endpoints, email, SMS, mobile push, Lambda, Amazon SQS  |  AWS services, Lambda, API destinations, event buses in other AWS accounts  |
|  Typical use cases  |  Decoupling microservices, buffering requests, processing tasks asynchronously  |  Fanout notifications, pub/sub messaging, mobile push notifications  |  Event-driven architectures, real-time stream processing, cross-account event sharing  |
|  Integration with other AWS services  |  Lambda, CloudWatch, AWS KMS, IAM  |  Lambda, Amazon SQS, Mobile Push, AWS KMS, IAM  |  Lambda, Step Functions, Amazon SQS, Amazon SNS, Kinesis, SageMaker AI, CloudWatch, IAM  |

## Details on the differences
<a name="sqs-sns-eb-differences"></a>

 The following tabbed sections compare Amazon SQS, Amazon SNS, and EventBridge in eight key areas.

------
#### [ Communication model ]

**Amazon SQS**

Pull-based model where consumers actively poll messages from the queue, allowing for fine-grained control over message processing rates and independent scaling of consumers. Amazon SQS supports both short polling (immediate response) and long polling, with a maximum wait time of up to 20 seconds. Long polling helps control the cost of using Amazon SQS by reducing the potential for empty responses.

**Amazon SNS**

 Push-based model that delivers messages to subscriptions such as HTTP/HTTPS endpoints, email addresses, SMS, Amazon SQS queues, and AWS Lambda functions. Messages are delivered asynchronously with built-in retry logic and dead-letter queue support.

**Amazon EventBridge**

 Event-driven model that matches events against rules, delivering messages to targets such as AWS services, integrated SaaS applications, and custom applications, enabling loosely-coupled, event-driven architectures.

------
#### [ Persistence and delivery guarantees ]

**Amazon SQS**

Messages are persisted in the queue until successfully processed or expired (up to 14 days retention). Provides at-least-once delivery, guaranteeing that every message is delivered at least once, with the possibility of duplicates.

**Amazon SNS**

Messages are not persisted and are delivered to subscribers in real-time. Offers at-least-once delivery for HTTP/S subscribers and exactly-once delivery for Lambda and Amazon SQS subscribers.

**Amazon EventBridge**

Amazon EventBridge processes events in real-time and doesn't persist events. At-least-once delivery is guaranteed to targets, which means events may be delivered multiple times. By default, Amazon EventBridge retries sending events for 24 hours and up to 185 times with an exponential back off and jitter, or randomized delay.

------
#### [ Message ordering ]

**Amazon SQS and Amazon SNS**

Amazon SQS FIFO queues and Amazon SNS FIFO topics support First-In-First-Out guaranteed message ordering, making them suitable for scenarios requiring sequential processing. See [message ordering details for FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/fifo-topic-message-ordering.html) for more information on message ordering using Amazon SNS and Amazon SQS.

**Amazon EventBridge**

EventBridge does not provide message ordering guarantees, instead delivering events to targets in an arbitrary order.

------
#### [ Message filtering and routing ]

**Amazon SQS**

Offers basic filtering capabilities through visibility timeouts (to prevent duplicate processing) and dead-letter queues (to handle failed messages).

**Amazon SNS**

Provides message filtering using subscription filter policies, allowing subscribers to selectively receive messages based on message attributes.

**Amazon EventBridge**

Supports advanced event pattern matching and content-based filtering, enabling fine-grained event processing and routing based on event content.

------
#### [ Supported subscribers and integrations ]

**Amazon SQS**

Supports pull-based consumers, such as Amazon EC2 instances or Lambda functions, which actively retrieve messages from the queue.

**Amazon SNS**

Supports a wide range of subscribers, including HTTP/S endpoints, email, SMS, mobile push notifications, Lambda functions, and Amazon SQS queues.

**Amazon EventBridge**

Integrates with numerous AWS services, such as Lambda, Step Functions, Amazon SQS, Amazon SNS, Kinesis, and SageMaker AI, allowing event routing based on predefined rules. EventBridge also has numerous built-in integrations with third party products such as PagerDuty, DataDog, New Relic. To see the complete list visit [Amazon EventBridge targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html).

------
#### [ Typical use cases ]

**Amazon SQS**

Commonly used for decoupling microservices, buffering requests, and processing tasks asynchronously, enabling independent scaling and graceful failure handling.

**Amazon SNS**

Often used for fanout notifications, pub/sub messaging, and mobile push notifications, facilitating the broadcasting of messages to multiple subscribers simultaneously.

**Amazon EventBridge**

Ideal for building event-driven architectures, real-time stream processing, and cross-account event sharing, allowing reactive systems to be built across multiple services.

------
#### [ Scalability and performance ]

**Amazon SQS**

Highly scalable, automatically scaling based on the number of messages and consumers, providing high throughput for message processing.

**Amazon SNS**

Highly scalable, capable of delivering messages to a large number of subscribers, with elastic scaling to handle increasing publish and subscribe demands.

**Amazon EventBridge**

Automatically scales based on incoming event traffic, offering low-latency event processing and near real-time delivery to targets.

------
#### [ Pricing ]

**Amazon SQS**

Pricing based on the number of API requests and data transferred, with a free tier including a monthly allowance of free API requests and data transfer.

**Amazon SNS**

Pricing is based on the number of API requests, notifications delivered, and data transferred. Amazon SNS SMS messages are billed through AWS End User Messaging.

**Amazon EventBridge**

Pricing based on the number of events published and target invocations, with a free tier that includes a monthly allowance of free events and invocations.

------

## Use
<a name="use"></a>

------
#### [ Amazon SQS ]
+  **Get started with Amazon SQS**

  Get step-by-step instructions on setting up and using Amazon SQS. It covers topics such as creating a queue, sending and receiving messages, and configuring queue properties.

  [Explore the guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)
+  **Amazon SQS tutorial**

  Walk through a practical example of using Amazon SQS to decouple the components of a simple application. It demonstrates how to create a queue, send messages to the queue, and process messages from the queue using AWS SDKs.

  [Explore the tutorial](https://aws.amazon.com/getting-started/hands-on/send-messages-distributed-applications/)
+  **Send Fanout Event Notifications**

  Learn how to implement a fanout messaging scenario using Amazon SQS and Amazon SNS.

  [Explore the tutorial](https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/)

------
#### [ Amazon SNS ]
+  **Get started with Amazon SNS**

  A step-by-step walkthrough of setting up and using Amazon SNS. It covers topics such as creating a topic, subscribing endpoints to a topic, publishing messages, and configuring access permissions.

  [Explore the guide](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html)
+  **Amazon SNS - Troubleshooting**

  Learn how to view configuration information, monitor processes, and gather diagnostic data about Amazon SNS.

  [Explore the course](https://explore.skillbuilder.aws/learn/course/external/view/elearning/14124/amazon-simple-notification-service-amazon-sns-troubleshooting)

------
#### [ EventBridge ]
+  **Amazon EventBridge User Guide**

  This comprehensive documentation covers topics such as creating event buses, defining event rules, setting up targets, and integrating with various AWS services.

   [Explore the guide ](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
+  **Amazon EventBridge Tutorials**

  The AWS documentation offers a series of tutorials that walk users through different use cases and scenarios using Amazon EventBridge. These tutorials cover topics like scheduling automated tasks, reacting to changes in AWS resources, and integrating with AWS services.

   [Explore the tutorials](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial.html)
+  **AWS Serverless Workshops - Event-Driven Architecture**

  Build event-driven architectures using Amazon EventBridge and other AWS serverless services. This workshop guides participants through the process of creating event buses, defining event rules, and triggering actions based on events.

  [Explore the workshop](https://event-driven-architecture.workshop.aws/)
+  **AWS Online Tech Talk - Introduction to Amazon EventBridge**

  Get an introduction to Amazon EventBridge, explaining key concepts, features, and use cases. The tech talk includes demonstrations and practical examples to help users understand how to leverage EventBridge in their applications.

  [Watch the video](https://www.youtube.com/watch?v=TXh5oU_yo9M)
+  **Building Event-Driven Applications with Amazon EventBridge**

  This blog post explores the process of building event-driven applications using Amazon EventBridge. It provides a step-by-step guide on creating event buses, defining event patterns, and setting up targets to process events.

   [Read the blog post](https://aws.amazon.com/blogs/compute/building-an-event-driven-application-with-amazon-eventbridge/)
+  **Create Point-to-Point Integrations Between Event Producers and Consumers with Amazon EventBridge Pipes**

  Explore Amazon EventBridge Pipes, a feature of EventBridge that makes it easier for you to build event-driven applications by providing a consistent and cost-effective way to create point-to-point integrations between event producers and consumers, removing the need to write undifferentiated glue code.

   [Read the blog post](https://aws.amazon.com/blogs/aws/new-create-point-to-point-integrations-between-event-producers-and-consumers-with-amazon-eventbridge-pipes/)

------
