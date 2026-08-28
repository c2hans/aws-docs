---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/dms.html
---

# Migration with native database tools and AWS DMS
<a name="dms"></a>

Many DBAs are familiar with a wide range of tools that handle database migration and replication. These tools are typically offered by database engine vendors and third-party companies, and they work on the logical level of the specific database engine, unlike the fully application-agnostic, block-level replication approach offered by MGN.

Here's a list of these tools, ranging from the simplest to more complex approaches:
+ ***Full backup/restore*** is a familiar, well-known, and easy to use process for IT staff. The method depends on the type of the database engine. The process usually moves multiple logical databases that are colocated on the same database server, and can also be used to restore the databases into a managed service such as Amazon Relational Database Service (Amazon RDS). Backup/restore is the simplest method but requires a much longer cutover window compared with the other options, due to the size of the backups and the time it would require to create, copy, and restore them on the target database. For more information about this approach, see [Native SQL Server backup/restore](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/native-backup-restore.html) and [Oracle RMAN](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/homogeneous-migration-tools.html#oracle-rman) on the AWS Prescriptive Guidance website.
+ ***Logical backup or export*** is another method that takes a copy of a full or partial logical database. This native database engine tool lets you decompose a large database server to migrate selected databases that are associated with a particular application. It provides more control than full backup/restore on what to migrate, and also supports Amazon RDS as a target. However, this option also requires a longer cutover window for the same reasons as the previous method.
+ ***Native database high availability (HA) tools*** include the Always On or distributed availability group clusters in Microsoft SQL Server and Oracle's Data Guard replications. This approach requires a major effort to set up across extended, cross-site HA clusters, and might cause some performance degradation because of the longer latency to achieve fully synchronous active-active deployments. However, this method provides the closest to near-zero downtime during the cutover.
+ ***Change data capture (CDC)*** replication is supported by [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/) and native database replication tools such as Oracle GoldenGate, Qlik, and Talend. You can use these tools to copy a partial or complete database with the advantage of near-zero downtime, because they keep the target database in sync with the source database. You can also use this method with [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) and AWS DMS for heterogeneous migrations, to migrate and modernize your database at the same time.
+ If network throughput is a bottleneck during your database migration, you can use AWS DMS in conjunction with [AWS Snowball](https://aws.amazon.com/snowball/) to migrate and modernize very large databases. For more information, see the blog post [Enable large-scale database migrations with AWS DMS and AWS Snowball Edge](https://aws.amazon.com/blogs/storage/enable-large-scale-database-migrations-with-aws-dms-and-aws-snowball/).

## Advantages
<a name="dms-advantages"></a>

Using database tools for migration has the following advantages over block-level replication methods:
+ Some tools provide migration with minimal downtime. These include AWS DMS and native tools that support native HA clusters or CDC replication.
+ You're able to use tools that are familiar to most DBAs to migrate your clustered databases.
+ You can modernize the database as part of the migration workflow, and move into managed database services such as Amazon RDS or Amazon Aurora.
+ You can take advantage of consolidation and decomposition (or partial database migrations), when moving from a monolithic infrastructure to microservices, splitting up a large database server or a cluster, or merging smaller databases into a larger instance or into an AWS service.

## Disadvantages
<a name="dms-disadvantages"></a>

Most of the benefits discussed in the previous section are outside a typical lift-and-shift migration scenario and fall under the replatform approach. Moreover, native database migration methods have some disadvantages in large-scale migrations, such as:
+ Preparation – You have to pre-provision and configure the target infrastructure, database servers, and clusters fully before you can use any of the native database methods.
+ Complexity – Some methods, such as full or logical backup/restore, have to be combined with another replication method to detect all the changes since the initial backup was created.
+ Scalability – There's no simple automation framework available to roll these methods out to other database clusters and servers when you migrate at scale.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
