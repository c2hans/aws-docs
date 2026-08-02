---
source_url: https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/amazon-memorydb-for-redis.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon MemoryDB
<a name="amazon-memorydb-for-redis"></a>

 [Amazon MemoryDB](https://aws.amazon.com/memorydb/) (MemoryDB) is a fully managed, in-memory database service. It is designed to provide high performance and low latency for applications that require fast and frequent access to data.

 Some of the key features of MemoryDB include:
+  **Compatibility** — Compatibility with Redis, an open-source, in-memory data store that is widely used for caching, near real-time analytics, and other high-performance applications. MemoryDB supports the same set of Redis data types and parameters, and requires no code change to migrate from Redis.
+  **Scalability** — Designed to be highly available and durable, with automatic failover and data replication across multiple Availability Zones for high availability and disaster recovery.
+  **Data durability** — Data is stored across multiple Availability Zones, while ensuring single-digit millisecond response using AWS proprietary architecture design.
+  **Support for security features** such as [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), encryption with [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS), and authentication and authorization with Redis ACLs.
+  **Flexibility** — Provides a number of features and capabilities to help you optimize your application's performance, including read and write replicas, Multi-AZ deployments, automatic scaling, and flexible pricing options based on usage. MemoryDB is well-suited for a wide range of use cases, including caching, near real-time analytics, and session stores. It is particularly useful for applications that require fast and frequent access to data, such as gaming, e-commerce, and advertising.

 Amazon NoSQL databases integrate with [AWS Identity and Access Management](https://aws.amazon.com/iam/) (AWS IAM) for access control and security. IAM allows you to manage access to your NoSQL databases by creating policies that define permissions for specific users, groups, or roles. You can use IAM to control access to specific tables or resources within your NoSQL databases, as well as to enforce fine-grained permissions for read and write operations.
