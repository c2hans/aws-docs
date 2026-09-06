---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/caching-strategy.html
---

# Caching strategy
<a name="caching-strategy"></a>

The ECS architecture implements a multi-layer caching strategy to optimize performance and reduce latency. In addition to the CloudFront edge cache for processed images, the architecture maintains an in-memory configuration cache in each ECS task and a DynamoDB-backed Amazon Rekognition result cache (v8.1\+) that deduplicates detection API calls.

 **In-memory cache**
+ Each ECS task maintains local caches for transformation policies and origin mappings
+ Cache is populated during task startup from DynamoDB
+ Fast lookup times for frequently accessed configurations

 **Cache initialization**

1. New ECS tasks query DynamoDB during startup

1. All transformation policies are loaded into memory

1. Origin mappings are stored in optimized data structures

 **Cache invalidation**
+ Rolling deployment strategy updates all ECS tasks with new configurations
+ Eventual consistency model balances performance with data freshness
+ Cache refresh typically takes up to 5 minutes

 **Cache consistency**
+ New ECS tasks always load the latest configuration data
+ Existing tasks maintain cached data until manual refresh or natural replacement
+ Auto-scaling events automatically provision tasks with current data
+ Stale cache scenarios are resolved through the rolling update process
