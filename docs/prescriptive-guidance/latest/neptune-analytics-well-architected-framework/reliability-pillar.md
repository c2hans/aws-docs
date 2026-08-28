---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-analytics-well-architected-framework/reliability-pillar.html
---

# Reliability pillar
<a name="reliability-pillar"></a>

The AWS Well-Architected Framework [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/reliability.html) encompasses the ability of a workload to perform its intended function correctly and consistently when it's expected to. This includes the ability to operate and test the workload through its entire lifecycle.

A reliable workload starts with upfront design decisions for both software and infrastructure. Your architecture choices impact your workload behavior across all the Well-Architected pillars. For reliability, there are specific patterns you must follow, as discussed in this section.

The reliability pillar focuses on the following key areas:
+ Workload architecture, including service quotas and deployment patterns
+ Change management
+ Failure management

## Understand Neptune service quotas
<a name="service-quotas"></a>

Your AWS account has default quotas (formerly referred to as *limits*) for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some, but not all, quotas.

To find quotas for Neptune Analytics, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services**, and then select **Amazon Neptune Analytics**. Pay attention to quotas on the number of graphs and snapshots, maximum provisioned memory for a graph, and API request rates.

If the maximum provisioned memory isn't sufficient for your dataset, assess which node and edge types are essential for your intended analytical usage. Load a subset of the data so that analytics are possible within an allowable provisioned capacity. Many analytics workloads, especially those that run graph algorithms, only need the topology with a limited set of properties instead of the full transactional graph. (For a discussion of the differences between transactional and analytical workloads, see the [Performance efficiency pillar](performance-efficiency-pillar.md) section.)

If the maximum number of graphs isn't sufficient for your intended use:
+ Consider combining graphs that have similar uses.
+ Assess how many graphs have to run at a given time. If you have an ephemeral analytics use case, snapshot and delete a graph when it is no longer needed. This reduces the number of graphs against the quota.
+ Consider provisioning graphs in different AWS accounts.

## Understand Neptune deployment patterns
<a name="deployment-patterns"></a>

Understand the following decision points when you plan to deploy a Neptune Analytics graph:
+ **Seeding**: Decide whether to create an empty graph or load data into it at creation time with data from Amazon S3, an existing Neptune database cluster, or an existing Neptune database snapshot.

  Recommendation: If the source is a Neptune cluster or snapshot, you must load its data at graph creation time. If the source is Amazon S3, load the data at creation time if the effort of loading it is significant and best performed as an infrastructure provisioning activity. If you prefer to load data as an data engineering or application activity, create an empty graph and load data from Amazon S3 later.
+ **Capacity**: Estimate the required provisioned capacity for a graph, given the data size and expected application usage.

  Recommendation: At creation time, [specify maximum provisioned memory](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphUsingImportTask.html) to limit the graph size. This setting is mandatory. You can change capacity later if necessary.
+ **Availability and fault tolerance**: Decide whether replicas are required for availability. A replica acts as a warm standby for recovery in case of graph failure. A graph with replicas recovers faster than a graph without replicas. Also consider how long the graph is needed, whether it is for ephemeral analytics only, and, if so, when it will be removed.

  Recommendation: Determine availability requirements—such as how long the graph can be unavailable and when it can be removed—before you create a graph.
+ **Networking and security**: Determine whether you need public connectivity, private connectivity, or both, and whether you want to encrypt your data.

  Recommendation**: **Understand organizational requirements—such as whether public connectivity is allowed and where graph client applications will be deployed—before you create a graph.
+ **Backups and recovery**: Determine whether snapshots should be created, and, if so, when or under which conditions. Consider whether your organization has disaster recovery (DR) requirements.

  Recommendation: Creating snapshots is a manual activity. Decide when to create snapshots and consider your DR requirements before you create a graph.

## Manage and scale Neptune clusters
<a name="clusters"></a>

A Neptune Analytics graph consists of a single, memory-optimized instance. The capacity (m-NCU) of the instance is set at creation time. The instance can be vertically scaled by increasing provisioned capacity through an [administrative action](https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UpdateGraph.html); provisioned capacity can also be decreased. Replicas are passive failover targets, so they do not increase the scale of a graph. In this respect, a graph replica differs from a [Neptune database read replica](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-add-replicas.html), which is an active instance in a Neptune cluster that can process read operations from applications.

Replicas incur cost. The replica is priced at the m-NCU rate of the graph. For example, if a graph is provisioned for 128 m-NCU and has a single replica, the cost is twice that of an equivalent graph that has no replicas.

In analytics, there are two primary reasons to scale up:
+ To provide more memory and CPU for analytical queries and algorithms, because the individual query is expensive, the graph algorithm to run is inherently complex and requires more resources given its input, or the concurrent request rate is high. If such queries are encountering out-of-memory errors, scaling up is a reasonable remedy.
+ To support a larger graph size than you planned for. For example, if the current provisioned capacity is 128 m-NCU to support 60 GB of source data and you need an additional 40 GB of source data, an increase to 256 m-NCU is warranted.

Monitor CloudWatch metrics for Neptune Analytics, such as `NumQueuedRequestsPerSec`, `NumOpenCypherRequestsPerSec`, `GraphStorageUsagePercent`, `GraphSizeBytes`, and `CPUUtilization`, to determine if scaling is necessary. You can update a graph's configuration through the console, AWS CLI, or SDKs. (For examples and best practices, see the [Operational excellence pillar](operational-excellence-pillar.md) section.)

## Manage backups and failover events
<a name="failover"></a>

Use replicas to ensure that a graph remains available in case of failure. A graph uses log-based persistence to commit changes across Availability Zones in an AWS Region. The replica acts as a warm standby and has access to this data. If there is a failure, the graph resumes operations on the replica. The application continues to use the same endpoint to connect to the graph. In-flight requests during the failure generate errors with a *service unavailable* exception. Consider using a [retry with backoff pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) in the application code to catch the error, and try again after a brief interval. New requests made during failover are queued and might experience longer latency.

If no replica is configured and the graph fails, Neptune Analytics recovers from durable storage, but recovery takes longer because Neptune has to re-initialize resources.

Create snapshots of the graph. (Neptune Analytics doesn't take automatic snapshots.) If the graph is modified on a regular basis after creation, take frequent snapshots to capture its current state. Delete older snapshots if restoration to an earlier point in time isn't required.

You can share snapshots with other accounts and across AWS Regions. If you have DR requirements, consider whether restoring the graph in a different Region from a snapshot meets your recovery time objective (RTO) and recovery point objective (RPO) requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
