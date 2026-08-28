---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/cqrs-pattern.html
---

# CQRS pattern
<a name="cqrs-pattern"></a>

The command query responsibility segregation (CQRS) pattern separates the data mutation, or the command part of a system, from the query part. You can use the CQRS pattern to separate updates and queries if they have different requirements for throughput, latency, or consistency. The CQRS pattern splits the application into two parts: the command side and the query side. The command side handles `create`, `update`, and `delete` requests. The query side runs the `query` part by using the read replicas.

![CQRS pattern](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/images/guide-img/44ded022-4fc5-47f3-9dda-29ff14ee9ef8/images/c7446d93-7ef4-4d44-9dff-ce1d5cdcf801.png)

The diagram shows the following process:

1. The business interacts with the application by sending commands through an API. Commands are actions such as creating, updating or deleting data.

1. The application processes the incoming command on the command side. This involves validating, authorizing, and running the operation.

1. The application persists the command's data in the write (command) database.

1. After the command is stored in the write database, events are triggered to update the data in the read (query) database.

1. The read (query) database processes and persists the data. Read databases are designed to be optimized for specific query requirements.

1. The business interacts with read APIs to send queries to the query side of the application.

1. The application processes the incoming query on the query side and retrieves the data from the read database.

You can implement the CQRS pattern by using various combinations of databases, including:
+ Using relational database management system (RDBMS) databases for both the command and the query side. Write operations go to the primary database and read operations can be routed to read replicas. Example: [Amazon RDS read replicas](https://aws.amazon.com/rds/features/read-replicas/)
+ Using an RDBMS database for the command side and a NoSQL database for the query side. Example: [Modernize legacy databases using event sourcing and CQRS with AWS DMS](https://aws.amazon.com/blogs/database/modernize-legacy-databases-using-event-sourcing-and-cqrs-with-aws-dms/)
+ Using NoSQL databases for both the command and the query side. Example: [Build a CQRS event store with Amazon DynamoDB](https://aws.amazon.com/blogs/database/build-a-cqrs-event-store-with-amazon-dynamodb/)
+ Using a NoSQL database for the command side and an RDBMS database for the query side, as discussed in the following example.

In the following illustration, a NoSQL data store, such as DynamoDB, is used to optimize the write throughput and provide flexible query capabilities. This achieves high write scalability on workloads that have well-defined access patterns when you add data. A relational database, such as Amazon Aurora, provides complex query functionality. A DynamoDB stream sends data to a Lambda function that updates the Aurora table.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/images/guide-img/44ded022-4fc5-47f3-9dda-29ff14ee9ef8/images/48a87da4-6fcd-458a-9dd9-8078171e188f.png)

Implementing the CQRS pattern with DynamoDB and Aurora provides these key benefits:
+ DynamoDB is a fully managed NoSQL database that can handle high-volume write operations, and Aurora offers high read scalability for complex queries on the query side.
+ DynamoDB provides low-latency, high-throughput access to data, which makes it ideal for handling command and update operations, and Aurora performance can be fine-tuned and optimized for complex queries.
+ Both DynamoDB and Aurora offer serverless options, which enables your business to pay for resources based on usage only.
+ DynamoDB and Aurora are fully managed services, which reduces the operational burden of managing databases, backups and scalability.

You should consider using the CQRS pattern if:
+ You implemented the database-per-service pattern and want to join data from multiple microservices.
+ Your read and write workloads have separate requirements for scaling, latency, and consistency.
+ Eventual consistency is acceptable for the read queries.

**Important**
The CQRS pattern typically results in eventual consistency between the data stores.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
