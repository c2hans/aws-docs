---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/reliability-pillar.html
---

# Reliability pillar
<a name="reliability-pillar"></a>

The [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/reliability.html) encompasses the ability of a workload to perform its intended function correctly and consistently when it's expected to. This includes the ability to operate and test the workload through its total lifecycle.

A reliable workload starts with upfront design decisions for both software and infrastructure. Your architecture choices will impact your workload behavior across all of the AWS Well-Architected pillars. For reliability, there are specific patterns you must follow.

The reliability pillar focuses on the following key areas:
+ Workload architecture, including service quotas and deployment patterns
+ Change management
+ Failure management

## Understand Neptune service quotas
<a name="neptune-quotas"></a>

A [Neptune cluster volume](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage.html) can grow to a maximum size of 128 tebibytes (TiB) in all supported AWS Regions except China and GovCloud, where the quota is 64 TiB.

The 128 TiB quota is sufficient to store approximately 200-400 billion objects in the graph. In a labeled property graph (LPG), an [object](https://docs.aws.amazon.com/neptune/latest/userguide/graph-get-started.html) is a node, an edge, or a property on a node or edge. In a Resource Description Framework (RDF) graph, an object is a [quad](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-data-model.html).

For any [Neptune Serverless cluster](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-capacity-scaling.html), you set both the minimum and the maximum number of Neptune Capacity Units (NCUs). Each NCU consists of 2 gibibytes (GiB) of memory and the associated vCPU and networking. The minimum and maximum NCU values apply to any serverless instances in the cluster. The highest maximum NCU value you can set is 128.0 NCUs, and the lowest minimum is 1.0 NCUs. Optimize the NCU range that works best for your application by observing the Amazon CloudWatch metrics `ServerlessDatabaseCapacity` and `NCUUtilization` to capture the range you commonly run in and correlate undesired behavior or costs within that range. In many workloads, 1.0 NCU is too low of a starting point and results in unreliable behavior after periods of inactivity. If you find that your workload doesn't scale fast enough, increase the minimum NCUs to provide enough processing for the initial surge while it scales.

Each AWS account has quotas for each Region on the number of database resources that you can create. These resources include DB instances and DB clusters. After you reach a limit for a resource, additional calls to create that resource fail with an exception. Some quotas are soft quotas that can be increased by request. For a list of quotas shared between Amazon Neptune and Amazon RDS, Amazon Aurora, and Amazon DocumentDB (with MongoDB compatibility), along with links to request quota increases when available, see [Quotas in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.Limits).

## Understand Neptune deployment patterns
<a name="deployment-patterns"></a>

In Neptune DB clusters, there is one primary DB instance and up to 15 Neptune replicas. The primary DB instance supports read and write operations, and it performs all of the data modifications to the cluster volume. Neptune replicas connect to the same storage volume as the primary DB instance, and they support only read operations. Neptune replicas can offload read workloads from the primary DB instance.

To achieve high availability, use read replicas. Having one or more read replica instances available in different Availability Zones can increase availability because read replicas serve as failover targets for the primary instance. If the writer instance fails, Neptune promotes a read replica instance to become the primary instance. When this happens, there is a brief interruption (generally less than 30 seconds) while the promoted instance is rebooted, during which read and write requests made to the primary instance fail with an exception. For highest reliability, consider two read replicas in different Availability Zones. If the primary instance in Availability Zone 1 goes offline, the instance in Availability Zone 2 is promoted to primary, but it cannot handle queries while that happens. So an instance in Availability Zone 3 is required to handle read queries during the transition.

If you are using Neptune Serverless, reader and writer instances in all Availability Zones will scale up and down, independently of each other, depending on their database load. You can set the promotion tier of a reader instance to 0 or 1 so that it scales up and down along with the capacity of the writer instance. This makes it ready to take over the current workload at any time.

If your application has a worldwide footprint or requires [multi-Region failover](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-gdb-disaster-recovery.html), consider using a [Neptune global database](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-global-database.html). An Amazon Neptune global database spans multiple AWS Regions, enabling low-latency global reads and providing fast recovery in the rare case where an outage affects an entire AWS Region. A Neptune global database consists of a primary DB cluster in one Region and up to five secondary DB clusters in different Regions.

## Manage and scale Neptune clusters
<a name="managing-and-scaling-neptune-clusters"></a>

You can use [Neptune auto-scaling](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-autoscaling.html) to automatically adjust the number of Neptune replicas in a DB cluster to meet your connectivity and workload requirements based on CPU utilization thresholds. With auto-scaling, your Neptune DB cluster can handle sudden increases in workload. When the workload decreases, auto-scaling removes unnecessary replicas so that you aren't paying for unused capacity. Be aware that new instance startup can take as long as 15 minutes, so auto-scaling alone is not a sufficient solution for rapid changes in demand.

You can use auto-scaling only with a Neptune DB cluster that already has one primary writer instance and at least one read-replica instance ([see Amazon Neptune DB Clusters and Instances](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-db-clusters.html)). Also, all read-replica instances in the cluster must be in an available state. If any read-replica is in a state other than available, Neptune auto-scaling does nothing until every read-replica in the cluster is available.

If you experience rapid changes in demand, consider using serverless instances. The serverless instances can scale vertically over short periods while auto-scaling scales horizontally over longer periods. This configuration provides optimal scalability because the serverless instances scale vertically while auto-scaling instantiates new read replicas to handle the workload beyond the maximum capacity of a single serverless instance. For more information about capacity scaling of Amazon Neptune Serverless, see [Capacity scaling in a Neptune Serverless DB cluster](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-capacity-scaling.html).

If your scaling needs change at predictable times, you can [schedule changes](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html) to the minimum instances, maximum instances, and thresholds to better handle those shifting needs. Remember to schedule scale-out events at least 15 minutes in advance to allow for those instances to come online when needed.

You manage your database configuration in Amazon Neptune by using parameters in a [parameter group](https://docs.aws.amazon.com/neptune/latest/userguide/parameter-groups.html). Parameter groups act as a *container* for engine configuration values that are applied to one or more DB instances. When modifying cluster parameters in parameter groups, understand the difference between static and dynamic parameters, and how and when they are applied. Use the [status](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-status.html) endpoint to see the current applied configuration.

## Manage backups and failover events
<a name="backup-failure"></a>

Neptune backs up your cluster volume automatically, and it retains backed up data for the length of the *backup retention period*. Neptune backups are continuous and incremental so you can quickly restore to any point within the backup retention period. You can specify a 1–35 day backup retention period when you create or modify a DB cluster.

To retain a backup beyond the backup retention period, you can also take a snapshot of the data in your cluster volume. Storing snapshots incurs the standard storage charges for Neptune.

When you create an Amazon Neptune snapshot of a DB cluster, Neptune creates a storage volume snapshot of the cluster, backing up all its data, not just individual instances. You can later create a new DB cluster by restoring from this DB cluster snapshot. When you restore the DB cluster, you provide the name of the DB cluster snapshot to restore from, and then you provide a name for the new DB cluster that is created by the restore.

Test how your system responds to failover events. Use the Neptune API to [force a failover event](https://docs.aws.amazon.com/neptune/latest/apiref/API_FailoverDBCluster.html). [Reboot with failover](https://docs.aws.amazon.com/neptune/latest/apiref/API_RebootDBInstance.html) is beneficial when you want to simulate a failure of a DB instance for testing or for restore operations to the original Availability Zone after a failover occurs. For more information, see [Configuring and managing a Multi-AZ deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html). When you reboot a DB writer instance, it fails over to the standby replica. Rebooting a Neptune replica does not initiate a failover.

Design your clients for reliability. Test their behavior during failover events. Implement retry logic in your client with exponential backoff logic. Code examples that implement this logic can be found in the documentation under the [AWS Lambda function examples for Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/lambda-functions-examples.html).

Consider using [AWS Backup](https://aws.amazon.com/blogs/storage/centralizing-data-protection-and-compliance-for-amazon-neptune-with-aws-backup/) if you have a common set of backup requirements you apply across multiple database engines.
