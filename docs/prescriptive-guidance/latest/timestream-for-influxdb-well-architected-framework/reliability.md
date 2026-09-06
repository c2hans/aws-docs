---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/timestream-for-influxdb-well-architected-framework/reliability.html
---

# Reliability pillar
<a name="reliability"></a>

The [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/reliability.html) encompasses the ability of a workload to perform its intended function correctly and consistently when it's expected to. This includes the ability to operate and test the workload through its complete lifecycle.

Configuring a reliable workload starts with upfront design decisions for both software and infrastructure. Your architecture choices will impact your workload behavior across all of the Well-Architected pillars. To achieve reliability, you must follow specific patterns.

The reliability pillar focuses on the following key areas:
+ Workload architecture, including service quotas and deployment patterns
+ Managing and scaling InfluxDB instances

## Workload architecture, including service quotas and deployment patterns
<a name="workload-architecture"></a>

Each AWS account has quotas for resources offered in each AWS Region. For example, each Region has a [quota for Timestream for InfluxDB instances](https://docs.aws.amazon.com/general/latest/gr/timestream.html#timestream-quotas), regardless of instance size. After you reach the maximum number of instances in a Region, additional calls to create instances fail with an exception. A Timestream for InfluxDB instance storage volume can grow to a maximum size of 16 tebibytes (TiBs) in all supported AWS Regions.

### Deployment patterns
<a name="deployment-patterns.a9dce884-3cfe-54aa-860c-22b836addf9f"></a>

For [high availability](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influx-managing-multi-az-instance-deployments.html) and failover support for Timestream for InfluxDB instances, you can use Multi-AZ deployments with a single standby DB instance. This type of deployment is called a Multi-AZ DB instance deployment. Amazon Timestream for InfluxDB uses the Amazon failover technology. In a Multi-AZ DB instance deployment, Amazon Timestream automatically provisions and maintains a synchronous standby replica in a different Availability Zone. To provide data redundancy, the primary DB instance is synchronously replicated across Availability Zones to the standby replica.

Running a DB instance with high availability can provide availability during DB instance failure or Availability Zone disruption. If an unplanned outage of your DB instance results from an infrastructure defect, Amazon Timestream for InfluxDB automatically switches to the standby replica. The time that it takes for the failover to complete depends on the database activity and other conditions at the time that the primary DB instance became unavailable.

Failover times are typically 60–120 seconds. However, large transactions with high-cardinality data or a lengthy recovery process with pre-warmup requirements can increase failover time. After the failover is complete, additional time might be required before the Timestream console reflects the new Availability Zone.

If your application must remain available during a complete AWS Region outage, consider setting up replication or writing to a different Region as part of your disaster recovery (DR) plans. However, before you set up replication, be sure that you understand the limitations. For more information, see the [InfluxDB documentation](https://docs.influxdata.com/influxdb/cloud/write-data/replication/replicate-data/).

Amazon Timestream for InfluxDB periodically takes internal backups and retains them for 24 hours to support availability and durability. Snapshots are taken during deletes and retained for 30 days to support restores. To access or use these, create a case at [AWS Support](https://console.aws.amazon.com/support/home?nc2=h_ql_cu#/).

## Manage and scale Timestream for InfluxDB
<a name="manage-scale"></a>

Timestream for InfluxDB supports instance classes that are ideal for running memory-intensive workloads in open source InfluxDB databases. The different [db.influx instance classes](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html#timestream-for-influx-dbi-classt-hw) have limits on vCPUs, memory, storage, and network bandwidth. To choose the instance class that fits your application's write and query latency requirements, observe the Amazon CloudWatch `CPUUtilization`, `MemoryUtilization`, and `DiskUtilization` metrics during testing. You can [scale your instances up and down](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influx-managing-modifying-db.html) based on your workload requirements. Timestream for InfluxDB provides multiple storage tiers that are preconfigured with optimal IOPS and throughput required for different types of workloads. Choose what works best for your workload based on your requirements.

If your scaling needs change at predictable times, you can use an [AWS Lambda function](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html) or a custom scheduler and run an API or SDK to scale up and down with some buffer time.

You manage your InfluxDB configuration in Timestream for InfluxDB by using parameters in a parameter group. Parameter groups act as a *container* for InfluxDB configuration options that are applied to one or more DB instances. When modifying parameters in parameter groups, understand the difference between static and dynamic parameters, and how and when they are applied. To see the current applied configuration, use the [GetDbParameterGroup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbParameterGroup.html) API action.
