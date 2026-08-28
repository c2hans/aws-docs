---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-committer-enable.html
---

# Enable the EMRFS S3-optimized committer for Amazon EMR 5.19.0
<a name="emr-spark-committer-enable"></a>

If you are using Amazon EMR 5.19.0 , you can manually set the `spark.sql.parquet.fs.optimized.committer.optimization-enabled` property to `true` when you create a cluster or from within Spark if you are using Amazon EMR .

## Enabling the EMRFS S3-optimized committer when creating a cluster
<a name="w2aac62c61c17c13b5"></a>

Use the `spark-defaults` configuration classification to set the `spark.sql.parquet.fs.optimized.committer.optimization-enabled` property to `true`. For more information, see [Configure applications](emr-configure-apps.md).

## Enabling the EMRFS S3-optimized committer from Spark
<a name="w2aac62c61c17c13b7"></a>

You can set `spark.sql.parquet.fs.optimized.committer.optimization-enabled` to `true` by hard-coding it in a `SparkConf`, passing it as a `--conf` parameter in the Spark shell or `spark-submit` and `spark-sql` tools, or in `conf/spark-defaults.conf`. For more information, see [Spark configuration](https://spark.apache.org/docs/latest/configuration.html) in Apache Spark documentation.

The following example shows how to enable the committer while running a spark-sql command.

```
spark-sql \
  --conf spark.sql.parquet.fs.optimized.committer.optimization-enabled=true \
  -e "INSERT OVERWRITE TABLE target_table SELECT * FROM source_table;"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
