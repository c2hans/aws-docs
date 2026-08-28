---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/architecture.html
---

# Architecture components of an Amazon Redshift data warehouse
<a name="architecture"></a>

We recommend that you have a basic understanding of the core architecture components in an Amazon Redshift data warehouse. This knowledge can help you better understand how to design your queries and tables for optimal performance.

A data warehouse in Amazon Redshift consists of the following core architecture components:
+ **Clusters** – A cluster, which is composed of one or more compute nodes, is the core infrastructure component of an Amazon Redshift data warehouse. Compute nodes are transparent to external applications, but your client application interacts directly with the leader node only. A typical cluster has two or more compute nodes. The compute nodes are coordinated through the leader node.
+ **Leader node** – A leader node manages the communications for client programs and all compute nodes. A leader node also prepares the plans for running a query whenever a query is submitted to a cluster. After the plans are ready, the leader node compiles code, distributes the compiled code to the compute nodes, and then assigns slices of data to each compute node to process the query results.
+ **Compute node** – A compute node runs a query. The leader node compiles code for individual elements of the plan to run the query and assigns the code to individual compute nodes. The compute nodes run the compiled code and send intermediate results back to the leader node for final aggregation. Each compute node has its own dedicated CPU, memory, and attached disk storage. As your workload grows, you can increase the compute capacity and storage capacity of a cluster by increasing the number of nodes, upgrading the node type, or both.
+ **Node slice** – A compute node is partitioned into units called slices. Every slice in a compute node is allocated a portion of the node's memory and disk space where it processes a portion of the workload assigned to the node. The slices then work in parallel to complete the operation. Data is distributed among slices on the basis of the [distribution style](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-best-dist-key.html) and distribution key of a particular table. An even distribution of data makes it possible for Amazon Redshift to evenly assign workloads to slices and maximizes the benefit of parallel processing. The number of slices per compute node is decided on the basis of the type of node. For more information, see [Clusters and nodes in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-about-clusters-and-nodes) in the Amazon Redshift documentation.
+ **Massively parallel processing (MPP)** – Amazon Redshift uses MPP architecture to quickly process data, even complex queries and vast amounts of data. Multiple compute nodes run the same query code on portions of data to maximize parallel processing.
+ **Client application** – Amazon Redshift integrates with various extract, transform, and load (ETL), business intelligence (BI) reporting, data mining, and analytics tools. All client applications communicate with the cluster through the leader node only.

The following diagram shows how the architecture components of an Amazon Redshift data warehouse work together to accelerate queries.

![The leader node and compute nodes in an Amazon Redshift cluster processing a query from a client.](http://docs.aws.amazon.com/prescriptive-guidance/latest/query-lifecycle-redshift/images/guide-img/84453e49-6013-472a-b5b1-062248897e49/images/a5dbbdbf-6551-4d39-82b7-0a8e0d5a5cde.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
