---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/service-per-team.html
---

# Event sourcing pattern
<a name="service-per-team"></a>

The event sourcing pattern is typically used with the CQRS pattern to decouple read from write workloads, and optimize for performance, scalability, and security. Data is stored as a series of events, instead of direct updates to data stores. Microservices replay events from an event store to compute the appropriate state of their own data stores. The pattern provides visibility for the current state of the application and additional context for how the application arrived at that state. The event sourcing pattern works effectively with the CQRS pattern because data can be reproduced for a specific event, even if the command and query data stores have different schemas.

By choosing this pattern, you can identify and reconstruct the application's state for any point in time. This produces a persistent audit trail and makes debugging easier. However, data becomes eventually consistent and this might not be appropriate for some use cases.

This pattern can be implemented by using either Amazon Kinesis Data Streams or Amazon EventBridge.

## Amazon Kinesis Data Streams implementation
<a name="amazon-kinesis"></a>

In the following illustration, Kinesis Data Streams is the main component of a centralized event store. The event store captures application changes as events and persists them on Amazon Simple Storage Service (Amazon S3).

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/images/guide-img/44ded022-4fc5-47f3-9dda-29ff14ee9ef8/images/843bc123-7084-4005-aa3d-d06876ab9beb.png)

The workflow consists of the following steps:

1. When the "/withdraw" or "/credit" microservices experience an event state change, they publish an event by writing a message into Kinesis Data Streams.

1. Other microservices, such as "/balance" or "/creditLimit," read a copy of the message, filter it for relevance, and forward it for further processing.

## Amazon EventBridge implementation
<a name="amazon-eventbridge"></a>

The architecture in the following illustration uses EventBridge. EventBridge is a serverless service that uses events to connect application components, which makes it easier for you to build scalable, event-driven applications. Event-driven architecture is a style of building loosely coupled software systems that work together by emitting and responding to events. EventBridge provides a [default event bus ](https://docs.aws.amazon.com/eventbridge/latest/userguide/create-event-bus.html)for events that are published by AWS services, and you can also create a [custom event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/create-event-bus.html) for domain-specific buses.

![Amazon EventBridge implementation of the event sourcing pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/images/guide-img/44ded022-4fc5-47f3-9dda-29ff14ee9ef8/images/d230e443-ac21-406e-966c-6e15b22457d2.png)

The workflow consists of the following steps:

1. "OrderPlaced" events are published by the "Orders" microservice to the custom event bus.

1. Microservices that need to take action after an order is placed, such as the "/route" microservice, are initiated by rules and targets.

1. These microservices generate a route to ship the order to the customer and emit a "RouteCreated" event.

1. Microservices that need to take further action are also initiated by the "RouteCreated" event.

1. Events are sent to an event archive (for example, EventBridge archive) so that they can be replayed for reprocessing, if required.

1. Historical order events are sent to a new Amazon Simple Queue Service (Amazon SQS) queue (replay queue) for reprocessing, if required.

1. If targets are not initiated, the affected events are placed in a dead letter queue (DLQ) for further analysis and reprocessing.

You should consider using this pattern if:
+ Events are used to completely rebuild the application's state.
+ You require events to be replayed in the system and that an application's state can be determined at any point in time.
+ You want to be able to reverse specific events without having to start with a blank application state.
+ Your system requires a stream of events that can easily be serialized to create an automated log.
+ Your system requires heavy read operations but is light on write operations; heavy read operations can be directed to an in-memory database, which is kept updated with the events stream.

***Important**: If you use the event sourcing pattern, you must deploy the Saga pattern to maintain data consistency across microservices.*
