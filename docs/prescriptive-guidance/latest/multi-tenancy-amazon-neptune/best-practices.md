---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/best-practices.html
---

# Operational best practices for ISVs
<a name="best-practices"></a>

Many of the guidelines in this section are best practices for all customers, but they have added significance for ISVs.

## Update your Neptune cluster with the newest versions
<a name="update"></a>

In the Amazon Neptune [release notes](https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html), you can see that every version brings a number of bug fixes, performance improvements, and new features. Keep your Neptune clusters on the latest version as much as possible. If you find a previously undiscovered bug in your workload and your cluster is on the latest version, Neptune engineers can create a private patch for your cluster (if warranted and you want it). The patch can bridge until the next release when that fix will be generally available. To help with updating your clusters to the newest version, use the [Neptune Blue/Green solution](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-deployments.html).

## Use deltas instead of delete and replace for data ingestion
<a name="deltas"></a>

You can use several techniques to ingest, or write, data to Neptune. Many customers try to simplify their data ingestion by deleting and reinserting their graph every time a change is received in the feed. They might add a `last-modified` property to each node and periodically scan for nodes that haven't been modified since some specified date and delete them. While these techniques simplify the data ingestion process, they have long-term health and scalability implications for your Neptune cluster.

First, Neptune uses [dictionary encoding](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-data-model.html#feature-overview-storage-dictionary) of strings. Unless you explicitly specify the IDs of nodes and edges, Neptune generates a GUID represented as a string for the ID and stores that string in the dictionary. If you are constantly deleting and adding objects, the automatically generated IDs will cause bloat in the dictionary.

Second, Neptune scales up to ingest about 120 K objects per second at the maximum. If you continuously delete and add objects, you consume a lot of that bandwidth on objects that essentially are not changing. This limits the number of tenants that you can host on a cluster, requires larger writer instances in the clusters, and requires more I/O operations. All of these factors increase your costs.

We highly recommend that you develop a way to calculate the true delta of what has changed instead of using the delete and add methods. However, some data sources aren't conducive to this (for example, API calls that return the current state, or events that do not track exactly what changed). If your raw data source is not conducive to identifying changes, use your extract, transform, and load (ETL) processes to calculate the delta. For example, you can maintain snapshots from each previous data capture in Parquet format, use AWS Glue to calculate the differences between those snapshots, and push only the differences to Neptune.

## Model how Neptune costs will evolve with your tenants
<a name="costs"></a>

Whether you use a silo, pool, or hybrid model, your cloud costs will scale with your tenants' size. Tenants that require more concurrent connections need larger instances or more read replicas than those with fewer concurrent connections. The same applies to tenants that require more rapid data ingestion. The three components of Neptune cluster cost are instance size (and number), data size (GB-months), and I/O operations (per million). While these costs are generally workload specific, they scale with size and data volume, they can be measured by using AWS tools. Track and understand the economies of scale against key indicators of your tenants' sizes, including how their sizes vary over time. If the unpredictability of your I/O charges impacts your margins, consider choosing [Neptune I/O-Optimized](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html) storage for a more predictable cost.

## Scale your clusters for customer demand
<a name="scale"></a>

There is no tried or true formula for right-sizing your Neptune instance size. The [Neptune documentation](https://docs.aws.amazon.com/neptune/latest/userguide/instance-types.html) provides guidance, but there are too many variables to recommend a direct mapping. These variables include but aren't limited to the following:
+ Data model
+ Data shape
+ Query concurrency
+ Query complexity.

Plan testing to determine the optimal size for your workloads and tenant profiles. In general, we recommend using provisioned instances for cost efficiency and predictability. If your customer-experience goals prioritize optimal scaling over costs, consider using [Neptune Serverless instances](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless.html) to ensure a more consistent experience regardless of workload fluctuations.

If your tenant read workloads have significant variability in their peaks and troughs, combine Neptune Serverless instances with [Neptune auto-scaling](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-autoscaling.html).  It usually takes 10-15 minutes for a new read replica to come online after it's initialized. This means that auto-scaling alone can handle prolonged changes in traffic, but it isn't sufficient for rapidly changing spikes in activity. By combining Neptune Serverless and Neptune auto-scaling, you can both scale instances up or down and scale the number of read replicas in and out.

If your tenants have significantly different workload profiles or service level agreements (SLAs), consider using [custom endpoints](https://docs.aws.amazon.com/neptune/latest/userguide/feature-custom-endpoint-membership.html) and dedicated read replicas to direct traffic to instances that are optimized for that traffic. Optimization can include a different sizing of the instance, specific query patterns, or pre-warming the buffer cache.
