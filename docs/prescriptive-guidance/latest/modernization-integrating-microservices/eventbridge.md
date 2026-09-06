---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/eventbridge.html
---

# Amazon EventBridge
<a name="eventbridge"></a>

[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service and often acts as the foundation for an event-driven architecture (EDA). You can also use it to route and deliver messages asynchronously between microservices. Using EventBridge, producers publish events to a bus. You configure rules that match events based on their content and choose one or more targets that events matching that rule will be delivered to. EventBridge supports a [wide range of rule targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html). Using an event bus enables you to decouple producers from consumers and consolidate your routing and delivery logic.

In EventBridge, you can also create scheduled rules, so you can take actions at specific times. You can define events by using cron-based and rate-based expressions.

[EventBridge Pipes](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html) gives you the ability to pipe messages from a [source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-source.html) to a [target](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html) without using a compute service such as AWS Lambda. For example, let's say you have an SQS queue that receives messages, which should trigger an AWS Step Functions state machine. Instead of creating a Lambda function that has an event source mapping to consume messages from the queue, and writing code by using an AWS SDK to invoke the state machine, you can use EventBridge Pipes to do this for you without writing any custom code.

EventBridge is commonly used with other messaging services such as Amazon SQS and Amazon SNS. For example, delivering events to an SQS queue gives a receiving service the flexibility to consume messages when it's able, at a rate that is independent of the rate at which events are produced. Likewise, you can deliver events that should be fanned out to a large number of subscribers to an SNS topic.

## Guidance
<a name="eventbridge-guidance"></a>

Use EventBridge when:
+ You do not require synchronous communication between services.
+ You want to decouple message routing logic from your microservices. The microservices only produce events and publish them to the event bus, and interested services create rules to match and deliver those events.
+ You need to deliver messages from one supported service to another.

Consider other services in situations where:
+ You require strict ordering of events. In these cases, consider Amazon SQS FIFO queues or Amazon SNS FIFO topics. Alternatively, consider event stream services such as Amazon Kinesis Data Streams or Amazon Managed Streaming for Apache Kafka (Amazon MSK).
