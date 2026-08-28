---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/zeppelin-considerations.html
---

# Considerations when using Zeppelin on Amazon EMR
<a name="zeppelin-considerations"></a>
+ Connect to Zeppelin using the same [SSH tunneling method](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ssh-tunnel.html) to connect to other web servers on the master node. Zeppelin server is found at port 8890.
+ Zeppelin on Amazon EMR release versions 5.0.0 and later supports [Shiro authentication](https://zeppelin.apache.org/docs/0.8.0/setup/security/shiro_authentication.html).
+ Zeppelin on Amazon EMR release versions 5.8.0 and later supports using AWS Glue Data Catalog as the metastore for Spark SQL. For more information, see [Using AWS Glue Data Catalog as the metastore for Spark SQL.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-glue.html)
+ Zeppelin does not use some of the settings defined in your cluster's `spark-defaults.conf` configuration file, even though it instructs YARN to allocate executors dynamically if you have set `spark.dynamicAllocation.enabled` to `true`. You must set executor settings, such as memory and cores, using the Zeppelin **Interpreter** tab, and then restart the interpreter for them to be used.
+ Amazon EMR releases 6.10.0 and higher support Apache Zeppelin integration with Apache Flink. See [Working with Flink jobs from Zeppelin in Amazon EMR](flink-zeppelin.md) for more information.
+ Zeppelin on Amazon EMR does not support the SparkR interpreter.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
