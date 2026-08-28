---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients-lettuce-cmd-readfrom.html
---

# Distributing reads to replicas (cluster mode disabled)
<a name="BestPractices.Clients-lettuce-cmd-readfrom"></a>

For cluster mode disabled clusters with replicas, you can use Lettuce's `StaticMasterReplicaTopologyProvider` with the `ReadFrom` setting to direct writes to the primary node and distribute reads across replicas. This improves read throughput by offloading reads from the primary.

Use the primary endpoint for writes and the reader endpoint for reads. The reader endpoint automatically load-balances connections across available replicas.

```
// Primary endpoint for writes, reader endpoint for read distribution
RedisURI primaryURI = RedisURI.Builder.redis("primary-endpoint.cache.amazonaws.com")
    .withPort(6379).withSsl(true).build();
RedisURI readerURI = RedisURI.Builder.redis("reader-endpoint.cache.amazonaws.com")
    .withPort(6379).withSsl(true).build();

RedisClient redisClient = RedisClient.create(clientResources);
redisClient.setOptions(clientOptions);

// Open a primary-replica connection using the StaticMasterReplicaTopologyProvider
StatefulRedisMasterReplicaConnection<String, String> connection =
    MasterReplica.connect(redisClient, StringCodec.UTF8, Arrays.asList(primaryURI, readerURI));

// Direct reads to replicas, writes always go to the primary
connection.setReadFrom(ReadFrom.REPLICA_PREFERRED);
```

The following `ReadFrom` options are available:
+ `REPLICA_PREFERRED` – Reads from replicas when available and falls back to the primary (recommended for most use cases).
+ `REPLICA` – Reads only from replicas. Fails if no replica is available.
+ `PRIMARY_PREFERRED` – Reads from the primary, falls back to replicas.
+ `ANY_REPLICA` – Reads from any replica node.
+ `PRIMARY` – Reads only from the primary node. Use when strong consistency is required.

**Note**
Data read from replicas might be slightly stale because replication is asynchronous. If your application requires strong consistency, use `ReadFrom.PRIMARY` or `ReadFrom.PRIMARY_PREFERRED`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
