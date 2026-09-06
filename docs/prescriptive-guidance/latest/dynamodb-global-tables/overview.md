---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/overview.html
---

# Overview
<a name="overview"></a>

## Key facts
<a name="key-facts"></a>
+ There are two versions of global tables: version [11.29 (legacy)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V1.html) (sometimes called *v1*) and [version 2019.11.21 (current)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.V2.html) (sometimes called *v2*). This guide focuses exclusively on the current version.
+ DynamoDB (without global tables) is a Regional service, which means that it is highly available and intrinsically resilient to failures of infrastructure, including the failure of an entire Availability Zone. A single-Region DynamoDB table is designed for 99.99% availability. For more information, see the [DynamoDB service-level agreement (SLA)](https://aws.amazon.com/dynamodb/sla/).
+ A DynamoDB global table replicates its data between two or more Regions. A multi-Region DynamoDB table is designed for 99.999% availability. With proper planning, global tables can help create an architecture that is resilient to Regional failures.
+ DynamoDB doesn't have a global endpoint. All requests are made to a Regional endpoint that accesses the global table instance that's local to that Region.
+ Calls to DynamoDB should not go across Regions. The best practice is for an application that is homed to one Region to directly access only the local DynamoDB endpoint for its Region. If problems are detected within a Region (in the DynamoDB layer or in the surrounding stack), end user traffic should be routed to a different application endpoint that's hosted in a different Region. Global tables ensure that the application homed in every Region has access to the same data.

## Consistency modes
<a name="consistency-modes"></a>

When you create a global table, you configure its consistency mode. Global tables support two consistency modes: multi-Region eventual consistency (MREC) and multi-Region strong consistency (MRSC), which was introduced in June 2025.

If you do not specify a consistency mode when you create a global table, the global table defaults to MREC. A global table cannot contain replicas that are configured with different consistency modes. You cannot change a global table's consistency mode after its creation.

### Key facts about MREC
<a name="key-facts-about-mrec.fc3c67a9-a82f-5f2b-848e-63546822bc4d"></a>
+ Global tables that use MREC employ an active-active replication model. From the perspective of DynamoDB, the table in each Region has equal standing to accept read and write requests. After receiving a write request, the local replica table replicates the write operation to other participating remote Regions in the background.
+ Items are replicated individually. Items that are updated within a single transaction might not be replicated together.
+ Each table partition in the source Region replicates its write operations in parallel with every other partition. The sequence of write operations within a remote Region might not match the sequence of write operations that happened within the source Region. For more information about table partitions, see the blog post [Scaling DynamoDB: How partitions, hot keys, and split for heat impact performance](https://aws.amazon.com/blogs/database/part-3-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/).
+ A newly written item is usually propagated to all replica tables within a second. Nearby Regions tend to propagate faster.
+ Amazon CloudWatch provides a `ReplicationLatency` metric for each Region pair. It is calculated by looking at arriving items, comparing their arrival time with their initial write time, and computing an average. Timings are stored within CloudWatch in the source Region. Viewing the average and maximum timings can be useful for determining the average and worst-case replication lag. There is no SLA on this latency.
+ If an individual item is updated at about the same time (within this `ReplicationLatency` window) in two different Regions, and the second write operation happens before the first write operation was replicated, there's a potential for write conflicts. Global tables that use MREC resolve such conflicts by using a *last writer wins* mechanism, based on the timestamp of the write operations. The first operation "loses" to the second operation. These conflicts aren't recorded in CloudWatch or AWS CloudTrail.
+ Each item has a last write timestamp held as a private system property. The *last writer wins* approach is implemented by using a conditional write operation that requires the incoming item's timestamp to be greater than the existing item's timestamp.
+ A global table replicates all items to all participating Regions. If you want to have different replication scopes, you can create multiple global tables and assign each table different participating Regions.
+ The local Region accepts write operations even if the replica Region is offline or `ReplicationLatency` grows. The local table continues to attempt replicating items to the remote table until each item succeeds.
+ In the unlikely event that a Region goes fully offline, when it comes back online later, all pending outbound and inbound replications will be retried. No special action is required to bring the tables back in sync. The *last writer wins* mechanism ensures that the data eventually becomes consistent.
+ You can add a new Region to a DynamoDB MREC table at any time. DynamoDB handles the initial sync and ongoing replication. You can also remove a Region (even the original Region), and this will delete the local table in that Region.

### Key facts about MRSC
<a name="key-facts-about-mrsc.7db3b9a9-10c3-56d0-af46-76036d235b02"></a>
+ Global tables that use MRSC also employ an active-active replication model. From the perspective of DynamoDB, the table in each Region has equal standing to accept read and write requests. Item changes in an MRSC global table replica are **synchronously** replicated to at least one other Region before the write operation returns a successful response.
+ Strongly consistent read operations on any MRSC replica always return the latest version of an item. Conditional write operations always evaluate the condition expression against the latest version of an item. Updates always operate against the latest version of an item.
+ Eventually consistent read operations on an MRSC replica might not include changes that recently occurred in another Region, and might not even include changes that very recently occurred in the same Region.
+ A write operation fails with a `ReplicatedWriteConflictException` exception when it attempts to modify an item that is already being modified in another Region. Write operations that fail with the `ReplicatedWriteConflictException` exception can be retried and will succeed if the item is no longer being modified in another Region.
+ With MRSC, latencies are higher for write operations and for strongly consistent read operations. These operations require cross-Region communication. (For more information, see the AWS re:Invent 2024 presentation, [Multi-Region strong consistency with Amazon DynamoDB global tables](https://www.youtube.com/watch?v=R-nTs8ZD8mA).) This communication tends to add latency that increases based on the round-trip latency between the Region that is being accessed and the nearest Region that participates in the global table. Eventually consistent read operations experience no extra latency. There is an open source [tester tool](https://github.com/awslabs/amazon-dynamodb-tools/tree/main/tester) that lets you experimentally calculate these latencies with your Regions.
+ Items are replicated individually. Global tables that use MRSC do not support the transaction APIs.
+ An MRSC global table must be deployed in exactly three Regions. You can configure an MRSC global table with three replicas, or with two replicas and one witness. A witness is a component of an MRSC global table that contains recent data written to global table replicas. A witness provides an optional alternative to a full replica while supporting MRSC's availability architecture. You cannot perform read or write operations on a witness. A witness does not incur storage or write costs. A witness is located within a different Region from the two replicas.
+ To create an MRSC global table, you add one replica and a witness, or add  two replicas to an existing DynamoDB table that contains no data. You cannot add additional replicas to an existing MRSC global table. You cannot delete a single replica or a witness from an MRSC global table. You can delete two replicas, or delete one replica and a witness, from an MRSC global table. The second scenario converts the remaining replica to a single-Region DynamoDB table.
+ You can determine whether an MRSC global table has a witness configured, and which Region it's configured in, from the output of the [DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html) API. The witness is owned and managed by DynamoDB and does not appear in your AWS account in the Region where it is configured.
+ MRSC global tables are available in the following Region sets:
  + US Region set: US East (N. Virginia), US East (Ohio), US West (Oregon)
  + EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt)
  + AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), and Asia Pacific (Osaka)
+ MRSC global tables cannot span Region sets. For example, an MRSC global table cannot contain replicas from both US and EU Region sets.
+ Time to live (TTL) is not supported for MRSC global tables.
+ Local secondary indexes (LSIs) are not supported for MRSC global tables.
+ [CloudWatch Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) information is reported only for the Region in which an operation occurred.
+ The local Region accepts all read and write operations as long as a second Region that hosts a replica or witness is available to establish quorum. If a second Region isn't available, the local Region can service only eventually consistent reads.
+ In the unlikely event that a Region goes fully offline, when it comes back online later, it will automatically catch up. Until it's caught up, write operations and strongly consistent read operations will return errors. However, eventually consistent read operations will return the data that has so far been propagated into the Region, with usual local consistency behavior between the leader node and local replicas. No special action is required to bring the tables back in sync.

## Use cases
<a name="use-cases"></a>

MREC global tables provide these benefits:
+ **Lower-latency read operations**. You place a copy of the data closer to the end user to reduce network latency during read operations. The data is kept as fresh as the `ReplicationLatency` value.
+ **Lower-latency write operations**. An end user can write to a nearby Region to reduce network latency and the time to complete the write operation. The write traffic must be carefully routed to ensure that there are no conflicts. Techniques for routing are discussed in a [later section](routing-strategies.md).
+ **Seamless Region migration**. You can add a new Region and then delete the old Region to migrate a deployment from one Region to another, without any downtime at the data layer.

MREC and MRSC global tables both provide this benefit:
+ **Increased resiliency and disaster recovery**. If a Region has degraded performance or a full outage, you can evacuate it (that is, move away some or all requests that go to that Region). Using global tables increases the [DynamoDB SLA](https://aws.amazon.com/dynamodb/sla/) for monthly uptime percentage from 99.99% to 99.999%. Using MREC supports a recovery point objective (RPO) and recovery time objective (RTO) measured in seconds. Using MRSC supports an RPO of zero.

  For example, Fidelity Investments [presented at re:Invent 2022](https://youtu.be/QUpV5MDu4Ys?t=706) on how they use DynamoDB global tables for their Order Management System. Their goal was to achieve reliably low latency processing at a scale they couldn't attain with on-premises processing while also maintaining resilience to Availability Zone and Regional failures.

If your goal is resiliency and disaster recovery, MRSC tables have higher write latencies and higher strongly consistent read latencies, but support an RPO of zero. MREC global tables support an RPO that's equal to the replication delay between replicas—usually a few seconds depending on the replica Regions. For more information, see [Consistency modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes) in the DynamoDB documentation.
