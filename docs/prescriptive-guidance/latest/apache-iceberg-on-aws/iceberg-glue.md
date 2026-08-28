---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-glue.html
---

# Working with Iceberg in AWS Glue
<a name="iceberg-glue"></a>

[AWS Glue](https://aws.amazon.com/glue/) is a serverless data integration service that makes it easier to discover, prepare, move, and integrate data from multiple sources for analytics, machine learning (ML), and application development. One of the core capabilities of AWS Glue is its ability to perform extract, transform, and load (ETL) operations in a simple and cost-effective manner. This helps categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams.

[AWS Glue jobs](https://docs.aws.amazon.com/glue/latest/dg/etl-jobs-section.html) encapsulate scripts that define transformation logic by using an [Apache Spark](https://spark.apache.org/) or Python runtime. AWS Glue jobs can be run in both batch and streaming mode.

When you create Iceberg jobs in AWS Glue, depending on the version of AWS Glue, you can use either native Iceberg integration or a custom Iceberg version to attach Iceberg dependencies to the job.

## Using native Iceberg integration
<a name="glue-native-integration"></a>

AWS Glue versions 3.0, 4.0, and 5.0 natively support transactional data lake formats such as Apache Iceberg, Apache Hudi, and Linux Foundation Delta Lake in AWS Glue for Spark. This integration feature simplifies the configuration steps required to start using these frameworks in AWS Glue.

To enable Iceberg support for your AWS Glue job, set the job: Choose the **Job details** tab for your AWS Glue job,  scroll to **Job parameters** under **Advanced properties**, and set the key to `--datalake-formats`  and its value to `iceberg`.

If you are authoring a job by using a notebook, you can configure the parameter in the first notebook cell by using the `%%configure` magic as follows:

```
%%configure
{
  "--conf" : <job-specific Spark configuration discussed later>,
  "--datalake-formats" : "iceberg"
}
```

The `iceberg `configuration for `--datalake-formats` in AWS Glue corresponds to specific Iceberg versions based on your AWS Glue version:

|
|
| AWS Glue version | Default Iceberg version |
| --- |--- |
| 5.0 | 1.7.1 |
| 4.0 | 1.0.0 |
| 3.0 | 0.13.1 |

## Using a custom Iceberg version
<a name="glue-custom-integration"></a>

In some situations, you might want to retain control over the Iceberg version for the job and upgrade it at your own pace. For example, upgrading to a later version can unlock access to new features and performance enhancements. To use a specific Iceberg version with AWS Glue, you can provide your own JAR files.

Before you implement a custom Iceberg version, verify compatibility with your AWS Glue environment by checking the [AWS Glue versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html) section of the AWS Glue documentation. For example, AWS Glue 5.0 requires compatibility with Spark 3.5.4.

As an example, to run AWS Glue jobs that use Iceberg version 1.9.1, follow these steps:

1. Acquire and upload the required JAR files to Amazon S3:

   1. Download [iceberg-spark-runtime-3.5\_2.12-1.9.1.jar](https://mvnrepository.com/artifact/org.apache.iceberg/iceberg-spark-runtime-3.5_2.12/1.9.1) and [iceberg-aws-bundle-1.9.1.jar](https://mvnrepository.com/artifact/org.apache.iceberg/iceberg-aws-bundle/1.9.1) from the Apache Maven repository.

   1. Upload these files to your designated S3 bucket location (for example, `s3://your-bucket-name/jars/`).

1. Set up the **Job parameters** for your AWS Glue job as follows:

   1. Specify the complete S3 path to both JAR files in the `--extra-jars` parameter, separating them with a comma (for example, `s3://your-bucket-name/jars/iceberg-spark-runtime-3.5_2.12-1.9.1.jar,s3://your-bucket-name/jars/iceberg-aws-bundle-1.9.1.jar`).

   1. Do not include `iceberg` as a value for the `--datalake-formats` parameter.

   1. If you use AWS Glue 5.0, you must set the `--user-jars-first` parameter to `true`.

## Spark configurations for Iceberg in AWS Glue
<a name="glue-spark-config"></a>

This section discusses the Spark configurations required to author an AWS Glue ETL job for an Iceberg dataset. You can set these configurations by using the `--conf` Spark key with a comma-separated list of all Spark configuration keys and values. You can use the `%%configure` magic in a notebook, or the **Job parameters** section of the AWS Glue Studio console.

```
%glue_version 5.0

%%configure
{
  "--conf" : "spark.sql.extensions=org.apache.iceberg.spark.extensions...",
  "--datalake-formats" : "iceberg"
}
```

Configure the Spark session with the following properties:
+ `<catalog_name>` is the name of your Iceberg Spark session catalog. Replace it with a name of your choice, and remember to change the references throughout all configurations that are associated with this catalog. In your code, you can refer to your Iceberg tables by using the fully qualified table name, including the Spark session catalog name, as follows:

  `<catalog_name>.<database_name>.<table_name>`

  Alternatively, you can change the default catalog to the Iceberg catalog that you defined by setting `spark.sql.defaultCatalog` to your catalog name. You can use this second approach to refer to tables without the catalog prefix, which can simplify your queries.
+ `<catalog_name>.<warehouse>` points to the Amazon S3 path where you want to store your data and metadata.
+ To make the catalog an AWS Glue Data Catalog, set `spark.sql.catalog.<catalog_name>.type`  to `glue`. This key is required to point to an implementation class for any custom catalog implementation. For catalogs supported by Iceberg, see the [General best practices](best-practices-general.md) section later in this guide.

For example, if you have a catalog called `glue_iceberg`, you can configure your job by using multiple `--conf` keys as follows:

```
%%configure
{
  "--datalake-formats" : "iceberg",
  "--conf" : "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.catalog.glue_iceberg=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.glue_iceberg.warehouse=s3://<your-warehouse-dir>/ --conf spark.sql.catalog.glue_iceberg.type=glue"
}
```

Alternatively, you can use code to add the above configurations to your Spark script as follows:

```
spark = SparkSession.builder\
                    .config("spark.sql.extensions","org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")\
                    .config("spark.sql.catalog.glue_iceberg", "org.apache.iceberg.spark.SparkCatalog")\
                    .config("spark.sql.catalog.glue_iceberg.warehouse","s3://<your-warehouse-dir>/")\
                    .config("spark.sql.catalog.glue_iceberg.type", "glue") \
                    .getOrCreate()
```

## Best practices for AWS Glue jobs
<a name="glue-best-practices"></a>

This section provides general guidelines for tuning Spark jobs in AWS Glue to optimize reading and writing data to Iceberg tables. For Iceberg-specific best practices, see the [Best practices](best-practices.md) section later in this guide.
+ **Use the latest version of AWS Glue and upgrade whenever possible** – New versions of AWS Glue provide performance improvements, reduced startup times, and new features. They also support newer Spark versions that might be required for the latest Iceberg versions. For a list of available AWS Glue versions and the Spark versions they support, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html).
+ **Optimize AWS Glue job memory** – Follow the recommendations in the AWS blog post [Optimize memory management in AWS Glue](https://aws.amazon.com/blogs/big-data/optimize-memory-management-in-aws-glue/).
+ **Use AWS Glue Auto Scaling** – When you enable Auto Scaling, AWS Glue automatically adjusts the number of AWS Glue workers dynamically based on your workload. This helps reduce the cost of your AWS Glue job during peak loads, because AWS Glue scales down the number of workers when the workload is small and workers are sitting idle. To use AWS Glue Auto Scaling, you specify a maximum number of workers that your AWS Glue job can scale to. For more information, see [Using auto scaling for ](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html)AWS Glue in the AWS Glue documentation.
+ **Use the desired Iceberg version **– AWS Glue native integration for Iceberg is best for getting started with Iceberg. However, for production workloads, we recommend that you add library dependencies (as discussed [earlier in this guide](#glue-custom-integration)) to get full control over the Iceberg version. This approach helps you benefit from the latest Iceberg features and performance improvements in your AWS Glue jobs.
+ **Enable the Spark UI for monitoring and debugging** – You can also use the [Spark UI in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html) to inspect your Iceberg job by visualizing the different stages of a Spark job in a directed acyclic graph (DAG) and monitoring the jobs in detail. Spark UI provides an effective way to both troubleshoot and optimize Iceberg jobs. For example, you can identify bottleneck stages that have large shuffles or disk spill to identify tuning opportunities. For more information, see [Monitoring jobs using the Apache Spark web UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html) in the AWS Glue documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
