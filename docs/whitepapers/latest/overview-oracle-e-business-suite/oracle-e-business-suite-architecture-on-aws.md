---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/oracle-e-business-suite-architecture-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle E-Business Suite architecture on AWS
<a name="oracle-e-business-suite-architecture-on-aws"></a>

 The following reference diagram illustrates how Oracle E-Business Suite can be deployed on AWS. The application and database tiers are deployed across multiple Availability Zones for high availability.

![Diagram showing a sample Oracle E-Business Suite deployment on AWS](https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/images/sample-oracle-e-business-suite-deployment-on-aws.png)

 User requests from the client tier are routed using Amazon Route53 DNS to the Oracle E-Business Suite application servers deployed on EC2 instances through Application Load Balancer. The OHS and the Oracle WLS are deployed on each application tier instance. The OHS accepts the requests from Application Load Balancer and routes them to the Oracle WLS. The Oracle WLS runs the appropriate business logic and communicates with the Oracle database.

 The various modules and functions within Oracle E-Business Suite share a common data model. There is only one Oracle database instance for multiple application tier nodes. Database tier for Oracle E-Business Suite can be deployed either on Amazon RDS Custom for Oracle managed service or self-managed Oracle database on Amazon EC2.

## Load balancing and high availability
<a name="load-balancing-and-high-availability"></a>

 Application Load Balancer is used to distribute incoming traffic across multiple application tier instances deployed across multiple Availability Zones. You can add and remove application tier instances from your load balancer as your needs change, without disrupting the overall flow of information. Application Load Balancer ensures that only healthy instances receive traffic by detecting unhealthy instances and rerouting traffic across the remaining healthy instances.

 If an application tier instance fails, Application Load Balancer automatically reroutes the traffic to the remaining running application tier instances. In the unlikely event of an Availability Zone failure, user traffic is routed to the remaining application tier instances in the other Availability Zone.

 Other third-party load balancers like the F5 BIG-IP are available on AWS Marketplace and can be used as well. See [My Oracle Support document 1375686.1](https://support.oracle.com/epmos/faces/DocumentDisplay?parent=DOCUMENT&sourceId=1375686.1&id=1375686.1) for more details on using load balancers with Oracle E-Business Suite (sign in required).

 If the database tier is deployed on RDS Custom for Oracle, then create its replica in another Availability Zone. Replica uses Oracle Data Guard for asynchronous (maximum performance) replication between primary and standby. Protection mode for Data Guard can be changed to maximum availability or maximum protection as desired.

 If the database tier is deployed on an EC2 instance, then create its Oracle Data Guard standby on EC2 instance in a different Availability Zone. If the primary database fails, the standby database is promoted as the primary and the application tier instances will connect to it.

 For more details on deploying Oracle Database on AWS, see the [Oracle Database on AWS](https://aws-quickstart.github.io/quickstart-oracle-database/#_overview) Quick Start.

## Scalability
<a name="scalability"></a>

 When using AWS, you can scale your application easily due to the elastic nature of the cloud. You can scale up the Oracle E-Business Suite application tier and database tier instances simply by changing the instance type to a larger instance type.

 For example, you can start with an `r5.large` instance with two vCPUs and 16 GiB RAM and scale up all the way to an `x1e.32xlarge` instance with 128 vCPUs and 3,904 GiB RAM. After selecting a new instance type, only a restart is required for the changes to take effect. Typically, the resizing operation is completed in a few minutes, the EBS volumes remain attached to the instances, and no data migration is required.

 You can scale out the application tier by adding and configuring more application tier instances when required. You can launch a new EC2 instance in a few minutes. However, additional work is required to ensure that the AutoConfig files are correct and the new application tier instance is correctly configured and registered with the database.

 Although it might be possible to automate scaling out the application tier using scripting, this requires an additional technical investment. A simpler alternative might be to use standby EC2 instances, as explained in the next section.

 If the database tier is deployed on RDS Custom for Oracle, then you can use RDS Custom for Oracle read replica to offload some production reporting workloads (for example, selected Concurrent Manager reports) from the primary RDS Custom for Oracle instance.

## Standby EC2 instances (application tier)
<a name="standby-ec2-instances"></a>

 To meet extra capacity requirements, additional application tier instances of Oracle E-Business Suite can be pre-installed and configured on EC2 instances. These standby instances can be shut down until extra capacity is required. Charges are not incurred when EC2 instances are shut down—only EBS storage charges are incurred.

 At the time of this publication, EBS General Purpose (`gp2`) volumes are priced at $0.10 per GB per month in the US East (Ohio) Region. Therefore, for an EC2 instance with 120 GB hard disk drive (HDD) space the storage charge is only $12 per month. These pre-installed standby instances provide you the flexibility to use these instances for meeting additional capacity needs as and when required. In this model, you need to ensure that any configuration changes/patching/maintenance activities are also applied to the standby node to avoid inconsistencies.

## Storage options and backup
<a name="storage-options-and-backup"></a>

 AWS offers a complete range of cloud storage services to support both application and archival compliance requirements. You can choose from object, file, block, and archival services. The following table lists some of the storage options and how they can be used when deploying Oracle E-Business Suite on AWS.

 *Table 1 – Storage options and how they can be used *

|  Storage type  |  Storage characteristics  |  Oracle E-Business Suite use case  |
| --- | --- | --- |
|  [Amazon EBS](https://aws.amazon.com/ebs/) – gp2/gp3 volumes  |  SSD-based block storage with up to 16,000 input/output operations per second (IOPS) per volume  |  Boot volumes, operating system and software binaries, Oracle database archive logs  |
|  Amazon EBS – io1/io2/io2 Block Express volumes  |  SSD-based block storage with up to 64,000 IOPS per volume. Multiple volumes can be striped together for higher IOPS. By attaching io2 volumes to r5b instance types, you can achieve up to 256,000 IOPS per volume.  |  Storage for the database tier – ASM disks, Oracle data files, redo logs  |
|  [Amazon EFS](https://aws.amazon.com/efs/)  |  Highly durable, NFSv4.1 compatible file system  |  PCP out and log files, media staging  |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  Object store with 99.999999999% durability  |  Backups, archives, media staging  |
|  [Amazon Glacier](https://aws.amazon.com/s3/glacier/)  |  Extremely low-cost and highly durable storage for long-term backup and archival  |  Long-term backup and archival  |
|  [Amazon EC2 instance storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)  |  Ephemeral or temporary storage, data persists only for the lifetime of the instance  |  Swap, temporary files, reports cache, Web Server cache  |

 The application and database servers use EBS volumes for persistent block storage. Amazon EBS has two types of solid-state drive (SSD)-backed volumes: provisioned IOPS SSD (`io1`, `io2`, `io2 Block Express`) for latency-sensitive database and application workloads, and general-purpose SSD (`gp2`, `gp3`) that balances price and performance for a wide variety of transactional workloads, including development and test environments, and boot volumes.

 General purpose SSD volumes provide good balance between price and performance and can be used for boot volumes, the Oracle E-Business Suite application tier file system, and logs. They are designed to offer single-digit millisecond latencies and deliver a consistent baseline performance of 3 IOPS/GB for `gp2` and 3,000 IOPS regardless of volume size for `gp3` to a maximum of 16,000 IOPS per volume.

 Provisioned IOPS volumes are the highest performance EBS storage option and can be used for storing the Oracle database data and log files. You can provision up to 64,000 IOPS per `io1` or `io2` volume and 256,000 per `io2 Block Express`. These volumes are designed to achieve single-digit millisecond latencies and to deliver the provisioned IOPS 99.9% for `i01` and 99.999% of the time for `io2` and `io2 Block Express`. For database tier on Amazon EC2, you can use Oracle Automatic Storage Management (ASM) or Linux Volume Manager (LVM) to stripe the data across multiple EBS volumes for higher IOPS and to scale the database storage throughput.

 To maximize the performance of EBS volumes, use [EBS-optimized EC2 instances](https://aws.amazon.com/ebs/details/#ebsoptimized) and instances based on the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/).

 EC2 instances have temporary SSD-based block storage called [instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html). Instance storage persists only for the lifetime of the instance and should not be used to store valuable, long-term data. Instance storage can be used as swap space and for storing temporary files like the report cache or web server cache. If you are using Oracle Linux as the operating system for the database server, you can use the instance storage for the Oracle Database Smart Flash Cache to improve the database performance.

 Parallel Concurrent Processing (PCP) allows you to distribute concurrent managers across multiple nodes so that you can use the available capacity and provide failover. You can use a shared file system such as Amazon EFS for storing the log and out files while implementing PCP in Oracle E-Business Suite. However, this configuration may not be ideal for environments with an extremely large number of `log` and `out` files.

 Oracle E-Business Suite Release 12.2 introduced a new environment variable, `APPLLDM`, to specify whether log and out files are stored in a single directory for all Oracle E-Business Suite products, or in one subdirectory per product. `APPLLDM` can be set to 'single' or 'product'. 'product' will avoid the highest concentration of `log` and `out` files in a single directory and may avoid performance issues.

 Amazon S3 provides low cost, scalable, and highly durable storage and should be used for storing backups. You can use Oracle Recovery Manager (RMAN) to back up your database, then copy the data to Amazon S3. Additionally, if your database tier is on RDS Custom for Oracle, automated backups are enabled by default and can be retained up to 35 days. This includes daily snapshot backups and transaction logs backups. You can also take manual snapshots which can be retained as long as you need.

 Alternatively, you can use the Oracle Secure Backup (OSB) Cloud Module to back up your database. The OSB Cloud Module is fully integrated with RMAN features and functionality, and the backups are sent directly to Amazon S3 for storage.
