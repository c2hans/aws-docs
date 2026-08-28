---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/data-tier-amazon-aurora-and-amazon-elasticache.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data tier (Amazon Aurora and Amazon ElastiCache)
<a name="data-tier-amazon-aurora-and-amazon-elasticache"></a>

 With the WordPress installation stored on a distributed, scalable, shared network file system, and static assets being served from Amazon S3, you can focus your attention on the remaining stateful component: the database. As with the storage tier, the database should not be reliant on any single server, so it cannot be hosted on one of the web servers. Instead, host the WordPress database on Amazon Aurora.

 [Amazon Aurora](https://aws.amazon.com/rds/aurora) is a MySQL and PostgreSQL compatible relational database built for the cloud that combines the performance and availability of high-end commercial databases with the simplicity and cost-effectiveness of open source databases. Aurora MySQL increases MySQL performance and availability by tightly integrating the database engine with a purpose-built distributed storage system, backed by SSD. It is fault-tolerant and self-healing, replicates six copies of your data across three Availability Zones, is designed for greater than 99.99% availability, and continuously backs up your data in Amazon S3. Amazon Aurora is designed to automatically detect database crashes and restart without the need for crash recovery or to rebuild the database cache.

 Amazon Aurora provides a number of [instances types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) to suit different application profiles, including memory-optimized and burstable instances. To improve the performance of your database you can select a large instance type to provide more CPU and memory resources.

 Amazon Aurora automatically handles failover between the primary instance and [Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Replication.html) so that your applications can resume database operations as quickly as possible without manual administrative intervention. Failover typically takes less than 30 seconds.

 After you have created at least one Aurora Replica, connect to your primary instance using the cluster endpoint to allow your application to automatically fail over in the event the primary instance fails. You can create up to 15 low-latency read replicas across three Availability Zones.

 As your database scales, your database cache will also need to scale. As discussed previously in the [Database Caching](database-caching.md) section, ElastiCache has features to scale the cache across multiple nodes in an ElastiCache cluster, and across multiple Availability Zones in a Region for improved availability. As you scale your ElastiCache cluster, ensure that you configure your caching plugin to connect using the configuration endpoint so that WordPress can use new cluster nodes as they are added and stop using old cluster nodes as they are removed. You must also set up your web servers to use the [ElastiCache Cluster Client for PHP](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Appendix.PHPAutoDiscoverySetup.html) and update your AMI to store this change.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
