---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-general.html
---

# General best practices
<a name="best-practices-general"></a>

Regardless of your use case, when you use Apache Iceberg on AWS, we recommend that you follow these general best practices.
+ **Use Iceberg format version 2.**

  Athena uses Iceberg format version 2 by default.

  When you use Spark on Amazon EMR or AWS Glue to create Iceberg tables, specify the format version as described in the [Iceberg documentation](https://iceberg.apache.org/docs/nightly/configuration/#reserved-table-properties).
+ **Use the AWS Glue Data Catalog as your data catalog.**

  Athena uses the AWS Glue Data Catalog by default.

  When you use Spark on Amazon EMR or AWS Glue to work with Iceberg, add the following configuration to your Spark session to use the AWS Glue Data Catalog. For more information, see the section [Spark configurations for Iceberg in AWS Glue](iceberg-glue.md#glue-spark-config) earlier in this guide.

  ```
  "spark.sql.catalog.<your_catalog_name>.type": "glue"
  ```
+ **Use the AWS Glue Data Catalog as lock manager.**

  Athena uses the AWS Glue Data Catalog as lock manager by default for Iceberg tables.

  When you use Spark on Amazon EMR or AWS Glue to work with Iceberg, make sure to configure your Spark session configuration to use the AWS Glue Data Catalog as lock manager. For more information, see [Optimistic Locking](https://iceberg.apache.org/docs/latest/aws/#optimistic-locking) in the Iceberg documentation.
+ **Use Zstandard (ZSTD) compression.**

  The default compression codec of Iceberg is gzip, which can be modified by using the table property `write.<file_type>.compression-codec`. Athena already uses ZSTD as the default compression codec for Iceberg tables.

  In general, we recommend using the ZSTD compression codec because it strikes a balance between GZIP and Snappy, and offers good read/write performance without compromising the compression ratio. Additionally, compression levels can be adjusted to suit your needs. For more information, see [ZSTD compression levels in Athena](https://docs.aws.amazon.com/athena/latest/ug/compression-support-zstd-levels.html) in the Athena documentation.

  Snappy might provide the best overall read and write performance but has a lower compression ratio than GZIP and ZSTD. If you prioritize performance—even if it means storing larger data volumes in Amazon S3—Snappy might be the optimal choice.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
