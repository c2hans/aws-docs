---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/storage.html
---

# Storage capacity
<a name="storage"></a>

Amazon RDS for Oracle supports the following AWS storage types:
+ General Purpose solid-state drive (SSD): gp2, gp3
+ Provisioned IOPS SSD: io1, io2
+ Magnetic

The storage types differ in performance characteristics and price. You can tailor storage performance and cost to the needs of your database workload.

Amazon RDS Custom for Oracle supports SSD storage type gp2, gp3 and io1. Magnetic storage isn't supported.

The maximum IOPS and throughput per RDS instance depends on the selected storage type and instance class. For more information, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html).

Amazon RDS for Oracle provides storage autoscaling that can automatically scale storage capacity in response to growing database workloads, with zero downtime. Amazon RDS storage autoscaling continuously monitors storage consumption. Capacity scales up automatically when actual utilization approaches provisioned storage capacity. There is no additional cost for enabling the storage autoscaling feature. You pay only for the storage that is provisioned.

Amazon RDS Custom for Oracle doesn't support storage autoscaling. You must manually provision storage.

|
|
| Storage features | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| Storage type | All | gp2, gp3, io1 |
| Maximum storage size | 64 TiB | 64 TiB |
| Maximum IOPS per instance | 256,000 | 256,000 |
| Maximum throughput per instance | 16,000 MiB/s | 4,000 MiB/s |
| Storage autoscaling | Yes | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
