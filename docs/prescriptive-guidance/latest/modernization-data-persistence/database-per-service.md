---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/database-per-service.html
---

# Database-per-service pattern
<a name="database-per-service"></a>

Loose coupling is the core characteristic of a microservices architecture, because each individual microservice can independently store and retrieve information from its own data store. By deploying the database-per-service pattern, you choose the most appropriate data stores (for example, relational or non-relational databases) for your application and business requirements. This means that microservices don't share a data layer, changes to a microservice's individual database do not impact other microservices, individual data stores cannot be directly accessed by other microservices, and persistent data is accessed only by APIs. Decoupling data stores also improves the resiliency of your overall application, and ensures that a single database can't be a single point of failure.

In the following illustration, different AWS databases are used by the "Sales," "Customer," and "Compliance" microservices. These microservices are deployed as AWS Lambda functions and accessed through an Amazon API Gateway API. AWS Identity and Access Management (IAM) policies ensure that data is kept private and not shared among the microservices. Each microservice uses a database type that meets its individual requirements; for example, "Sales" uses Amazon Aurora, "Customer" uses Amazon DynamoDB, and "Compliance" uses Amazon Relational Database Service (Amazon RDS) for SQL Server.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/images/guide-img/44ded022-4fc5-47f3-9dda-29ff14ee9ef8/images/138cae6b-aec5-4c5e-bfce-deba6133876c.png)

You should consider using this pattern if:
+ Loose coupling is required between your microservices.
+ Microservices have different compliance or security requirements for their databases.
+ More granular control of scaling is required.

There are the following disadvantages to using the database-per-service pattern:
+ It might be challenging to implement complex transactions and queries that span multiple microservices or data stores.
+ You have to manage multiple relational and non-relational databases.
+ Your data stores must meet two of the [CAP theorem](https://www.ibm.com/cloud/learn/cap-theorem) requirements: *consistency*, *availability*, or *partition tolerance*.

**Note**
If you use the database-per-service pattern, you must deploy another pattern to implement queries that span multiple microservices. You can use the API composition pattern (which you can speed up with the CQRS pattern) or the event sourcing pattern to create aggregated results.
