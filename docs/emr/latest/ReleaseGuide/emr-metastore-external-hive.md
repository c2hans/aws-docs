---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-metastore-external-hive.html
---

# Configuring an external metastore for Hive
<a name="emr-metastore-external-hive"></a>

By default, Hive records metastore information in a MySQL database on the primary node's file system. The metastore contains a description of the table and the underlying data on which it is built, including the partition names, data types, and so on. When a cluster terminates, all cluster nodes shut down, including the primary node. When this happens, local data is lost because node file systems use ephemeral storage. If you need the metastore to persist, you must create an *external metastore* that exists outside the cluster.

You have two options for an external metastore:
+ AWS Glue Data Catalog (Amazon EMR release 5.8.0 or later only).

  For more information, see [Using the AWS Glue Data Catalog as the metastore for Hive](emr-hive-metastore-glue.md).
+ Amazon RDS or Amazon Aurora.

  For more information, see [Using an external MySQL database or Amazon Aurora](emr-hive-metastore-external.md).

**Note**
If you're using Hive 3 and encounter too many connections to Hive metastore, configure the parameter `datanucleus.connectionPool.maxPoolSize` to have a smaller value or increase the number of connection the database server can handle. The increased number of connections is due to the way Hive computes the maximum number of JDBC connections. To calculate the optimal value for performance, see [Hive Configuration Properties](https://cwiki.apache.org/confluence/display/Hive/Configuration+Properties#ConfigurationProperties-datanucleus.connectionPool.maxPoolSize.1).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
