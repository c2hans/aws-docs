---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/performance-efficiency-pillar.html
---

# Performance efficiency pillar
<a name="performance-efficiency-pillar"></a>

The [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html) of the AWS Well-Architected Framework focuses on how to optimize performance while ingesting or querying data. Performance optimization is an incremental and continual process of the following:
+ Confirming business requirements
+ Measuring the workload performance
+ Identifying under-performing components
+ Tuning the components to meet your business needs

The performance efficiency pillar provides use case–specific guidelines that can help in identifying the right graph data model and query languages to use. It also includes best practices to follow when ingesting data into and consuming data from Amazon Neptune.

The performance efficiency pillar focuses on the following key areas:
+ Graph modeling
+ Query optimization
+ Cluster right-sizing
+ Write optimization

## Understand graph modeling
<a name="graph-modeling"></a>

Understand the difference between Labeled Property Graph (LPG) and Resource Description Framework (RDF) models. In most cases, it is a matter of preference. There are several use cases, however, where one model is better suited than the other. If you require knowledge of the path connecting two nodes in your graph, choose LPG. If you want to federate data across Neptune clusters or other graph triple stores, choose RDF.

If you are building a software as a service (SaaS) application or an application that requires multi-tenancy, consider incorporating the logical separation of tenants in your data model instead of having one tenant for each cluster. To achieve that type of design, you can use SPARQL named graphs and labeling strategies, such as prepending customer identifiers to labels or adding property key-value pairs representing tenant identifiers. Make sure your client layer injects these values to keep that logical separation. For more information about multi-tenancy recommendations, see [Multi-tenancy guidance for ISVs running Amazon Neptune databases](https://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/introduction.html).

The performance of your queries depends on the number of graph objects (nodes, edges, properties) that need to be evaluated in the processing of your query. As such, the graph model can have significant impact on the performance of your application. Use granular labels when possible, and store only the properties you need to achieve path determination or filtering. To achieve higher performance, consider precalculating parts of your graph, such as creating summarization nodes or more direct edges connecting common paths.

Try to avoid navigating across nodes that have an abnormally high number of edges with the same label. Such nodes often have thousands of edges (where most nodes have edge counts in the tens). The result is much higher compute and data complexity. These nodes might not be problematic in some query patterns, but we recommend modeling your data differently to avoid it, especially if you will navigate across the node as an intermediate step. You can use [slow-query logs](https://docs.aws.amazon.com/neptune/latest/userguide/slow-query-logs.html) to help identify queries that navigate across these nodes. You will likely observe much higher latency and data access metrics than your average query patterns, especially if you use [debug mode](https://docs.aws.amazon.com/neptune/latest/userguide/slow-query-logs.html#slow-query-log-debug-attributes).

Use deterministic node IDs for nodes and edges if your use case supports it instead of using Neptune to assign random GUID values for IDs. Accessing nodes by ID is the most efficient method.

## Optimize queries
<a name="optimize-queries"></a>

The openCypher and Gremlin languages can be used interchangeably on LPG models. If performance is a top concern, consider using the two languages interchangeably because one might perform better than the other for specific query patterns.

Neptune is in the process of converting to its alternative query engine [(DFE)](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-engine.html). openCypher runs on the DFE only, but both Gremlin and SPARQL queries can be optionally set to run on the DFE by using query annotations. Consider testing your queries with the DFE activated and comparing performance of your query pattern when not using the DFE.

Neptune is optimized for transactional type queries that start at a single node or set of nodes and fan out from there, rather than analytical queries that evaluate the entire graph. For your analytical query workloads, use [Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html). Neptune Analytics is an ideal choice for investigatory, exploratory, or data-science workloads that require fast iteration for data, analytical and algorithmic processing. It can also perform a vector search on graph data and can load data directly from your Neptune database instance. If Neptune Analytics does not meet your needs, you can also consider [AWS SDK for Pandas](https://github.com/aws/aws-sdk-pandas) or using [neptune-export](https://github.com/aws/neptune-export) combined with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) or [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html).

To identify inefficiencies and bottlenecks in your models and queries, use the `profile` and `explain` APIs for each query language to obtain detailed explanations of the query plan and query metrics. For more information, see [Gremlin profile](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html), [openCypher explain](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain.html), and [SPARQL explain](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain.html).

Understand your query patterns. If the number of distinct edges in a graph becomes large, the default Neptune access strategy can become inefficient. The following queries might become quite inefficient:
+ Queries that navigate backward across edges when no edge labels are given.
+ Clauses that use this same pattern internally, such as `.both()` in Gremlin, or clauses that drop nodes in any language (which requires dropping incoming edges without knowledge of labels).
+ Queries that access property values without specifying property labels. These queries might become quite inefficient. If this matches your usage pattern, consider enabling the [OSGP index](https://docs.aws.amazon.com/neptune/latest/userguide/features-lab-mode.html#features-lab-mode-features-osgp-index) (object, subject, graph, predicate).

Use [slow-query logging](https://docs.aws.amazon.com/neptune/latest/userguide/slow-query-logs.html) to identify slow queries. Slow queries can be caused by unoptimized query plans or unnecessarily large numbers of index lookups, which can increase I/O costs. The Neptune explain and profile endpoints for [Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html), [SPARQL](https://docs.aws.amazon.com/neptune/latest/userguide/sparql-explain.html), or [openCypher ](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain.html)can help you understand why these queries are slow. Causes might include the following:
+ Nodes with an abnormally high number of edges compared with the average node in the graph (for example, thousands compared with tens) can add computational complexity and therefore longer latency and greater resource consumption. Determine whether these nodes are correctly modeled, or whether the access patterns can be improved to reduce the number of edges that must be traversed.
+ Unoptimized queries will contain a warning that specific steps are not optimized. Rewriting these queries to use optimized steps might improve performance.
+ Redundant filters might cause unnecessary index lookups. Likewise, redundant patterns might cause duplicate index lookups that can be optimized by improving the query (see `Index Operations - Duplication ratio` in the profile output).
+ Some languages such as Gremlin don't have strongly typed numerical values, and they use type promotion instead. For example, if the value is 55, Neptune looks for values that are integers, longs, floats, and other numerical types equivalent to 55. This results in additional operations. If you know your types match in advance, you can avoid this by using a [query hint](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-query-hints-typePromotion.html).
+ Your graph model can greatly impact performance. Consider reducing the number of objects that need to be evaluated by using more granular labels or by precalculating shortcuts to multiple-hop linear paths.

If query optimization alone does not allow you to reach your performance requirements, consider using a variety of [caching techniques](https://aws.amazon.com/blogs/database/part-1-accelerate-graph-query-performance-with-caching-in-amazon-neptune/) with Neptune to achieve those requirements.

Neptune performance is continuously improving with each version. Review the [release notes](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html) to see details of the improvements with each release. Consider planning regular updates to your Neptune DB cluster to help achieve optimal performance. Newer versions also support newer instances. Consider upgrading to 1.4.5.0 or later to be able to utilize the `r8g` instances. For more information about how this can improve your workload's performance, see [4.7 times better write query price-performance with AWS Graviton4 R8g instances using Amazon Neptune v1.4.5](https://aws.amazon.com/blogs/database/4-7-times-better-write-query-price-performance-with-aws-graviton4-r8g-instances-using-amazon-neptune-v1-4-5/).

## Right-size clusters
<a name="right-size-clusters"></a>

Size your cluster for your concurrency and throughput requirements. The number of concurrent queries that can be handled by each instance in the cluster is equal to two times the number of virtual CPUs (vCPUs) on that instance. Additional queries that arrive while all worker threads are occupied are put into a [server-side queue](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-queuing.html). Those queries are handled on a first-in-first-out (FIFO) basis when worker threads become available. The `MainRequestQueuePendingRequests` Amazon CloudWatch metric shows the current queue depth for each instance. If this value is frequently above zero, consider [choosing an instance](https://docs.aws.amazon.com/neptune/latest/userguide/instance-types.html) with more vCPUs. If the queue depth exceeds 8,192, Neptune will return a `ThrottlingException` error.

Approximately 65 percent of the RAM for each instance is reserved for buffer cache. The buffer cache holds the working data set of data (not the entire graph; just the data that is being queried). To determine what percentage of data is being fetched from the buffer cache instead of storage, monitor the CloudWatch metric `BufferCacheHitRatio`. If this metric often drops below 99.9 percent, consider trying an instance with more memory to determine if it decreases your latency and I/O costs.

Read replicas do not have to be the same size same as your writer instance. However, heavy write workloads can cause smaller replicas to fall behind and reboot because they cannot keep up with the replication. Therefore, we recommend making replicas equal to or larger than the writer instance.

When using auto-scaling for your read replicas, remember that it might take up to 15 minutes to bring a new read replica online. When the client traffic increases quickly but predictably, consider using [scheduled scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html) to set the minimum number of read replicas higher to account for that initialization time.

Serverless instances support several different use cases and workloads. Consider serverless over provisioned instances for the following scenarios:
+ Your workload fluctuates often throughout the day.
+ You created a new application and you are unsure what the workload size will be.
+ You're performing development and testing.

It's important to note that serverless instances are more expensive than equivalent provisioned instances on a dollar per GB of RAM basis. Each serverless instance consists of 2 GB of RAM along with associated vCPU and networking. Perform a cost analysis between your options to avoid surprise bills. In general, you will achieve cost savings with serverless only when your workload is very heavy for only a few hours each day and almost zero the rest of the day or if your workload fluctuates significantly throughout the day.

Utilize the [Amazon Neptune Pricing Calculator](https://pricingcalc.neptunedemos.com/) to help assess the correct configuration for your cluster based upon factors like queries-per-second (QPS) requirements.

## Optimize writes
<a name="optimize-writes"></a>

To optimize writes, consider the following:
+ The [Neptune Bulk Loader](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html) is the optimal way to initially load your database or append to existing data. The Neptune loader is not transactional and cannot delete data, so do not use it if these are your requirements.
+ Transactional updates can be made by using the supported query languages. To optimize write I/O operations, write data in batches of 50-100 objects per commit. An object is a node, an edge, or a property on a node or edge in LPG, or a triple store or a quad in RDF..
+ All transactional Neptune write operations are single threaded for each connection. When sending a large amount of data to Neptune, consider having multiple parallel connections that are each writing data. When you choose a Neptune provisioned instance, the instance size is associated with a number of vCPUs. Neptune creates two database threads for each vCPU on the instance, so start at twice the number of vCPUs when testing for optimal parallelization.  Serverless instances scale the number of vCPUs at a rate of approximately one for each 4 NCUs.
**Note**
This does not apply to the bulk loading API, only direct connections.
+ Plan for and efficiently handle [ConcurrentModificationExceptions](https://docs.aws.amazon.com/neptune/latest/userguide/transactions-exceptions.html) during all write processes, even if only a single connection is writing data at any time. Design your clients for reliability when `ConcurrentModificationExceptions` occur.
+ If you want to delete all of your data, consider using the [fast reset API](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-fast-reset.html) instead of issuing concurrent delete queries. The latter will take much longer and incur substantial I/O cost compared with the former.
+ If you want to delete most of your data, consider exporting the data you that you want to keep by using [neptune-export](https://github.com/aws/neptune-export) to load the data into a new cluster. Then delete the original cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
