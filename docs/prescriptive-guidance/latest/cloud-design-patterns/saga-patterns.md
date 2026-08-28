---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-patterns.html
---

# Saga patterns
<a name="saga-patterns"></a>

A *saga* consists of a sequence of local transactions. Each local transaction in a saga updates the database and triggers the next local transaction. If a transaction fails, the saga runs compensating transactions to revert the database changes made by the previous transactions.

This sequence of local transactions helps achieve a business workflow by using continuation and compensation principles. The *continuation principle* decides the forward recovery of the workflow, whereas the *compensation principle* decides the backward recovery. If the update fails at any step in the transaction, the saga publishes an event for either continuation (to retry the transaction) or compensation (to go back to the previous data state). This ensures that data integrity is maintained and is consistent across the data stores.

For example, when a user purchases a book from an online retailer, the process consists of a sequence of transactions―such as order creation, inventory update, payment, and shipping―that represents a business workflow. In order to complete this workflow, the distributed architecture issues a sequence of local transactions to create an order in the order database, update the inventory database, and update the payment database. When the process is successful, these transactions are invoked sequentially to complete the business workflow, as the following diagram shows. However, if any of these local transactions fails, the system should be able to decide on an appropriate next step―that is, either a forward recovery or a backward recovery.

![Business workflows](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/dbf35a03-02f9-4292-8bb9-4e9f5d14a304.png)

The following two scenarios help determine whether the next step is forward recovery or backward recovery:
+ Platform-level failure, where something goes wrong with the underlying infrastructure and causes the transaction to fail. In this case, the saga pattern can perform a forward recovery by retrying the local transaction and continuing the business process.
+ Application-level failure, where the payment service fails because of an invalid payment. In this case, the saga pattern can perform a backward recovery by issuing a compensatory transaction to update the inventory and the order databases, and reinstate their previous state.

The saga pattern handles the business workflow and ensures that a desirable end state is reached through forward recovery. In case of failures, it reverts the local transactions by using backward recovery to avoid data consistency issues.

The saga pattern has two variants: choreography and orchestration.

## Saga choreography
<a name="saga-choreography.b4e15e2f-3ece-50df-8c0e-67858aee3561"></a>

The saga choreography pattern depends on the events published by the microservices. The saga participants (microservices) subscribe to the events and act based on the event triggers. For example, the order service in the following diagram emits an `OrderPlaced` event. The inventory service subscribes to that event and updates the inventory when the `OrderPlaced` event is emitted. Similarly, the participant services act based on the context of the emitted event.

The saga choreography pattern is suitable when there are only a few participants in the saga, and you need a simple implementation with no single point of failure. When more participants are added, it becomes harder to track the dependencies between the participants by using this pattern.

![Saga choreography pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/4e92e053-6d80-4959-9ffb-067d67d205d7.png)

## Saga orchestration
<a name="saga-orchestration.6a38a249-1551-54ac-a92b-4fce80cf3e99"></a>

The saga orchestration pattern has a central coordinator called an *orchestrator*. The saga orchestrator manages and coordinates the entire transaction lifecycle. It is aware of the series of steps to be performed to complete the transaction. To run a step, it sends a message to the participant microservice to perform the operation. The participant microservice completes the operation and sends a message back to the orchestrator. Based on the message it receives, the orchestrator decides which microservice to run next in the transaction.

The saga orchestration pattern is suitable when there are many participants, and loose coupling is required between saga participants. The orchestrator encapsulates the complexity in the logic by making the participants loosely coupled. However, the orchestrator can become a single point of failure because it controls the entire workflow.

![Saga orchestration pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/f2c495f6-ccfe-4488-9dc6-f0fd913c897d.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
