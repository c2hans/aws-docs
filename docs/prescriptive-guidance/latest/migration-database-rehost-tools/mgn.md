---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/mgn.html
---

# Migration with AWS Application Migration Service
<a name="mgn"></a>

Most large lift-and-shift migrations to AWS use [AWS Transform MGN](https://aws.amazon.com/application-migration-service/). This service works on a physical level by moving data that is stored on any directly attached block storage device (such as a hard drive or SAN drive) to the corresponding Amazon Elastic Block Store (Amazon EBS) storage device on AWS. It essentially implements a traditional backup/restore procedure (by cloning the hard drives), but also provides a recovery point objective (RPO) of near seconds and a recovery time objective (RTO) of minutes by achieving continuous data protection (CDP) synchronization mode between the source systems and the target storage devices in the staging area.

This block-level replication method doesn't support network-attached storage (NAS), shared drives such as Network File System (NFS) shares, or Common Internet File System (CIFS) / Server Message Block (SMB) shares. It supports only block-level storage that's directly attached to the migrated system at the time of migration. (For more information, see the [MGN FAQ on SAN/NAS support](https://docs.aws.amazon.com/mgn/latest/ug/General-Questions-FAQ.html#SAN-NAS-Support).) This limits the applicability of replication through MGN for most clustered systems, because the majority of clusters rely on shared storage of various implementations. For more information, see the *Advantages* and *Disadvantages* sections on this page.

The block-level replication method requires you to install an AWS Replication Agent at the operating system (OS) level, and that agent supports only x86 platforms that are based on the Windows or Linux operating system (see [Operating systems supported by MGN](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)). Non-x86 platforms are out of scope for this migration method. These include ARM, RISC/CISC systems, PowerPC variations, IBM systems such as pSeries, iSeries, zSeries, and their respective operating systems such as AIX, HP-UX, Solaris, Linux for PowerPC, zLinux on mainframes, and other non-x86 architectures.

The AWS Replication Agent works at the level of a virtual file system device driver\* in the OS stack, capturing any data blocks to be written to the underlying block-level devices (including drives, hard drives, and directly attached SAN devices), as explained on the MGN FAQ page under these questions:
+ [What does the AWS Replication Agent do?](https://docs.aws.amazon.com/mgn/latest/ug/Agent-Related-FAQ.html#What-Agent-Do)
+ [Does the AWS Replication Agent cache any data to disk?](https://docs.aws.amazon.com/mgn/latest/ug/Agent-Related-FAQ.html#Does-Agent-Cache-Data)
+ [What is there to note regarding SAN/NAS support?](https://docs.aws.amazon.com/mgn/latest/ug/General-Questions-FAQ.html#SAN-NAS-Support)

**\*** See the definitions of [file system](https://en.wikipedia.org/wiki/File_system), [virtual file system](https://en.wikipedia.org/wiki/Virtual_file_system), and [device driver](https://en.wikipedia.org/wiki/Device_driver) in Wikipedia.

## Advantages
<a name="mgn-advantages"></a>

For lift-and-shift migrations of any scale, MGN has many benefits:
+ The replication is easy to set up. (It doesn't require a steep learning curve.)
+ It's fast to scale, by rolling out agents on the source machines.
+ You can use the [Cloud Migration Factory](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/) to automate most manual tasks, manage multiple machines, and orchestrate migration waves.
+ It supports a [wide range of x86 operating system architectures](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html).
+ It supports any type of source environment (on-premises data center, any other cloud, or another AWS Region).
+ It's application-agnostic, so it supports any application running on the source servers.
+ No license or purchase is required. AWS offers pay-as-you-go pricing, so you pay for the service only as long as you use it, without long-term contracts or complex licensing. MGN provides a free 90-day period per server, which is enough for most migrations. For details, see [AWS Transform MGN pricing](https://aws.amazon.com/application-migration-service/pricing/) on the AWS website.

## Disadvantages
<a name="mgn-disadvantages"></a>

When you use block-level replication tools such as MGN, you might encounter the following corner cases and factors to consider:
+ MGN doesn't support mounted shared file systems or shared storage devices such as NAS, including CIFS/SMB and NFS file systems. For more information about replication methods for NAS or shared file systems, see [MGN replication agent to migrate NFS Share](https://repost.aws/en/questions/QUgFBCo50lQsK_KVl1kcuqTQ/mgn-replication-agent-to-migrate-nfs-share) (AWS re:Post article) and [Migrate shared file systems in an AWS large migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-shared-file-systems-in-an-aws-large-migration.html) (AWS Prescriptive Guidance pattern).
+ MGN doesn't support most clustered file server or database cluster configurations with shared storage because of limitations in how that shared storage is represented to the OS level through the device driver layers. For example, Microsoft SQL Server clusters with the Storage Space Direct (S2D) option are not supported. However, you still can use MGN to replicate other types of clustered systems with shared block storage, such as shared storage in Failover Cluster Instance (FCI) configurations in Windows Server Failover Cluster (WSFC), as described in the blog post [Migrating your Microsoft Windows clusters to AWS using CloudEndure Migration](https://aws.amazon.com/blogs/storage/migrating-your-microsoft-windows-clusters-to-aws-using-cloudendure-migration/), storage exposed from external SAN arrays (iSCSI connections), and some Microsoft SQL Server Always On availability group (AAG) clusters in specific corner cases. In general, MGN supports replication of a block-level device from a server where the storage device is fully present on the server during the migration. (The AWS Replication Agent must be installed on the server, and the device must be visible to the agent for replication.) However, all of these scenarios require very specific procedures and result in longer cutover windows.
+ Systems that have a high rate of data changes (such as OLTP databases) might have higher performance or network requirements, which complicate migration efforts.
+ Network bandwidth must be sufficient for the amount of data to be transferred within the planned migration and cutover time window. This is because MGN doesn't provide an offline shipping option, unlike [AWS Snowball](https://aws.amazon.com/snowball/).
+ Migration requires a small downtime window, within an RTO of minutes. MGN uses EBS snapshots as part of the migration process, and new EBS disks that are created from such snapshots initially have worse performance. With some database read patterns, this might increase the effective cutover window until the migrated database is at full performance.

## Best-fit scenarios
<a name="mgn-scenarios"></a>

MGN covers almost any lift-and-shift migration fully, with few disadvantages, as discussed in the previous two sections. This tool can handle most of the corner cases, such as database clusters, as long as the longer cutover window required for these systems satisfies your migration requirements.

The following sections cover two scenarios in more depth:
+ Large-scale migration with multiple migration waves
+ Single application migration that requires minimal downtime

### Large-scale migration with multiple migration waves
<a name="large-scale-migration-with-multiple-migration-waves.197881f4-d61b-5ea9-8a0d-2ddccba40748"></a>

An example of a large-scale migration is a data center exit that is characterized by size and speed requirements. It also usually involves a specific time constraint, such as the end of the lease contract for the data center. In this case, the scale dictates the approach. The migration waves are determined and grouped by applications, including databases, and each wave has a planned preparation, migration, and final cutover phase with specific downtime requirements.

Inside each migration wave, the database servers are best moved at scale by using MGN block-level replication, except for a few exceptions for the following special cases that might require a separate migration approach:
+ Most clustered database systems
+ Database systems where the rate of change exceeds available network throughput (which might result in a replication lag)

For each special case, consider the tradeoff between your downtime requirements and the level of effort involved in using another migration tool. In some cases, it's much easier to use the same migration approach for all systems instead of using separate tools and creating different processes for specific systems. If MGN doesn't support the downtime requirements for a specific system, we recommend that you use one of the methods described in the [Migration with native database tools](dms.md) section instead.

### Single application migration
<a name="single-application-migration.e9cccc01-93cf-5d89-b6f9-d0de6e4f300f"></a>

The single application scenario represents a granular approach for migrating a single business-critical application that requires minimum or near-zero downtime during migration, or a few such applications. The scope of the migration might vary, depending on business criticality and downtime requirements, in contrast to the speed and scale requirements of the previous (large-scale migration) scenario. If the application allows for downtime within the RTO of MGN, it should be handled in the same way as any large-scale migration described earlier.

However, in cases where the cutover time must be as close to the minimum as possible―for example, when the migrated database has read patterns that require a long time to operate at full performance and the cutover windows have to remain small―you should consider a more detailed and granular approach. In general, that approach involves additional steps and requirements, which require more effort and time. One of the steps is to separate the database migration from the application server migration and to use the database migration tools described in the [next section](dms.md) to keep the source and the target databases in sync. You can use various methods to achieve synchronization. Each method has advantages and disadvantages, and involves different tradeoffs between the amount of downtime and the complexity of synchronization. Nevertheless, keeping the database in sync between the source and target environments enables you to unlink the database layer from the application layer. Assuming that application servers don't store persistent data locally but pass everything to the database layer, synchronization also removes downtime restrictions from the application layer.

Decoupling the database and application layers enables you to migrate application servers by using MGN as in the previous scenario. Target application servers can be started in the target environment while source systems are still working, processing the data, and storing it in the database layer. Because the database layer is already in sync with the target, cutover time is minimal―it only involves switching networks and redirecting customer requests from the old source system to the target environment. You can use multiple methods to do this, following the guidance for [blue/green deployments](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/update-dns-routing-with-amazon-route-53.html), typically by switching DNS endpoints, using weighted DNS zones, using [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) to reduce Time to Live (TTL) DNS propagation delays, and similar methods.
