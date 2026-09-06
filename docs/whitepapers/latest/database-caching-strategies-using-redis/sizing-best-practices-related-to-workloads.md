---
source_url: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/sizing-best-practices-related-to-workloads.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Sizing Best Practices Related to Workloads
<a name="sizing-best-practices-related-to-workloads"></a>

 With Redis version 5.0.5, you can scale up or scale down your Amazon ElastiCache (Redis OSS) cluster online without any downtime. This enables your cluster to stay online and respond to incoming requests while scaling.

 To increase read and write capacity, you can scale up your cluster by selecting a larger node type, and alternatively read and write capacity can be reduced by selecting a smaller node. Amazon ElastiCache (Redis OSS) can resize your cluster dynamically without any downtime.

 You can also scale out read capacity by adding read replicas and write capacity by adding a specified number of new shards to a cluster.

 To ensure uninterrupted scaling, you need to follow these best practices:

1.  To scale up, you need to ensure sufficient number of ENI (Elastic Network Interface) availability.

1.  To scale down, you need to ensure smaller nodes have adequate memory to absorb the incoming traffic.

1.  Perform scaling activities when traffic towards your cluster is at a minimum. Although the scaling process is designed to remain online, this will help to synchronize data to newer nodes.

1.  Always test your application in a development environment, where possible.
