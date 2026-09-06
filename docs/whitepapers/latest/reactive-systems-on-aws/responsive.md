---
source_url: https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/responsive.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Responsive
<a name="responsive"></a>

As previously mentioned, being responsive means that systems respond in a timely manner, even under heavy load. To meet this requirement, special attention must be paid to latency. In the example architecture, an Application Load Balancer serves as the single point of contact for clients. The load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. This increases the availability of your application, and you can add one or more listeners to your load balancer. Elastic Load Balancing publishes data points to Amazon CloudWatch for your load balancers and your targets. CloudWatch enables you to retrieve statistics about those data points as an ordered set of time-series data, known as metrics. You can think of a metric as a variable to monitor, and the data points as the values of that variable over time. For example, you can monitor the total number of healthy targets for a load balancer over a specified time period. Application Load Balancer exposes the metric TargetResponseTime which is the time elapsed (in seconds) after the request leaves the load balancer until a response from the target is received. Based on this metric, it is possible to scale out the number of services running in an Amazon ECS cluster by defining Amazon CloudWatch Alarms.

 Another important component for reducing latency is the use of caches. At this point you have to differentiate between an in-memory cache inside the application and external caches such as Redis or Memcache, which are offered as a managed service within the framework of Amazon ElastiCache. In-memory caches can be used directly in the application via corresponding libraries. Depending on the extent to which outdated data can be tolerated, this type of cache should be updated shortly after records are changed, and can be implemented via a pub/sub mechanism. In addition, a least-recently-used (LRU) strategy and the limitation of cache entries in terms of quantity and time are also useful. There are several strategies and picking the right caching strategy has a huge impact on the overall performance of the system.

The following section outlines popular caching strategies:
+ **Cache-aside**

   The cache-aside strategy is one of the most common design patterns for cache access. The cache sits next to the database and first the cache is checked to see if a value is found there. If it is not there, the database is queried and the value is then stored in the cache. This means, data is read lazily on first read. One major advantage of this strategy is that the architecture is resilient to cache failures: if your cache fails, the system can still work, but it will have a major impact on response time and latency. It is a common best practice to invalidate cache entries if data is updated or deleted. In addition, a time to live (TTL) is used to automatically invalidate cache entries.
+ **Read-through**

   This read-through strategy is similar to cache-aside, one major difference is that the cache is responsible for reading from the database. With a read-through cache, this is used as a central storage for data: all read accesses go to the cache. If no entry is found when reading, the missing data is fetched from the database by the cache. A read-through cache loads data lazily if the data if accessed for the first time.
+ **Write-through**

   The write-through strategy ensures that entries that are written into the cache are also put into the central storage behind it (for example, a database). Amazon DynamoDB Accelerator (DAX) is a write-through caching service that is designed to simplify the process of adding a cache to DynamoDB tables. Because DAX operates separately from DynamoDB, it is important that you understand the [consistency models of both DAX and DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.consistency.html) to ensure that your applications behave as you expect. Usually, write-through caches are combined with read-through caches, because an isolated write-through cache will only introduce additional latency.
+ **Write-back (write-behind) **

  The write-back strategy, stores entries directly in the cache by the application and after a delay are stored in a database. This type of caching is particularly suitable for write-intensive applications, because services don’t have to wait for data being persisted to the database. Database updates can be stored in a queue and applied asynchronously. Often this pattern is combined with a read-through cache if the workload is read- and write-heavy.

All of these caching strategies have advantages and disadvantages, which can be mitigated by appropriate logic (invalidation, pre-warming etc.). Therefore, additional logic is necessary, which has to be implemented and tested.
