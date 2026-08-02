---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ccm-and-qpm-aurora-postgresql/cluster-cache-management.html
---

# Cluster cache management
<a name="cluster-cache-management"></a>

Caching is one of the most important features of any database (DB) because it helps reduce the disk I/O. The most frequently accessed data is stored in a memory area called the *buffer cache*. When a query runs frequently, it retrieves the data directly from the cache instead of the disk. This is faster and provides better scalability and application performance. You configure PostgreSQL cache size by using the `shared_buffers` parameter. For more information, see [Memory](https://www.postgresql.org/docs/current/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY) (PostgreSQL documentation).

After a failover, [cluster cache management (CCM)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.cluster-cache-mgmt.html) in Amazon Aurora PostgreSQL-Compatible Edition is designed to improve application and database recovery performance. In a typical failover situation without CCM, you might see a temporary but significant performance degradation. This occurs because when the failover DB instance starts, the buffer cache is empty. An empty cache is also known as a *cold cache*. The DB instance must read from the disk, which is slower than reading from the cache.

When you implement CCM, you choose a preferred *reader* DB instance, and CCM continuously synchronizes its cache memory with that of the primary, or *writer*, DB instance. If a failover occurs, the preferred reader DB instance is promoted to the new writer DB instance. Because it already has a cache memory, known as a *warm cache*, this minimizes the impact of the failover on the application performance.

## How does cluster cache management work?
<a name="ccm-operation"></a>

Failover DB instances are located in different availability zones from the primary, writer DB instance. The preferred reader DB instance is the priority failover target, which is specified by assigning it the **tier-0** priority level.

|
|
| Note: The promotion tier priority is a value that specifies the order in which an Aurora reader is promoted to the writer DB instance after a failure. Valid values are 0–15, where 0 is the first priority and 15 is the last priority. For more information about the promotion tier, see [Fault tolerance for an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html#Aurora.Managing.FaultTolerance). Modifying the promotion tier doesn't cause an outage. |
| --- |

CCM synchronizes the cache from the writer DB instance to the preferred reader DB instance. The reader DB instance sends the set of buffer addresses that are currently cached to the writer DB instance as a bloom filter. A *bloom filter* is a probabilistic, memory-efficient data structure that is used to test whether an element is a member of a set. Using a bloom filter prevents the reader DB instance from sending the same buffer addresses to the writer DB instance repeatedly. When the writer DB instance receives the bloom filter, it compares the blocks in its buffer cache and sends frequently used buffers to the reader DB instance. By default, a buffer is considered frequently used if it has a usage count greater than three.

The following diagram shows how CCM synchronizes the buffer cache of the writer DB instance with the preferred reader DB instance.

![Cluster cache management configured between Aurora DB instances in different Availability Zones.](http://docs.aws.amazon.com/prescriptive-guidance/latest/ccm-and-qpm-aurora-postgresql/images/guide-img/cffef437-8218-4d17-8fd1-5311668dbe92/images/533e323b-b2a7-4560-b033-18034e76f15c.png)

For more information about CCM, see [Fast recovery after failover with cluster cache management for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.cluster-cache-mgmt.html) (Aurora documentation) and [Introduction to Aurora PostgreSQL cluster cache management](https://aws.amazon.com/blogs/database/introduction-to-aurora-postgresql-cluster-cache-management/) (AWS blog post). For instructions about how to configure CCM, see [Configuring cluster cache management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.cluster-cache-mgmt.html#AuroraPostgreSQL.cluster-cache-mgmt.Configure) (Aurora documentation).

## Limitations
<a name="ccm-limitations"></a>

The CCM feature has the following limitations:
+ The reader DB instance must have the same DB instance class type and size as the writer DB instance, such as `r5.2xlarge` or `db.r5.xlarge`.
+ CCM is not supported for Aurora PostgreSQL DB clusters that are part of Aurora global databases.

## Use cases for CCM
<a name="ccm-use-cases"></a>

For some industries, such as retail, banking, and finance, delays of only a few milliseconds can cause application performance issues and result in a significant loss of business. Because CCM helps recover application and database performance by continuously synchronizing the buffer cache of the primary database instance to the preferred backup instance, it can help prevent businesses losses associated with failovers.
