---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/sas-on-aws.html
---

# Considerations for SAS on AWS
<a name="sas-on-aws"></a>

## SAS background
<a name="sas-background"></a>
+ SAS Permanent Data File Space (SASDATA)
  + Stores persistent data for SAS exploitation and resulting SAS output files
  + Extensively read from, but less extensively written back out
+ SAS Working Data File Space (SASWORK)
  + Scratch working space for SAS jobs
  + Used to perform the working storage activity of single-threaded SAS procedures
+ SAS Utility Data File Space (UTILLOC)
  + Same type of space as SASWORK for multi-threaded SAS procedures
  + By default, placed as a subdirectory under SASWORK
+ Storage does not persist through a reboot or restart of internal solid state (SSD) devices that are striped together in a RAID 0 configuration. We recommend that you use instances with non-volatile memory express (NVMe) ephemeral devices with high bandwidth, low latency, and sequential I/O. These instances are ideal for temporary SAS data (SASWORK and UTILLOC).

## SAS shared file system (required for SAS Grid)
<a name="sas-shared"></a>
+ AWS sets up Lustre file systems with the **rw**, **seclabel**, and **lazystatfs** mount options. These are not the recommended mount options for SAS Grid, so you will have to unmount these FSx for Lustre file systems and remount them with the **flock** parameter.
+ Amazon FSx for Lustre supports storage capacity scaling. You can increase the storage capacity of your file system as your data grows, and the file system remains online and available during the scaling operation. For more information, see [Managing storage and throughput capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-storage-capacity.html) in the FSx for Lustre documentation.
+ For FSx for Lustre persistent file systems, data is replicated within a single Availability Zone for increased durability. It is not replicated across AWS Availability Zones.
+ We recommend that you use the Amazon S3 storage option for use with SAS Grid and FSx for Lustre. For more information, see [Using Data Repositories with FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-data-repositories.html) in the AWS documentation.
+ See the [AWS Region table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) for availability of services across AWS Regions and Availability Zones. Also review [Amazon S3 same-Region replication (SRR) or cross-Region replication (CRR)](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html) for implications of data replication needs for high availability.

## SAS Grid server tier instance types
<a name="server-tier-instances"></a>

SAS Grid servers need fast CPUs for processing data. We recommend:
+ A minimum of 8 GB of physical RAM per physical core, and robust I/O throughput (especially for SASWORK and SAS UTILLOC).
+ [I3 instances](https://aws.amazon.com/ec2/instance-types/i3/) – Amazon EC2 I3 instances are storage-optimized for high transaction, low latency workloads. These instances include NVMe SSD-based instances that are storage-optimized for high random I/O performance, high sequential read throughput, and high IOPS. Because of the high internal I/O bandwidth from striped NVMe SSD drives for SASWORK and SAS UTILLOC, you should configure your environment to explicitly use the NVMe-based SSD local drives instead of Amazon EBS volumes.
+ [I3en instances](https://aws.amazon.com/ec2/instance-types/i3en/) – This family provides NVMe SSD instances that are storage-optimized on Amazon EC2 with enhanced networking via ENA to achieve up to 100 Gbps of network bandwidth.
+ [M5n instances](https://aws.amazon.com/ec2/instance-types/m5/) – The M5 family provides a balance of compute, memory and networking. M5n instances are ideal for applications that require improved network throughput and packet rate performance.
+ SAS workloads can be characterized as predominately large, sequential I/O requests with high volumes of data. We recommend that you predetermine your SAS usage patterns. This will guide the optimal architecture and setup of the individual underlying file systems and their respective physical I/O provisioning.
  + Query, reporting, and light statistical jobs usually perform well with an I/O rate of 100 MiB per second per physical CPU core.
  + Advanced analytics and heavy statistical jobs might require up to 150 MiB per second per physical CPU core.
  + Overall, we recommend a minimum I/O throughput rate of 100-125 MiB per second per physical CPU core.

**Note**
Instance types listed were current as of the original publication. Newer generations are now available that may offer improved performance and cost efficiency. **I4i instances** (newer than I3) can provide better I/O performance. **M7i instances** (newer than M5n) can provide enhanced compute performance. Evaluate these newer instance types for your SAS Grid workload requirements.

## SAS Grid middle tier and metadata server tier instance types
<a name="mid-tier-instances"></a>

These servers do not require computing-intensive resources or robust I/O throughput. They do require access to more memory than the SAS computing tiers. We recommend:
+ A minimum of 24 GB of physical RAM or 8 GB of physical RAM per physical core, whichever is larger.
+ [R5 or R5d instances](https://aws.amazon.com/ec2/instance-types/r5/) – These instances are suitable for memory-intensive applications such as in-memory caches, mid-size in-memory databases, and real-time big data analytics.
**Note**
Instance types listed were current as of the original publication. Newer generations are now available that may offer improved performance and cost efficiency. **R7i instances** (newer than R5/R5d) can improve memory bandwidth. Evaluate these newer instance types for your SAS Grid workload requirements.

## High availability and disaster recovery for SAS Grid
<a name="ha-dr"></a>

Disaster recovery planning is important for any critical business system, including production systems that are running the SAS Intelligence Platform and SAS solutions.

Disaster recovery is not the same as high availability. Although both concepts are related to business continuity, high availability is about providing undisrupted continuity of operations. In contrast, disaster recovery involves some amount of downtime, typically measured in hours or days.

Use [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) for centralized backup management of FSx for Lustre file systems, Amazon EBS volumes, and Amazon RDS databases. AWS Backup supports automated backup policies, lifecycle management, and cross-Region copy for disaster recovery scenarios.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
