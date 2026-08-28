---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-analytics-well-architected-framework/cost-optimization-pillar.html
---

# Cost optimization pillar
<a name="cost-optimization-pillar"></a>

The [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-optimization.html) of the AWS Well-Architected Framework focuses on avoiding unnecessary costs. The following recommendations can help you meet the cost optimization design principles and architectural best practices for Neptune Analytics.

The cost optimization pillar focuses on the following key areas:
+ Understanding spending over time and controlling fund allocation
+ Selecting resources of the right type and quantity
+ Scaling to meet business needs without overspending

## Understand usage patterns and services needed
<a name="usage-patterns"></a>

Before you adopt Neptune Analytics, assess whether your use case is a good fit for graph analytics.
+ **Graph databases**: A graph database such as Neptune is a good fit for your workload if your data model has a discernible graph structure and your queries need to explore relationships and traverse multiple hops. A graph database isn't a good fit for the following patterns:
  + Mainly single-hop queries. In this use case, consider whether your data might be better represented as attributes of an object.
  + JSON or binary large object (blob) data stored as properties.
+ **Graph analytics**: Neptune Analytics is a graph analytics database engine that can quickly analyze large amounts of graph data in memory to get insights and find trends. You can store and query graph data in both a Neptune database and a Neptune Analytics graph. A Neptune database is best suited for scalable online transactional processing (OLTP) needs. Neptune Analytics is best for ephemeral analytics workloads. You can use the two in combination by loading data from your transaction-oriented Neptune database to a Neptune Analytics graph to run analytics of that data. When analysis is complete, you can remove the Neptune Analytics graph. For a more detailed comparison, see [When to use Neptune Analytics and when to use Neptune Database](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/neptune-analytics-vs-neptune-database.html) in the Neptune Analytics documentation.

Determine, with attention to cost, how best to populate your Neptune Analytics graph.
+ [Bulk-import](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import.html) graph data that's staged in an S3 bucket. We recommend this option if your data was previously staged for bulk load to a Neptune database, or if you already have, or can readily produce, the data to be analyzed in [CSV or other supported formats](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/loading-data-formats.html) that bulk import requires. You can run the bulk import as part of the graph creation procedure. [You can place bounds on minimum and maximum capacity](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphUsingImportTask.html). You can also [run the import on a previously created empty graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/loading-data-existing-graph.html) and [monitor the import task](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListImportTasks.html) while it runs.
+ You can create an empty graph and then populate it through an openCypher query by using [batch load](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/batch-load.html). This option is ideal if the data to be loaded is staged in Amazon S3 and is smaller than 50 GB.
+ You can [populate the graph from data in your Neptune database cluster](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-create-from-neptune.html) (supported in Neptune Database version 1.3.0 or later). The intent of this pattern is to run analytics on data that's *currently* in your graph database. Even if the database was initially populated through bulk load, it might have changed significantly since then. To import from the database, Neptune Analytics clones your database and exports data from the clone to an S3 bucket. This procedure incurs costs: notably Neptune database costs for running the clone and Amazon S3 costs for storing and consuming the exported data. The clone is removed when the export is complete. You can delete the exported data in Amazon S3.
+ You can [populate the graph from the snapshot of a Neptune database cluster](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/bulk-import-create-from-neptune.html). This is similar to the previous option, except that the source is a database snapshot. To import from a snapshot, Neptune Analytics first restores the snapshot to a new database cluster, and then exports the data to an S3 bucket. This procedure incurs costs: notably Neptune database costs for running the restored cluster and Amazon S3 costs for storing and consuming the exported data.
+ You can also perform openCypher queries to create, update, or delete data by using atomicity, consistency, isolation, durability (ACID) compliant transactions on the graph. We recommend this approach as a way to make small updates but not as a way of seeding the graph.

If the data needed for analytics is already staged in Amazon S3, we recommend bulk import or batch load. These are more cost-effective than populating the graph from a Neptune database cluster or snapshot.

## Select resources with attention to cost
<a name="consider-cost"></a>

[Neptune Analytics pricing](https://aws.amazon.com/neptune/pricing/#Amazon_Neptune_Analytics) uses a unit known as memory-optimized Neptune Capacity Unit (m-NCU). There is a fixed hourly cost for running a graph with a given m-NCU. A graph might have replicas for failover, and these replicas also incur hourly m-NCU cost.

We recommend the following best practices to estimate capacity, to limit costs, and to monitor costs against performance:
+ If possible, create the graph by importing data from an existing source: data staged in Amazon S3 or an existing Neptune cluster or snapshot. This saves you effort because Neptune Analytics performs the heavy lifting of seeding the graph, and [you can specify a bound maximum capacity](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphUsingImportTask.html).
+ You can [change provisioned capacity](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UpdateGraph.html) on an existing graph.
+ When the graph is no longer needed, you can [create a snapshot and delete the graph](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/managing-deleting.html). If you need to use it again, you can restore the graph from the snapshot.
+ You can choose the number of replicas when you create the graph. Set the value according to your analytics availability requirement. Save costs by minimizing this setting. The maximum value of 2 allows two replica instances in separate Availability Zones. The minimum value of 0 means that Neptune Analytics will not run a replica. However, recovery is faster when a replica is available. For an explanation of graph failure and recovery, see the [Reliability pillar](reliability-pillar.md) section.
+ Monitor Neptune Analytics expenses for current and past billing periods by using [AWS Billing and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html).
+ Monitor Neptune Analytics metrics for CloudWatch, especially `NumQueuedRequestsPerSec`, `NumOpenCypherRequestsPerSec`, `GraphStorageUsagePercent`, `GraphSizeBytes`, and `CPUUtlization`, to assess whether the provisioned capacity is appropriately sized for the graph. Determine if a smaller capacity can accommodate the observed request rate, CPU usage, and graph size.
+ If you require a private endpoint for your graph, pay attention to costs for elastic IPs, virtual private cloud (VPC) endpoints, NAT gateways, or other VPC-related costs. For more, see [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/) and [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).
+ You might want to run one or more Neptune notebook instances to provide a client interface to help developers and analysts query and visualize the graph (see [Neptune workbench pricing](https://aws.amazon.com/neptune/pricing/#Neptune_workbench)). To minimize costs, share the instance among users and create separate notebook folders for each user. Shut down the instance when it isn't in use. For an approach to automate the shutdown, see the AWS blog post [Automate the stopping and starting of Amazon Neptune environment resources using resource tags](https://aws.amazon.com/blogs/database/automate-the-stopping-and-starting-of-amazon-neptune-environment-resources-using-resource-tags/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
