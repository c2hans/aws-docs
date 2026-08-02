---
source_url: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/amazon-elasticache-for-redis-global-datastore.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon ElastiCache (Redis OSS) Global Datastore
<a name="amazon-elasticache-for-redis-global-datastore"></a>

 Amazon ElastiCache (Redis OSS) Global Datastore is a feature that has been introduced to handle two primary use cases: the ability to have global low latency reads and to support Disaster Recovery scenarios. For more information, see [Replication across AWS Regions using global datastores](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Redis-Global-Datastore.html).

 With the Amazon ElastiCache (Redis OSS) you can now architect a global application with extremely low latency local reads by reading from a geo-local Global Datastore, and also maintain cluster resiliency at the same time. In the unlikely event of the primary region degrading, it can failover to a secondary region.

 Each Global Datastore is a collection of one and more clusters that replicates to one another: A Primary (Active) Cluster (that accepts writes which are replicated to all clusters) and a Secondary (Passive) Cluster (that only accepts read requests and replicates data updates from a Primary cluster). Applications with media contents can now write to an active cluster and the same content can be read in the local regions.

 Amazon ElastiCache (Redis OSS) Global Datastore lets you create a reliable, secure and fully-managed cross-region replication that enables you to easily promote your secondary cluster to primary. During cross-region replication, Global Datastore can be set up on new cluster as well as existing cluster, provided the cluster is running the latest Redis engine version (5.0.6 or later). Scalability is built in to Global Datastore, with regional clusters that can be scaled both vertically and horizontally by modifying Global Datastore without any interruption.

 Amazon ElastiCache (Redis OSS) Global Datastore enables encryption in transit for cross-region communication in addition to encryption at rest.
