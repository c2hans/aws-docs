---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/saga-pattern.html
---

# Saga pattern
<a name="saga-pattern"></a>

The saga pattern is a failure management pattern that helps establish consistency in distributed applications, and coordinates transactions between multiple microservices to maintain data consistency. A microservice publishes an event for every transaction, and the next transaction is initiated based on the event's outcome. It can take two different paths, depending on the success or failure of the transactions.

The following illustration shows how the saga pattern implements an order processing system by using AWS Step Functions. Each step (for example, "ProcessPayment") also has separate steps to handle the success (for example, "UpdateCustomerAccount") or failure (for example, "Cancel Order") of the process.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/images/guide-img/44ded022-4fc5-47f3-9dda-29ff14ee9ef8/images/5999cebf-dc27-4e54-ac0f-78f8159e2d91.png)

You should consider using this pattern if:
+ The application needs to maintain data consistency across multiple microservices without tight coupling.
+ There are long-lived transactions and you don't want other microservices to be blocked if one microservice runs for a long time.
+ You need to be able to roll back if an operation fails in the sequence.

**Important**
The saga pattern is difficult to debug and its complexity increases with the number of microservices. The pattern requires a complex programming model that develops and designs compensating transactions for rolling back and undoing changes.
