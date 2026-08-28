---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/external-metastore-considerations.html
---

# Considerations when using an external metastore
<a name="external-metastore-considerations"></a>
+ You can configure databases that are compatible with MariaDB JDBC as your metastore. Examples of these databases are RDS for MariaDB, MySQL, and Amazon Aurora.
+ Metastores aren't auto-initialized. If your metastore isn't initialized with a schema for your Hive version, use the [Hive Schema Tool](https://cwiki.apache.org/confluence/display/Hive/Hive+Schema+Tool).
+ EMR Serverless doesn't support Kerberos authentication. You can't use a thrift metastore server with Kerberos authentication with EMR Serverless Spark or Hive jobs.
+ You must configure VPC access to use the multi-catalog hierarchy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
