---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-teradata-vantagecloud-aws/migration-approaches.html
---

# Data migration approaches
<a name="migration-approaches"></a>

This section provides an overview of the most common migration approaches, and highlights some of the key benefits and challenges of each approach. The following tools are used in the data migration approaches covered in this section:
+ Teradata Data Transfer Utility (DTU) – Offline migration
+ Network-attached storage (NAS) cloud storage device – Physical data migration using AWS Snowball

Use the following table to identify the migration approach that meets your requirements.

|
|
| Approach | Description | Benefits | Challenges |
| --- |--- |--- |--- |
| Teradata DTU with systems offline (recommended) | Uses DTU streaming to migrate data from on-premises source to AWS target environment | Maximizes throughput and minimizes the impacts of network and database restarts on migration<br />Offers the fastest elapsed time for migration<br />Streamlines support from the Data Migration, Global Support, and Engineering teams | Source system outage during migration |
| Teradata Data Stream Architecture (DSA) migration using a NAS device | Uses the Data Stream Utility (DSU) to migrate data from the source to a NAS cloud storage device (for example, Snowball), transport cloud storage device to a cloud data center, and offload cloud storage such as Amazon Simple Storage Service (Amazon S3), or use DSU to migrate data from cloud storage to the target environment | Workaround for poor network capacity to cloud | Logistics, risk of damage to storage device in transport, multiple migrations might be required<br />Longer elapsed time<br />Requires significant effort to sync target to source systems post-migration  |
