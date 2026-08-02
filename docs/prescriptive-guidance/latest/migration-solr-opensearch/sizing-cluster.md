---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/sizing-cluster.html
---

# Sizing your OpenSearch cluster
<a name="sizing-cluster"></a>

When you move from Solr to OpenSearch, using the proper sizing is vital for optimal performance and cost management. Start by analyzing your current Solr setup: CPU usage, memory, and performance metrics will serve as your baseline.

You might currently be running an older version of Solr. If so, when you migrate to OpenSearch, you'll typically experience better performance with similar resource allocation, because OpenSearch runs on a newer version of Lucene than your existing Solr deployment. This results in improved search capabilities and optimizations that the updated Lucene engine provides.

Search workloads are usually read-heavy, so we recommend that you prioritize response times by carefully planning replicas, shard sizes, and resource allocation. Use this migration as an opportunity to fix any existing performance issues.

You can start by matching your current Solr resources in OpenSearch. Use the same primary shard size, shard count, CPU, and physical memory for your OpenSearch sizing. Or, you can recalculate the size by using the standard OpenSearch sizing approach, because OpenSearch's optimizations might deliver better performance with the same resources. The goal is to create an improved, efficient search infrastructure instead of replicating your existing setup. For more information, see [Sizing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html) in the AWS documentation.

For example, consider an ecommerce search platform that implements a product catalog search. Let's say that the search handles 50 million documents and 1000 queries per second (QPS) at peak traffic. The following sections show how the search platform is sized in Solr and OpenSearch.

## Solr cluster topology
<a name="sizing-cluster-solr"></a>

The following tables specify Solr cluster sizing for the ecommerce search platform example.

|
|
| Solr component | Value |
| --- |--- |
| Total nodes | 15 |
| Data nodes | 12 |
| ZooKeeper nodes | 3 |
| Primary shards | 12 |
| Replication factor | 2 |
| Total shards | 24 (12 primary shards and 12  replica shards) |

|
|
| Solr node specification | Value |
| --- |--- |
| CPU | 4 cores (Intel Xeon 2.4 GHz) |
| Total RAM | 32 GiB |
| JVM heap | 16 GiB |
| Operating system or file system cache | 16 GiB |
| Disk | 100 GiB SSD |

|
|
| Solr data characteristic |  Value |
| --- |--- |
| Index size (primary) | 540 GiB |
| Index size (total with replica) | 1.1 TiB |
| Shard size | 45 GiB |
| Document count | 50 million |
| Document per shard | Approximately 4.2 million |

|
|
| Solr resource distribution | Per node | Cluster total |
| --- |--- |--- |
| CPU cores | 4 | 48 (data nodes) |
| RAM | 32 GiB | 192 GiB (data nodes only) |
| Storage | 100 GiB | 1.2 TiB (data nodes only) |

To provision identical resources in OpenSearch, keep the following ratios in mind:
+ Number of CPUs for every shard
+ Amount of JVM for every shard

## Equivalent OpenSearch sizing recommendations
<a name="sizing-opensearch"></a>

The following tables provide OpenSearch sizing recommendations for the Solr clusters in the previous section.

|
|
| OpenSearch component | Value |
| --- |--- |
| Instance type | `r7g.2xlarge` |
| Data nodes | 6 |
| Master nodes | 3 |
| Primary shards | 12 |
| Total shards | 24 |

|
|
| OpenSearch node specification | Value |
| --- |--- |
| CPU | 8 vCPU cores |
| Total RAM | 64 GiB |
| JVM heap | 32 GiB |
| OS or buffer cache | 32 GiB |
| Disk | 200 GiB SSD |

|
|
| OpenSearch resource distribution | Per node | Data nodes combined |
| --- |--- |--- |
| CPU cores | 8 | 48 (data nodes) |
| RAM | 64 GiB | 384 GiB (data nodes only) |
| Storage | 200 GiB | 1.2 TiB (data nodes only) |
