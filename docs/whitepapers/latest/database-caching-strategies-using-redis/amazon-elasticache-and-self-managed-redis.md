---
source_url: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/amazon-elasticache-and-self-managed-redis.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon ElastiCache and Self-Managed Redis
<a name="amazon-elasticache-and-self-managed-redis"></a>

 Redis is an open source, in-memory data store that has become the most popular key/value engine in the market. Much of its popularity is due to its support for a variety of data structures as well as other features, including [*Lua*](https://www.lua.org/) scripting support and Pub/Sub messaging capability. Other added benefits include high availability topologies with support for read replicas and the ability to persist data.

 Amazon ElastiCache offers a fully-managed service for Redis. This means that all the administrative tasks associated with managing your Redis cluster (including monitoring, patching, backups, and automatic failover), are managed by Amazon. This lets you focus on your business and your data instead of your operations.

 Other benefits of using Amazon ElastiCache (Redis OSS) over self-managing your cache environment include the following:
+  An enhanced Redis engine that is fully compatible with the open source version but that also provides added stability and robustness.
+  Easily modifiable parameters, such as eviction policies, buffer limits, etc.
+  Ability to scale and resize your cluster to terabytes of data.
+  Hardened security that lets you isolate your cluster within [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC).

 For more information about Redis or Amazon ElastiCache, see the [Further reading](further-reading.md) section at the end of this whitepaper.

## Redis Engine Support
<a name="redis-engine-support"></a>

 You can use [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis/) to build HIPAA-compliant applications. To help do this, you can enable at-rest encryption, in-transit encryption, and Redis AUTH when you create a Redis cluster using ElastiCache (Redis OSS) versions 3.2.6 or later.

 Amazon ElastiCache (Redis OSS) version 6.x also support a feature called Role-Based Access Control (RBAC), which can be used instead of authenticating users with the Redis AUTH command. With RBAC, users can be created with specific permissions by using an access string. Users can also be assigned to user groups aligned with a role that is specific to your use cases. More information on RBAC can be found at: [Authenticating Users with Role-Based Access Control](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.RBAC.html) documentation.

 In versions 5.0.3 and later, Amazon ElastiCache (Redis OSS) adds dynamic network processing to enhance I/O handling. By utilizing the extra CPU power available in nodes with four or more vCPUs, Amazon ElastiCache transparently delivers an increase of up to 83% in throughput and up to 47% reduction in latency per node. That is in addition to the significant performance improvements delivered with the introduction of R5 and M5 instances on the service. You can now benefit from the enhanced I/O handling to further boost application performance and reduce costs. Refer to the [Amazon Elasticache Pricing page](https://aws.amazon.com/elasticache/pricing/).

 Amazon ElastiCache (Redis OSS) improves throughput and reduces latency by leveraging more cores for processing I/O and dynamically adjusting to the workload. These improvements work best for applications that require a large number of concurrent connections to the Redis server. No client-side changes are needed.

 At the time of publication, Amazon ElastiCache (Redis OSS) supports Redis version 6.0.5 and earlier.

 Because the newer Redis versions provide a better and more stable experience, Redis versions 2.6.13, 2.8.6, and 2.8.19 are deprecated when using the Amazon ElastiCache console. We recommend against using these Redis versions. If you need to use one of them, work with the AWS CLI or Amazon ElastiCache API. The latest version information can be found on the [Supported ElastiCache (Redis OSS) Versions](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/supported-engine-versions.html) page.

## Available Instance Types
<a name="available-instance-types"></a>

 Amazon ElastiCache supports multiple instance node types. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

 Furthermore, you can launch both ElastiCache (Redis OSS) and Memcached on Graviton2 M6g and R6g instance families. The latest Graviton2 instance types offer you ultra-low latency and high throughput, and you can now enjoy a price/performance improvement of up to 45% over previous generation instances. Graviton2 instances are now the default choice for ElastiCache customers.

 You can launch general-purpose burstable T\*-Standard cache nodes in Amazon ElastiCache. These nodes provide a baseline level of CPU performance with the ability to burst CPU usage at any time until the accrued credits are exhausted. A *CPU credit* provides the performance of a full CPU core for one minute.

## AWS Nitro System
<a name="aws-nitro-system"></a>

 The [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) is the underlying platform for the next generation of EC2 instances that enables AWS to innovate faster, further reduce cost for customers, and deliver added benefits like increased security and new instance types.

 AWS has completely re-imagined its virtualization infrastructure. Traditionally, hypervisors protect the physical hardware and bios, virtualize the CPU, storage, and networking, and provide a rich set of management capabilities. With the Nitro System, we are able to break apart those functions and offload them to dedicated hardware and software.

 The Nitro System delivers practically all of the compute and memory resources of the host hardware to your instances, resulting in better overall performance.

Additionally, dedicated Nitro Cards enable high speed networking, high speed EBS, and I/O acceleration. To benefit from the AWS Nitro System in Amazon ElastiCache (Redis OSS), choose a cache type from the list of supported instances: either M5 (`cache.m5.xlarge` or higher) or R5 (`cache.r5.xlarge` or higher), or later.

 Latest information on supported instances (including listings of previous generation instances), along with details around Burstable types can be found on the following page: [*Supported Node Types*](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheNodes.SupportedTypes.html).
