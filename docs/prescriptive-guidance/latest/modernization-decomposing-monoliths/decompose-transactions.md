---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-transactions.html
---

# Decompose by transactions
<a name="decompose-transactions"></a>

In a distributed system, an application typically has to call multiple microservices to complete one business transaction. To avoid latency issues or two-phase commit problems, you can group your microservices based on transactions. This pattern is appropriate if you consider response times important and your different modules do not create a monolith after you package them. The following table explains the advantages and disadvantages of using this pattern.

|
|
| Advantages | Disadvantages |
| --- |--- |
| Faster response times.You don't have to worry about data consistency.Improved availability. | Multiple modules can be packaged together, and this can create a monolith.Multiple functionalities are implemented in a single microservice instead of separate microservices, which increases cost and complexity.Transaction-oriented microservices can grow if the number of business domains and dependencies among them is high.Inconsistent versions might be deployed at the same time for the same business domain. |

In the following illustration, the insurance monolith is broken down into multiple microservices based on transactions.

![Decompose by transactions pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/images/guide-img/8e9fa68d-7532-4c4b-8c7b-74bc6afdb7b9/images/7d8bfdf6-5aae-4d45-b891-9352d08ee666.png)

 In an insurance system, a claim request is typically tagged to a customer after it is submitted. This means that a claims service cannot exist without a *Customers* microservice. *Sales* and *Customers* are packaged together in one microservice package, and a business transaction requires coordination with both.
