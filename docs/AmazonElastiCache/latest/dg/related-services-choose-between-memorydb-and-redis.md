---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/related-services-choose-between-memorydb-and-redis.html
---

# Related services
<a name="related-services-choose-between-memorydb-and-redis"></a>

[MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb-for-redis.html)

When deciding whether to use ElastiCache or MemoryDB consider the following comparisons:
+ ElastiCache is a service that is commonly used to cache data from other databases and data stores using Valkey, Memcached, or Redis OSS. You should consider ElastiCache for caching workloads where you want to accelerate data access with your existing primary database or data store (microsecond read and write performance). You should also consider ElastiCache for use cases where you want to use Valkey or Redis OSS data structures and APIs to access data stored in a primary database or data store.
+ ElastiCache can also help you save database costs by storing frequently accessed data in a cache. If your application has high read throughput requirements, you can achieve high scale, fast performance, and lowered data storage costs by using ElastiCache, instead of scaling your underlying database.
+ With *durability enabled*, ElastiCache for Valkey can also serve as a durable datastore with microsecond read latency and single-digit millisecond write latency (synchronous writes) or microsecond write latency (asynchronous writes). For more information, see [Durability in ElastiCache](durability.md).
+ MemoryDB is a durable, in-memory database for workloads that require an ultra-fast, primary database. It is compatible with Valkey and Redis OSS. You should consider using MemoryDB if your workload requires *multi-Region active-active replication with conflict-free data types (CRDTs)*. For single-Region durable workloads, consider using ElastiCache with durability enabled.

[Amazon Relational Database Service](https://aws.amazon.com/rds/)

For further background information on the related Amazon Relational Database Service service, see [Amazon RDS](https://docs.aws.amazon.com/rds/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
