---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-analytics-well-architected-framework/sustainability-pillar.html
---

# Sustainability pillar
<a name="sustainability-pillar"></a>

The [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/sustainability.html) of the AWS Well-Architected Framework focuses on minimizing the environmental impacts of running cloud workloads. Key topics include a shared responsibility model for sustainability, understanding impact, and maximizing use to minimize required resources and reduce downstream impacts.

The sustainability pillar contains the following key focus areas:
+ Your impact
+ Sustainability goals
+ Maximized usage
+ Anticipating and adopting new, more efficient software offerings
+ Use of managed services
+ Downstream impact reduction

This guide focuses on understanding your impact. For more information about the other sustainability design principles, see the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus-design-principles.html).

Your choices and requirements have an impact on the environment. If you can choose AWS Regions that have lower carbon intensity, and if your requirements reflect actual workload needs instead of only maximizing uptime and durability, the sustainability of the workload increases. The next sections discuss best practices and considerations that will have a positive environmental impact if adopted in your workload design and ongoing operations

## Consider your AWS Region selection
<a name="region-selection"></a>

Some AWS Regions are near Amazon renewable energy projects or located where the grid has a published carbon intensity that is lower than others. Consider the [sustainability impact](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/) for Regions that might be viable for your workload, and cross-reference your list with the[ Regions where Neptune Analytics is available.](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/analytics-limits.html#limits-regions)

## Optimize consumption
<a name="consumption"></a>

Minimize the consumption of Neptune Analytics by practicing the following:
+ Analytics is often ephemeral. The graph is required only for the time to run algorithms and record the results. If this is the case, [snapshot and delete](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-deleting.html) the graph when it is no longer needed. You can [restore it from a snapshot](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots.html#graph-snapshots-restoring) later if necessary.
+ If the workload is ephemeral and you have the flexibility to decide when to run the analytics, consider day-to-day trends in power consumption. Demand for electricity is higher during certain times. If you're in the United States, see the [metrics on daily electricity consumption](https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48) on the U.S. Energy Information Administration (EIA) website. Run workloads during off-peak periods for your Region if possible.
+ If the workload is not ephemeral but needs to be available only for limited periods, delete the graph and restore it from a snapshot when it is needed. If its availability follows a schedule, automate the restoration process through scripts so that the graph is ready at the scheduled time.
+ If the data is read-only or has not changed since the last snapshot, do not snapshot it again before deletion.
+ Stop Neptune notebooks when they are not in use.
+ Monitor CloudWatch metrics such as `NumQueuedRequestsPerSec`, `NumOpenCypherRequestsPerSec`, `GraphStorageUsagePercent`, `GraphSizeBytes`, and `CPUUtilization` to assess whether the graph is oversized. Determine if a smaller instance capacity can accommodate the observed request rate, CPU usage, and graph size.

## Optimize software development and architecture patterns
<a name="patterns"></a>

To prevent waste, optimize your models and queries, and share compute resources so that you use all the resources available in Neptune instances and clusters. Specific best practices include:
+ Optimize queries and graph algorithm invocations. Use parameterized queries and [use the query plan cache](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-plan-cache.html), which is enabled by default. For slow queries, run an [explain plan](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-explain.html) to make improvements. If you use [vector similarity search](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vector-similarity.html), decide if smaller embeddings yield accurate similarity results, because smaller embeddings can be created, stored, and searched more efficiently. Before you call a [graph algorithm](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/algorithms.html), use a `MATCH` clause to minimize the input node set. Filter on node and edge labels if possible.
+ Seek the most efficient way to load data into the graph. If you load from data in Amazon S3, use [bulk import](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import.html) if the data is greater than 50 GB in size. Use [batch load](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/batch-load.html) for smaller data.
+ Ask developers to share Neptune notebook instances instead of each creating their own instance. Create separate notebook folders for each developer on a single Jupyter instance. Shut down the instance when it is not in use.
