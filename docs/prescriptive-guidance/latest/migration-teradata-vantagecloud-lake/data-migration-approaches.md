---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-teradata-vantagecloud-lake/data-migration-approaches.html
---

# Data migration approaches
<a name="data-migration-approaches"></a>

This section provides an overview of the most common migration approaches and highlights some of the key benefits and challenges of each approach. The following tools are used in the data migration approaches covered in this section:
+ Teradata Data Transfer Utility (DTU) – offline migration
+ Network attached storage (NAS) cloud storage device – physical data migration by using AWS Snowball

Use the following table to identify the migration approach that meets your requirements.

|
|
| Approach | Description | Benefits | Challenges |
| --- |--- |--- |--- |
| Teradata DTU with systems offline (recommended) | Uses DTU streaming to migrate data from the on-premises source to the AWS target environment. | + Maximizes throughput and minimizes the impacts of network and database restarts on migration+ Offers the fastest elapsed time for migration+ Streamlines support from the data migration, global support, and engineering teams | Source system outage during migration |
| Teradata DSA migration using a NAS device | Uses the Data Stream Utility (DSU) to migrate data from the source to a NAS cloud storage device (for example, AWS Snowball), transport the cloud storage device to a cloud data center, and offload to cloud storage (for example, to Amazon S3). Or, it uses DSU to migrate data from cloud storage to the target environment.<br />  | Workaround for poor network capacity to the cloud | + Logistics, risk of damage to storage device in transport, multiple migrations might be required+ Longer elapsed time+ Requires significant effort to synchronize target with source systems after migration  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
