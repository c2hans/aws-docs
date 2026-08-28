---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/storage-types.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Storage types
<a name="storage-types"></a>

 AWS has many storage types for temporary and permanent requirements. In this section, we address the options for field experiences and lab testing with the SAS on AWS storage options.

## Permanent SAS data storage
<a name="permanent-sas-data-storage"></a>

 Permanent SAS storage is used for SAS 9.4, SAS data files, and SAS Viya CAS tables. SAS 9.4 data files hold either a SAS dataset holding actual data, or a SAS non- materialized view definition that references data stored elsewhere.

 Viya CAS is not only an analytic and transformation engine, it is also a data server. It loads data into a CAS table in order to analyze and process. The format of these tables

 can vary including SASHDAT, CSV, Oracle, SQL Server, or Hadoop, and it is backed into a permanent storage with content stored in-memory.

 The following permanent storage options are suggested to support the SAS data files and SAS Viya CAS tables:
+  **Elastic Block Storage (EBS)** – Stripe together a minimum of 4 EBS volumes for I/O bandwidth aggregation.
  +  EBS ST1 (throughput optimized HDD) Storage designed for large block sequential I/O. A 12.5 TB volume can sustain 500 MB/second. If the volume size is less than 500 MB per second of total bandwidth, it can be observed during the burst window.
  +  For high-throughput read-heavy workloads (like in SAS), update the [read-ahead setting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.html) on EBS ST1/IO1 from default 256 KB to 8 MB. EBS IO1 (provisioned IOS SSD) storage can also be used.
  +  Other EBS storage types like GP2 (general purpose storage) and SC1 (cold storage) are not suitable for permanent SAS 9 or SAS CAS data files.
  +  RAID 0 [configuration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/raid-config.html) is preferential because fault tolerance is not a determining criterion for these workloads.
  +  Customers can also choose to have EBS IO1 volumes (provisioned storage). However, costs would increase as IO1 volumes are charged by storage and by provisioned IOPS. For ex – 32K IOPS can yield as much as 500 MB/sec but customers would pay an additional amount for the desired provisioned IOPS.
+
  +  Using [SAS/Access to Redshift](http://support.sas.com/kb/63/001.html), SAS Datasets can be loaded into Amazon S3/Amazon Redshift using Amazon S3 capabilities of multi-part upload, transfer acceleration, and COPY/UNLOAD to Amazon Redshift for relational storage.

![Small diagram that shows directional bulk and standard loading from SAS into Amazon S3 or Amazon Redshift.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/images/redshift-bulk-load.jpeg)

### Temporary SAS data storage
<a name="temporary-sas-data-storage"></a>

 Most temporary SAS storages used in SAS WORK, SAS UTILLOC, and CAS\_DISK\_CACHE will not persist through reboots and are considered ephemeral storage.
+  I3 instances feature low latency NVMe SSDs striped together with RAID0. Use NVMe devices to support high bandwidth, low latency, and sequential I/O .
+  If additional storage is required, default to permanent SAS storage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
