---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/data-store.html
---

# Data store
<a name="data-store"></a>

 The data store is used to persist data needed by the microservices. Popular stores for session data are in-memory caches such as Memcached or Redis. AWS offers both technologies as part of the managed [Amazon ElastiCache](https://aws.amazon.com/elasticache/) service.

 Putting a cache between application servers and a database is a common mechanism for reducing the read load on the database, which, in turn, may allow resources to be used to support more writes. Caches can also improve latency.

 Relational databases are still very popular to store structured data and business objects. AWS offers six database engines (Microsoft SQL Server, Oracle, MySQL, MariaDB, PostgreSQL, and [Amazon Aurora](https://aws.amazon.com/rds/aurora/)) as managed services through [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS).

 Relational databases, however, are not designed for endless scale, which can make it difficult and time intensive to apply techniques to support a high number of queries.

 NoSQL databases have been designed to favor scalability, performance, and availability over the consistency of relational databases. One important element of NoSQL databases is that they typically don’t enforce a strict schema. Data is distributed over partitions that can be scaled horizontally and is retrieved using partition keys.

 Because individual microservices are designed to do one thing well, they typically have a simplified data model that might be well suited to NoSQL persistence. It is important to understand that NoSQL databases have different access patterns than relational databases. For example, it's not possible to join tables. If this is necessary, the logic has to be implemented in the application. You can use [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) to create a database table that can store and retrieve any amount of data and serve any level of request traffic. DynamoDB delivers single-digit millisecond performance, however, there are certain use cases that require response times in microseconds. [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/) (DAX) provides caching capabilities for accessing data.

 DynamoDB also offers an automatic scaling feature to dynamically adjust throughput capacity in response to actual traffic. However, there are cases where capacity planning is difficult or not possible because of large activity spikes of short duration in your application. For such situations, DynamoDB provides an on-demand option, which offers simple pay-per-request pricing. DynamoDB on-demand is capable of serving thousands of requests per second instantly without capacity planning.

 For more information, see [Distributed data management](distributed-data-management.md) and [How to Choose a Database](https://aws.amazon.com/startups/learn/maximizing-performance-with-aws-databases).
