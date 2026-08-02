---
source_url: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/evictions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Evictions
<a name="evictions"></a>

 Evictions occur when cache memory is overfilled or is greater than the **maxmemory** setting for the cache, causing the engine to select keys to evict to manage its memory. The keys that are chosen are based on the eviction policy you select.

 By default, Amazon ElastiCache (Redis OSS) sets the **volatile-lru** eviction policy for your Redis cluster. When this policy is selected, the least recently used (LRU) keys that have an expiration (TTL) value set are evicted. Other eviction policies are available and can be applied in the configurable **maxmemory-policy** parameter.

 The following table summarizes eviction policies:

|  Eviction Policy  |  Description  |
| --- | --- |
|  allkeys-lru  |  The cache evicts the least recently used (LRU) keys regardless of TTL set.  |
|  allkeys-lfu  |  The cache evicts the least frequently used (LFU) keys regardless of TTL set.  |
|  volatile-lru  |  The cache evicts the least recently used (LRU) keys from those that have a TTL set.  |
|  volatile-lfu  |  The cache evicts the least frequently used (LFU) keys from those that have a TTL set.  |
|  volatile-ttl  |  The cache evicts the keys with the shortest TTL set.  |
|  volatile-random  |  The cache randomly evicts keys with a TTL set.  |
|  allkeys-random  |  The cache randomly evicts keys regardless of TTL set.  |
|  noeviction  |  The cache doesn’t evict keys at all. This blocks future writes until memory frees up.  |

 A good strategy in selecting an appropriate eviction policy is to consider the data stored in your cluster and the outcome of keys being evicted.

 Generally, LRU-based policies are more common for basic caching use cases. However, depending on your objectives, you might want to use a TTL or random-based eviction policy that better suits your requirements.

 Also, if you are experiencing evictions with your cluster, it is usually a sign that you should scale up (that is, use a node with a larger memory footprint) or scale out (that is, add more nodes to your cluster) to accommodate the additional data. An exception to this rule is if you are purposefully relying on the cache engine to manage your keys by means of eviction, also referred to as an [LRU cache](https://redis.io/topics/lru-cache).

In addition to the existing time-based LRU policy, Amazon ElastiCache (Redis OSS) also supports a least frequently used (LFU) eviction policy for evicting keys. The LFU policy, which is based on frequency of access, provides a better cache hit ratio by keeping frequently used data in-memory; it traces access counter for each object and evicts keys according to the counter. Every time the object is touched, it reduces the counter after a period called the decay period. This means data used rarely is evicted while the data used often has a higher chance of remaining in the memory.
