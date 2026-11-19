---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-glue.html
---

# Working with Iceberg in AWS Glue

[AWS Glue](https://aws.amazon.com/glue/) is a serverless data integration service that makes it easier to discover, prepare, move, and integrate data from multiple sources for analytics, machine learning (ML), and application development. One of the core capabilities of AWS Glue is its ability to perform extract, transform, and load (ETL) operations in a simple and cost-effective manner. This helps categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams.

[AWS Glue jobs](https://docs.aws.amazon.com/glue/latest/dg/etl-jobs-section.html) encapsulate scripts that define transformation logic by using an [Apache Spark](https://spark.apache.org/) or Python runtime. AWS Glue jobs can be run in both batch and streaming mode. From AWS Glue Spark jobs you can read from and write to Apache Iceberg tables that are either **self-managed on Amazon S3** or **hosted in Amazon S3 Tables** — the transformation code is the same, only the Spark session catalog configuration differs.

This section covers Iceberg format-version support, how AWS Glue attaches Iceberg dependencies (native integration or a custom Iceberg version), catalog configuration for both storage options, three ways to apply the Spark configuration (AWS Glue notebook, inline PySpark, `aws glue create-job` CLI), and a pointer to the shared Spark code examples.

## S3 Tables support in AWS Glue
<a name="s3-tables-support-in-aws-glue"></a>

Amazon S3 Tables is supported on **AWS Glue version 5.0 or higher**. Earlier AWS Glue versions can still read from and write to self-managed Iceberg tables on Amazon S3, but they cannot use the S3 Tables Spark catalog configuration described in [Amazon S3 Tables](#glue-amazon-s3-tables) below.

## Iceberg format version support in AWS Glue
<a name="iceberg-format-version-support-in-aws-glue"></a>

AWS Glue 3.0\+ supports Iceberg format version 2 through native integration. Iceberg format version 3 requires AWS Glue **5.1\+**.

|
|
| **AWS Glue version** | **Iceberg Format version** | **Iceberg library version** |
| --- |--- |--- |
| 3.0 | V2 | 0.13.1 |
| 4.0 | V2 | 1.0.0 |
| 5.0 | V2 | 1.7.1 |
| 5.1 | V2, V3 | 1.10.0 |
| 6.0 | V2, V3 | 1.11.0 |

When you create an Iceberg table with Spark on AWS Glue without setting the `format-version` table property, Spark applies the [Iceberg default of V2](https://iceberg.apache.org/docs/latest/configuration/#table-behavior-properties). Add `TBLPROPERTIES ('format-version'='3')` on `CREATE TABLE` (or `ALTER TABLE ... SET TBLPROPERTIES ('format-version'='3')` on an existing table) to opt into V3.

### V3 feature support in AWS Glue
<a name="v3-feature-support-in-aws-glue"></a>

Iceberg V3 introduces several new capabilities on top of V2. The following table shows per-feature availability on AWS Glue against V3 tables.

|
|
| **V3 feature** | **Supported** |
| --- |--- |
| Row lineage | Yes (AWS Glue 5.1\+) |
| Deletion vectors | Yes (AWS Glue 5.1\+) |
| Default column values | Yes (AWS Glue 6.0\+) |
| Nanosecond timestamps (`timestamp_ns`, `timestamptz_ns`) | Yes (AWS Glue 6.0\+) |
| Geography type | Yes (AWS Glue 6.0\+) |
| Geometry type | Yes (AWS Glue 6.0\+) |
| Variant type (without shredding) | Yes (AWS Glue 6.0\+) |
| Variant type (with shredding) | Yes (AWS Glue 6.0\+) |

Refer the [known limitations](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-60.html#migrating-version-60-known-limitations) section in Glue for a set of known limitations

## Using native Iceberg integration
<a name="using-native-iceberg-integration"></a>

AWS Glue versions 3.0, 4.0, 5.0, 5.1, and 6.0 natively support transactional data lake formats such as Apache Iceberg, Apache Hudi, and Linux Foundation Delta Lake in AWS Glue for Spark. This integration feature simplifies the configuration steps required to start using these frameworks in AWS Glue.

To enable Iceberg support for your AWS Glue job, set the job: Choose the **Job details** tab for your AWS Glue job, scroll to **Job parameters** under **Advanced properties**, and set the key to `--datalake-formats` and its value to `iceberg`. Additionally for using Geospatial Datatypes with AWS Glue 6.0\+, set this additional property `spark.sql.geospatial.enabled=true` in `--conf`.

If you are authoring a job by using an AWS Glue notebook, configure the AWS Glue version and job parameters in the first notebook cell by using the `%%configure` magic as follows:

```
%%configure
{
  "--conf" : <job-specific Spark configuration discussed later>,
  "--datalake-formats" : "iceberg",
  "glue_version" : "6.0"
}
```

## Using a custom Iceberg version
<a name="using-a-custom-iceberg-version"></a>

In some situations, you might want to retain control over the Iceberg version for the job and upgrade it at your own pace. For example, upgrading to a later version can unlock access to new features and performance enhancements. To use a specific Iceberg version with AWS Glue, you can provide your own JAR files.

Before you implement a custom Iceberg version, verify compatibility with your AWS Glue environment by checking the [AWS Glue versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html) section of the AWS Glue documentation. For example, AWS Glue 5.0 requires compatibility with Spark 3.5.4.

As an example, to run AWS Glue jobs that use Iceberg version 1.9.1, follow these steps:

1. Acquire and upload the required JAR files to Amazon S3:

   1. Download [iceberg-spark-runtime-3.5\_2.12-1.9.1.jar](https://mvnrepository.com/artifact/org.apache.iceberg/iceberg-spark-runtime-3.5_2.12/1.9.1) and [iceberg-aws-bundle-1.9.1.jar](https://mvnrepository.com/artifact/org.apache.iceberg/iceberg-aws-bundle/1.9.1) from the Apache Maven repository.

   1. Upload these files to your designated S3 bucket location (for example, `s3://<bucket-name>/jars/`).

1. Set up the **Job parameters** for your AWS Glue job as follows:

   1. Specify the complete S3 path to both JAR files in the `--extra-jars` parameter, separating them with a comma (for example, `s3://<bucket-name>/jars/iceberg-spark-runtime-3.5_2.12-1.9.1.jar,s3://<bucket-name>/jars/iceberg-aws-bundle-1.9.1.jar`).

   1. Do not include `iceberg` as a value for the `--datalake-formats` parameter.

   1. If you use AWS Glue 5.0\+, you must set the `--user-jars-first` parameter to `true`.

## Catalog configuration for Iceberg on AWS Glue Spark
<a name="catalog-configuration-for-iceberg-on-aws-glue-spark"></a>

The Iceberg SQL and DataFrame API surface is identical across the two hosting options. Only the Spark session catalog configuration differs.

### Self-managed Iceberg on S3
<a name="glue-self-managed-iceberg-on-s3"></a>

For self managed Iceberg tables on Amazon S3 general purpose buckets, you have two catalog options:

**Option A — Pure Iceberg catalog (**`SparkCatalog`**).** Use this when the job works exclusively with Iceberg tables. Register the catalog under any name you choose (for example, `glue_iceberg`) - Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location (default location where databases and tables are created if not explicitly specified):

```
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.catalog.glue_iceberg=org.apache.iceberg.spark.SparkCatalog
spark.sql.catalog.glue_iceberg.type=glue
spark.sql.catalog.glue_iceberg.warehouse=s3://<bucket-name>/<warehouse-dir>/
```

Reference tables as `glue_iceberg.<database>.<table>` (or set `spark.sql.defaultCatalog=glue_iceberg` to omit the prefix).

**Option B — Mixed Hive \+ Iceberg session (**`SparkSessionCatalog`**).** Use this when the job needs to access both Hive tables and Iceberg tables through the built-in Spark session catalog (`spark_catalog`). This is the recommended setup for migration scenarios where some tables have been converted to Iceberg and others remain as Hive. Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location (default location where databases and tables are created if not explicitly specified):

```
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog
spark.sql.catalog.spark_catalog.type=glue
spark.sql.catalog.spark_catalog.warehouse=s3://<bucket-name>/<warehouse-dir>/
```

With this option, tables are referenced as `<database>.<table>` (no catalog prefix) and Spark automatically routes Iceberg tables to Iceberg and Hive tables to Hive.

### Amazon S3 Tables
<a name="glue-amazon-s3-tables"></a>

For tables hosted in Amazon S3 Tables, access them from Spark on AWS Glue through the AWS Glue Data Catalog. This subsection assumes AWS Glue 5.0\+. Prerequisite: enable the [S3 Tables integration with AWS analytics services](getting-started-with-amazon-s3-tables.md) on your account, which registers each table bucket in Glue as `s3tablescatalog/<table-bucket-name>`. Then register a Spark catalog that points at the Glue federated catalog. Replace `<table-bucket-name>` with your own table bucket name and `<AWS_ACCOUNT_ID>` with your AWS Account ID:

```
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.catalog.s3_tables_catalog=org.apache.iceberg.spark.SparkCatalog
spark.sql.catalog.s3_tables_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog
spark.sql.catalog.s3_tables_catalog.glue.id=<AWS_ACCOUNT_ID>:s3tablescatalog/<table-bucket-name>
spark.sql.catalog.s3_tables_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO
```

Reference tables as `s3_tables_catalog.<namespace>.<table>`.

**Combining self-managed and S3 Tables in one session.** You can register both catalogs at once (for example `iceberg_catalog` or `spark_catalog` for self-managed and `s3_tables_catalog` for S3 Tables) and reference each table by its qualified catalog name in the same SQL query.

## Spark configurations for Iceberg in AWS Glue
<a name="spark-configurations-for-iceberg-in-aws-glue"></a>

The catalog configuration from the previous section can be applied in three ways: interactively from an AWS Glue notebook, inline from your PySpark code, or through the `aws glue create-job` CLI when you register a job for production. All three routes share the same Spark keys — only the wrapper differs.

### AWS Glue notebook (%%configure magic)
<a name="aws-glue-notebook-object-object-magic"></a>

Set the AWS Glue version (`glue_version`), enable the native Iceberg integration (`--datalake-formats`), and pass the catalog config as a space-separated list of `--conf key=value` pairs on the `--conf` job argument. The following example registers a self-managed Iceberg catalog called `glue_iceberg`. Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location:

```
%%configure
{
  "glue_version" : "6.0",
  "--datalake-formats" : "iceberg",
  "--conf" : "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.catalog.glue_iceberg=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.glue_iceberg.warehouse=s3://<bucket-name>/<warehouse-dir>/ --conf spark.sql.catalog.glue_iceberg.type=glue"
}
```

You can register both catalogs at once (for example, `glue_iceberg` or `spark_catalog` for self-managed Iceberg and `s3_tables_catalog` for S3 Tables) by including both sets of `spark.sql.catalog.<name>.*` entries — add the S3 Tables catalog properties from [Amazon S3 Tables catalog configuration](#glue-amazon-s3-tables). Then reference each table by its qualified catalog name in the same SQL query.

### Inline code properties (SparkSession.builder)
<a name="inline-code-properties-object-object"></a>

If you prefer to configure the session from your PySpark script (typical for scripts developed outside a notebook and later packaged into an AWS Glue job), use `SparkSession.builder.config(...)` — the keys are the same as the notebook `--conf` values above. Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location

```
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.glue_iceberg", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.glue_iceberg.warehouse", "s3://<bucket-name>/<warehouse-dir>/")
    .config("spark.sql.catalog.glue_iceberg.type", "glue")
    .getOrCreate()
)
```

**Note**
`SparkSession.builder.config(...)` only sets Spark runtime properties — it does **not** bring the Iceberg JARs into the classpath or select the AWS Glue runtime. The AWS Glue job that runs this script must still be configured with `"--datalake-formats": "iceberg"` (as a job parameter, which enables the [native Iceberg integration](#using-native-iceberg-integration) and adds the JARs) and the desired AWS Glue version (for example, `6.0` for the V3-capable runtime). See the [AWS Glue job (AWS CLI)](#aws-glue-job-aws-cli) example below.

You can register both catalogs at once (for example, `glue_iceberg` or `spark_catalog` for self-managed Iceberg and `s3_tables_catalog` for S3 Tables) by chaining additional `.config("spark.sql.catalog.<name>.*", "...")` calls — add the S3 Tables catalog properties from [Amazon S3 Tables catalog configuration](#glue-amazon-s3-tables). Then reference each table by its qualified catalog name in the same SQL query.

### AWS Glue job (AWS CLI)
<a name="aws-glue-job-aws-cli"></a>

When you register an AWS Glue job with the CLI, set the runtime version through the top-level `--glue-version` parameter and pass Iceberg-related job arguments in `--default-arguments` (the JSON payload uses the same Spark keys as the notebook example above). Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location, replace `<bucket-name>` with your own bucket name:

```
aws glue create-job \
  --name my-iceberg-job \
  --role AWSGlueServiceRole-MyRole \
  --command 'Name=glueetl,PythonVersion=3,ScriptLocation=s3://<bucket-name>/my_iceberg_job.py' \
  --glue-version 6.0 \
  --default-arguments '{
    "--datalake-formats": "iceberg",
    "--conf": "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.catalog.glue_iceberg=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.glue_iceberg.warehouse=s3://<bucket-name>/<warehouse-dir>/ --conf spark.sql.catalog.glue_iceberg.type=glue"
  }'
```

You can register both catalogs at once (for example, `glue_iceberg` or `spark_catalog` for self-managed Iceberg and `s3_tables_catalog` for S3 Tables) by including both sets of `spark.sql.catalog.<name>.*` entries in the `--conf` string — add the S3 Tables catalog properties from [Amazon S3 Tables catalog configuration](#glue-amazon-s3-tables). Then reference each table by its qualified catalog name in the same SQL query.

Notes:
+ The same job arguments can also be set through the AWS Glue Studio console under **Job details → Advanced properties → Job parameters**.

## Spark code examples
<a name="spark-code-examples"></a>

Once your AWS Glue job or notebook is configured and the Spark catalogs described above are registered, the day-to-day SQL and DataFrame code is engine-agnostic. For end-to-end examples — `CREATE TABLE`, `INSERT`, `UPDATE`, `MERGE INTO`, `DELETE`, reads, time travel, incremental queries, and metadata tables — see [Working with Iceberg tables by using Apache Spark](iceberg-spark.md).
