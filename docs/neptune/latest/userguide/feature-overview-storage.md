---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-storage.html
---

# Amazon Neptune storage, reliability and availability
<a name="feature-overview-storage"></a>

Amazon Neptune uses a distributed and shared storage architecture that scales automatically as your database storage needs grow.

Neptune data is stored in a cluster volume, which is a single, virtual volume that uses Non-Volatile Memory Express (NVMe) SSD-based drives. A cluster volume can grow to a maximum size of 128 tebibytes (TiB) (64 TiB in the China Regions and the AWS GovCloud (US) Regions). A cluster volume consists of copies of the data across three Availability Zones (AZs) in a single AWS Region, which provides high durability and availability.

The [Storage](storage.md) section covers these topics in detail:
+ **[Allocation](storage.md#storage-allocation)** – You are charged for space allocated, as determined by the storage high water mark.
+ **[Storage billing](storage.md#storage-billing)** – Storage costs are billed based on the high water mark, and Neptune also offers an [I/O–Optimized](storage-types.md#provisioned-iops-storage) pricing option for I/O–intensive workloads.
+ **[Reliability and high availability](storage.md#storage-reliability)** – Neptune replicates your data across three Availability Zones for high durability and automatic fault recovery.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
