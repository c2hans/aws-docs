---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/data-durability-and-ha-with-persistent-storage.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data durability and HA with persistent storage
<a name="data-durability-and-ha-with-persistent-storage"></a>

 Most RTC applications rely on persistent storage to store and access data for authentication, authorization, accounting (session data, call detail records, etc.), operational monitoring, and logging. In a traditional data center, ensuring high availability and durability for the persistent storage components (databases, file systems, and so on) typically requires heavy lifting via the setup of a storage area network (SAN), Redundant Array of Independent Disks (RAID) design, and processes for backup, restore, and failover processing. The AWS Cloud greatly simplifies and enhances traditional data center practices around data durability and availability.

 For object storage and file storage, AWS services like [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) and [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS) provide managed high availability and scalability. Amazon S3 has a data durability of 99.999999999% (11 nines).

 For transactional data storage, customers have the option to take advantage of the fully managed Amazon Relational Database Service (Amazon RDS) that supports Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle, and Microsoft SQL Server with high availability deployments. For the registrar function, subscriber profile, or accounting records storage (such as CDRs), the Amazon RDS provides a fault-tolerant, highly available and scalable option.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
