---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-choreography.html
---

# Saga choreography pattern

## Intent
<a name="saga-choreography-intent"></a>

The saga choreography pattern helps preserve data integrity in distributed transactions that span multiple services by using event subscriptions. In a distributed transaction, multiple services can be called before a transaction is completed. When the services store data in different data stores, it can be challenging to maintain data consistency across these data stores.

## Motivation
<a name="saga-choreography-motivation"></a>

A *transaction* is a single unit of work that might involve multiple steps, where all steps are completely executed or no step is executed, resulting in a data store that retains its consistent state. The terms *atomicity, consistency, isolation, and durability (ACID)* define the properties of a transaction. Relational databases provide ACID transactions to maintain data consistency.

To maintain consistency in a transaction, relational databases use the two-phase commit (2PC) method. This consists of a *prepare phase* and a *commit phase*.
+ In the prepare phase, the coordinating process requests the transaction's participating processes (participants) to promise to either commit or roll back the transaction.
+ In the commit phase, the coordinating process requests the participants to commit the transaction. If the participants cannot agree to commit in the prepare phase, the transaction is rolled back.

In distributed systems that follow a database-per-service design pattern, the two-phase commit is not an option. This is because each transaction is distributed across various databases, and there is no single controller that can coordinate a process that's similar to the two-phase commit in relational data stores. In this case, one solution is to use the saga choreography pattern.

## Applicability
<a name="saga-choreography-applicability"></a>

Use the saga choreography pattern when:
+ Your system requires data integrity and consistency in distributed transactions that span multiple data stores.
+ The data store (for example, a NoSQL database) doesn't provide 2PC to provide ACID transactions, you need to update multiple tables within a single transaction, and implementing 2PC within the application boundaries would be a complex task.
+ A central controlling process that manages the participant transactions might become a single point of failure.
+ The saga participants are independent services and need to be loosely coupled.
+ There is communication between bounded contexts in a business domain.

## Issues and considerations
<a name="saga-choreography-issues"></a>
+ **Complexity: **As the number of microservices increases, saga choreography can become difficult to manage because of the number of interactions between the microservices. Additionally, compensatory transactions and retries add complexities to the application code, which can result in maintenance overhead. Choreography is suitable when there are only a few participants in the saga, and you need a simple implementation with no single point of failure. When more participants are added, it becomes harder to track the dependencies between the participants by using this pattern.
+ **Resilient implementation:** In saga choreography, it's more difficult to implement timeouts, retries, and other resiliency patterns globally, compared with saga orchestration. Choreography must be implemented on individual components instead of at an orchestrator level.
+ **Cyclic dependencies:** The participants consume messages that are published by one another. This might result in cyclic dependencies, leading to code complexities and maintenance overheads, and possible deadlocks.
+ **Dual writes issue: **The microservice has to atomically update the database and publish an event. The failure of either operation might lead to an inconsistent state. One way to solve this is to use the [transactional outbox pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html).
+ **Preserving events: **The saga participants act based on the events published. It's important to save the events in the order they occur for audit, debugging, and replay purposes. You can use the [event sourcing pattern](event-sourcing-pattern.md) to persist the events in an event store in case a replay of the system state is required to restore data consistency. Event stores can also be used for auditing and troubleshooting purposes because they reflect every change in the system.
+ **Eventual consistency**: The sequential processing of local transactions results in eventual consistency, which can be a challenge in systems that require strong consistency. You can address this issue by setting your business teams' expectations for the consistency model or reassess the use case and switch to a database that provides strong consistency.
+ **Idempotency**: Saga participants have to be idempotent to allow repeated execution in case of transient failures that are caused by unexpected crashes and orchestrator failures.
+ **Transaction isolation**: The saga pattern lacks transaction isolation, which is one of the four properties in ACID transactions. The [degree of isolation](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-isolation-levels.html) of a transaction determines how much other concurrent transactions can affect the data that the transaction operates on. Concurrent orchestration of transactions can lead to stale data. We recommend using semantic locking to handle such scenarios.
+ **Observability**: Observability refers to detailed logging and tracing to troubleshoot issues in the implementation and orchestration process. This becomes important when the number of saga participants increases, resulting in complexities in debugging. End-to-end monitoring and reporting are more difficult to achieve in saga choreography, compared with saga orchestration.
+ **Latency issues**: Compensatory transactions can add latency to the overall response time when the saga consists of several steps. If the transactions make synchronous calls, this can increase the latency further.

## Implementation
<a name="saga-choreography-implementation"></a>

### High-level architecture
<a name="high-level-architecture.c5bdb488-d1d4-511c-bbc4-8f4520543a91"></a>

In the following architecture diagram, the saga choreography has three participants: the order service, the inventory service, and the payment service. Three steps are required to complete the transaction: T1, T2, and T3. Three compensatory transactions restore the data to the initial state: C1, C2, and C3.

![Saga choreography high-level architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/47da4cc0-42bf-4dda-9f6e-4d428d3029cc.png)

+ The order service runs a local transaction, T1, which atomically updates the database and publishes an `Order placed` message to the message broker.
+ The inventory service subscribes to the order service messages and receives the message that an order has been created.
+ The inventory service runs a local transaction, T2, which atomically updates the database and publishes an `Inventory updated` message to the message broker.
+ The payment service subscribes to the messages from the inventory service and receives the message that the inventory has been updated.
+ The payment service runs a local transaction, T3, which atomically updates the database with payment details and publishes a `Payment processed` message to the message broker.
+ If the payment fails, the payment service runs a compensatory transaction, C1, which atomically reverts the payment in the database and publishes a `Payment failed` message to the message broker.
+ The compensatory transactions C2 and C3 are run to restore data consistency.

### Implementation using AWS services
<a name="implementation-using-aws-services.909028d3-b101-5d57-844b-ef9bbc096ecd"></a>

You can implement the saga choreography pattern by using Amazon EventBridge. EventBridge uses events to connect application components. It processes events through event buses or pipes. An event bus is a router that receives [events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) and delivers them to zero or more destinations, or *targets*.[ Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) associated with the event bus evaluate events as they arrive and send them to [targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) for processing.

In the following architecture:
+ The microservices—order service, inventory service, and payment service—are implemented as Lambda functions.
+ There are three custom EventBridge buses: `Orders` event bus, `Inventory` event bus, and `Payment` event bus.
+ `Orders` rules, `Inventory` rules, and `Payment` rules match the events that are sent to the corresponding event bus and invoke the Lambda functions.

![Implementing the saga choreography pattern with AWS services](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/1cf0c140-a52d-4280-8d9a-6e54ef28b04b.png)

In a successful scenario, when an order is placed:

1. The order service processes the request and sends the event to the `Orders` event bus*.*

1. The `Orders` rules match the events and starts the inventory service*.*

1. The inventory service updates the inventory and sends the event to the `Inventory` event bus.

1. The `Inventory` rules match the events and start the payment service.

1. The payment service processes the payment and sends the event to the `Payment` event bus.

1. The `Payment` rules match the events and send the `Payment processed` event notification to the listener.

   Alternatively, when there is an issue in order processing, the EventBridge rules start the compensatory transactions for reverting the data updates to maintain data consistency and integrity.

1. If the payment fails, the `Payment` rules process the event and start the inventory service*. *The inventory service runs compensatory transactions to revert the inventory.

1. When the inventory has been reverted, the inventory service sends the `Inventory reverted` event to the `Inventory` event bus*. *This event is processed by `Inventory` rules*. *It starts the order service*, *which runs the compensatory transaction to remove the order.

## Related content
<a name="saga-choreography-resources"></a>
+ [Saga orchestration pattern](saga-orchestration.md)
+ [Transactional outbox pattern](transactional-outbox.md)
+ [Retry with backoff pattern](retry-backoff.md)
