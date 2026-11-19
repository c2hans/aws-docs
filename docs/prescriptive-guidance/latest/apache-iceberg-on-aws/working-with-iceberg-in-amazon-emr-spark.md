---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/working-with-iceberg-in-amazon-emr-spark.html
---

# Working with Iceberg in Amazon EMR (Spark)

Amazon EMR provides petabyte-scale data processing, interactive analytics, and machine learning in the cloud through open-source frameworks such as Apache Spark, Apache Hive, Apache Flink, and Trino. This section focuses on **Spark on Amazon EMR** — for Trino on Amazon EMR, see [Working with Iceberg tables by using Trino on Amazon EMR](working-with-iceberg-tables-by-using-trino-amazon-emr.md).

You can use Spark on Amazon EMR to read from and write to Apache Iceberg tables that are either **self-managed on Amazon S3** or **hosted in Amazon S3 Tables**. The Spark SQL and DataFrame code is the same in both cases — only the Spark session catalog configuration differs. This section covers Iceberg format-version support, cluster and catalog setup for both storage options, deployment options (Amazon EMR on EC2, Amazon EMR on EKS, Amazon EMR Serverless, and Amazon EMR on AWS Outposts — see the [Amazon EMR FAQ](https://aws.amazon.com/emr/faqs/) to choose one), and a pointer to the shared Spark code examples.

## S3 Tables support in Amazon EMR
<a name="s3-tables-support-in-amazon-emr"></a>

Amazon S3 Tables is supported on **Amazon EMR version 7.5 or higher**. Earlier Amazon EMR releases can still read from and write to self-managed Iceberg tables on Amazon S3, but they cannot use the S3 Tables Spark catalog configuration described in [Amazon S3 Tables](#emr-amazon-s3-tables) below.

## Iceberg format version support in Amazon EMR
<a name="iceberg-format-version-support-in-amazon-emr"></a>

Amazon EMR 6.5.0\+ (Iceberg 0.12.0) supports Iceberg format version 2. Iceberg format version 3 requires Amazon EMR 7.12.0\+ (Iceberg 1.10.0) for core V3 features (deletion vectors and row lineage). Amazon EMR 8.1.0\+ (Iceberg 1.11.0) for the complete set of V3 features including `variant` with shredding. For the full Amazon EMR → Iceberg version mapping, see [Iceberg release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Iceberg-release-history.html) in the Amazon EMR documentation.

|
|
| **Format version** | **Supported** |
| --- |--- |
| Version 2 (V2) | Yes (Amazon EMR 6.5.0\+ with Iceberg 0.12.0\+) |
| Version 3 (V3) | Yes (Core V3 features in EMR 7.12, full V3 features support on Amazon EMR 8.1.0\+) - see detailed table below |

When you create an Iceberg table with Spark on Amazon EMR without setting the `format-version` table property, Iceberg uses its default table format version. Since **Apache Iceberg 1.4.0**, that default is [V2](https://iceberg.apache.org/docs/latest/configuration/#table-behavior-properties). Add `TBLPROPERTIES ('format-version'='3')` on `CREATE TABLE` (or `ALTER TABLE ... SET TBLPROPERTIES ('format-version'='3')` on an existing table) to opt into V3.

### V3 feature support in Amazon EMR (Spark)
<a name="v3-feature-support-in-amazon-emr-spark"></a>

Iceberg V3 introduces several new capabilities on top of V2. The following table shows per-feature availability on Amazon EMR Spark against V3 tables.

|
|
| **V3 feature** | **Supported** |
| --- |--- |
| Row lineage | Yes (EMR 7.12.0\+) |
| Deletion vectors | Yes (EMR 7.12.0\+) |
| Default column values | Yes (EMR 8.1.0\+) |
| Nanosecond timestamps (`timestamp_ns`, `timestamptz_ns`) | Yes (EMR 8.1.0\+) |
| Geography type | Yes (EMR 8.1.0\+) |
| Geometry type | Yes (EMR 8.1.0\+) |
| Variant type (without shredding) | Yes (EMR 8.0.0\+) |
| Variant type (with shredding) | Yes (EMR 8.1.0\+) |

## Version and feature compatibility
<a name="version-and-feature-compatibility"></a>

Amazon EMR version 6.5.0 and later versions support Apache Iceberg natively. For a list of supported Iceberg versions for each Amazon EMR release, see [Iceberg release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Iceberg-release-history.html) in the Amazon EMR documentation. Also review the sections under [Use a cluster with Iceberg](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html) to see which Iceberg features are supported in Amazon EMR on different frameworks.

We recommend that you use the latest Amazon EMR version to benefit from the latest supported Iceberg version. The self-managed code examples in this section assume that you're using Amazon EMR release 7.12\+ (V2). For V3 workloads to have full V3 capabilities, use Amazon EMR **8.1.0\+** .

## Creating an Amazon EMR cluster with Iceberg
<a name="creating-an-amazon-emr-cluster-with-iceberg"></a>

To create an Amazon EMR cluster on Amazon EC2 with Iceberg installed, follow the instructions in the [Amazon EMR documentation](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html).

Specifically, your cluster should be configured with the following classification:

```
[{
    "Classification": "iceberg-defaults",
    "Properties": {
        "iceberg.enabled": "true"
    }
}]
```

You can also choose to use Amazon EMR Serverless or Amazon EMR on EKS as deployment options for your Iceberg workloads, starting from Amazon EMR 6.6.0.

To use S3 Tables from an Amazon EMR cluster you don't need any additional cluster-level classification beyond `iceberg-defaults`. The S3 Tables access is configured at the Spark session level (see the next section). If you plan to use S3 Tables through the AWS Glue Data Catalog integration, make sure the integration is enabled for the table buckets you want to query — see [Integrating Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html).

## Catalog configuration for Iceberg on Amazon EMR Spark
<a name="catalog-configuration-for-iceberg-on-amazon-emr-spark"></a>

Iceberg is accessed in Spark through a **catalog** that is registered as a `spark.sql.catalog.<name>` entry. The rest of the code you write (`CREATE TABLE`, `INSERT`, `MERGE`, `SELECT`, and so on) is identical across the two storage options — only the catalog configuration changes.

### Self-managed Iceberg on S3
<a name="emr-self-managed-iceberg-on-s3"></a>

For Iceberg tables that you manage yourself on Amazon S3 and register in the AWS Glue Data Catalog, there are two common ways to integrate the Iceberg catalog with Spark.

**Option A — Pure Iceberg catalog (**`SparkCatalog`**).** Use this when the session works exclusively with Iceberg tables. Register the catalog under any name you choose (for example, `iceberg_catalog`). Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location (default location where databases and tables are created if not explicitly specified):

```
spark.sql.catalog.iceberg_catalog=org.apache.iceberg.spark.SparkCatalog
spark.sql.catalog.iceberg_catalog.type=glue
spark.sql.catalog.iceberg_catalog.warehouse=s3://<bucket-name>/<warehouse-dir>/
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
```

Reference tables as `iceberg_catalog.<database>.<table>` (or set `spark.sql.defaultCatalog=iceberg_catalog` to omit the prefix).

**Option B — Mixed Hive \+ Iceberg session (**`SparkSessionCatalog`**).** Use this when the session needs to access both Hive tables and Iceberg tables through the built-in Spark session catalog (`spark_catalog`). This is the recommended setup for migration scenarios where some tables have been converted to Iceberg and others remain as Hive. Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location (default location where databases and tables are created if not explicitly specified):

```
spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog
spark.sql.catalog.spark_catalog.type=glue
spark.sql.catalog.spark_catalog.warehouse=s3://<bucket-name>/<warehouse-dir>/
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.hadoop.hive.metastore.client.factory.class=com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory
```

With this option, tables are referenced as `<database>.<table>` (no catalog prefix) and Spark automatically routes Iceberg tables to Iceberg and Hive tables to Hive.

### Amazon S3 Tables
<a name="emr-amazon-s3-tables"></a>

For tables hosted in Amazon S3 Tables, access them from Spark on Amazon EMR through the AWS Glue Data Catalog. This subsection assumes Amazon EMR 7.5\+. Prerequisite: enable the [S3 Tables integration with AWS analytics services](getting-started-with-amazon-s3-tables.md) on your account, which registers each table bucket in Glue as `s3tablescatalog/<table-bucket-name>`. Then register a Spark catalog that points at that Glue federated catalog. Replace `<table-bucket-name>` with your own table bucket name and `<AWS_ACCOUNT_ID>` with your AWS Account ID:

```
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.defaultCatalog=s3_tables_catalog
spark.sql.catalog.s3_tables_catalog=org.apache.iceberg.spark.SparkCatalog
spark.sql.catalog.s3_tables_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog
spark.sql.catalog.s3_tables_catalog.glue.id=<AWS_ACCOUNT_ID>:s3tablescatalog/<table-bucket-name>
```

Reference tables as `s3_tables_catalog.<namespace>.<table>`.

**Combining self-managed and S3 Tables in one session.** You can register both catalogs at once (for example `iceberg_catalog` or `spark_catalog` for self-managed and `s3_tables_catalog` for S3 Tables) and reference each table by its qualified catalog name in the same SQL query.

## Developing Iceberg applications in Amazon EMR
<a name="developing-iceberg-applications-in-amazon-emr"></a>

To develop the Spark code for your Iceberg applications, you can use [Amazon EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html), which is a web-based integrated development environment (IDE) for fully managed Jupyter notebooks that run on Amazon EMR clusters.

### Using Amazon EMR Studio notebooks
<a name="using-amazon-emr-studio-notebooks"></a>

You can interactively develop Spark applications in Amazon EMR Studio Workspace notebooks and connect those notebooks to your Amazon EMR on EC2 clusters or Amazon EMR on EKS managed endpoints. See AWS service documentation for instructions on setting up an EMR Studio for [Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-set-up.html) and [Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-eks-cluster.html).

To use Iceberg in EMR Studio, follow these steps:

1. Launch an Amazon EMR cluster with Iceberg enabled, as instructed in [Use a cluster with Iceberg Installed](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html).

1. Set up an EMR Studio. For instructions, see [Set up an Amazon EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-set-up.html).

1. Open an EMR Studio Workspace notebook and run the following code as the first cell in the notebook to configure your Spark session for using Iceberg.

   **For self-managed Iceberg on S3 - **Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location:

   ```
   %%configure -f
   {
       "conf": {
           "spark.sql.catalog.iceberg_catalog": "org.apache.iceberg.spark.SparkCatalog",
           "spark.sql.catalog.iceberg_catalog.warehouse": "s3://<bucket-name>/<warehouse-dir>/",
           "spark.sql.catalog.iceberg_catalog.type": "glue",
           "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
       }
   }
   ```

   **For Amazon S3 Tables (through the AWS Glue Data Catalog integration) - **Replace `<table-bucket-name>` with your own table bucket name and `<AWS_ACCOUNT_ID>` with your AWS Account ID:

   ```
   %%configure -f
   {
       "conf": {
           "spark.sql.catalog.s3_tables_catalog": "org.apache.iceberg.spark.SparkCatalog",
           "spark.sql.catalog.s3_tables_catalog.catalog-impl": "org.apache.iceberg.aws.glue.GlueCatalog",
           "spark.sql.catalog.s3_tables_catalog.glue.id": "<AWS_ACCOUNT_ID>:s3tablescatalog/<table-bucket-name>",
           "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
           "spark.sql.defaultCatalog": "s3_tables_catalog"
       }
   }
   ```

   In both cases:
   + The catalog name (`iceberg_catalog` or `s3_tables_catalog` in these examples) is arbitrary. Choose whatever makes sense for your project and reference tables with the fully qualified name `<catalog_name>.<database_or_namespace>.<table_name>`. Alternatively, set `spark.sql.defaultCatalog` to omit the catalog prefix from queries.
   + For self-managed Iceberg, `warehouse` is the Amazon S3 location where data and metadata are stored. For S3 Tables through Glue, the warehouse is implicit in `glue.id`.
   + For mixed Hive\+Iceberg sessions on self-managed tables, use `SparkSessionCatalog` on the `spark_catalog` name instead — see [Self-managed Iceberg on S3](#emr-self-managed-iceberg-on-s3) above.

1. You can now start interactively developing your Spark application for Iceberg in the notebook, as you would for any other Spark application.

For more information about configuring Spark for Apache Iceberg by using Amazon EMR Studio, see the blog post [Build a high-performance, ACID compliant, evolving data lake using Apache Iceberg on Amazon EMR](https://aws.amazon.com/blogs/big-data/build-a-high-performance-acid-compliant-evolving-data-lake-using-apache-iceberg-on-amazon-emr/).

### Running Iceberg jobs in Amazon EMR
<a name="running-iceberg-jobs-in-amazon-emr"></a>

After you develop the Spark application code for your Iceberg workload, you can run it on any Amazon EMR deployment option that supports Iceberg (see the [Amazon EMR FAQ](https://aws.amazon.com/emr/faqs/#Deployment_options)).

As with other Spark jobs, you can submit work to an Amazon EMR on EC2 cluster by adding steps or by interactively submitting Spark jobs to the primary node. To run a Spark job, see the following Amazon EMR documentation pages:
+ For an overview of the different options for submitting work to an Amazon EMR on EC2 cluster and detailed instructions for each option, see [Submit work to a cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-work-with-steps.html).
+ For Amazon EMR on EKS, see [Running Spark jobs with StartJobRun](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs.html).
+ For EMR Serverless, see [Running jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs.html).

The following sections provide an example for each Amazon EMR deployment option. Each example is shown with the self-managed Iceberg on S3 configuration; substitute the S3 Tables configuration from [Catalog configuration for Iceberg on Amazon EMR Spark](#catalog-configuration-for-iceberg-on-amazon-emr-spark) when your target is a table bucket.

#### Amazon EMR on EC2
<a name="amazon-emr-on-ec2"></a>

You can use these steps to submit the Iceberg Spark job:

1. Create the file `emr_step_iceberg.json` with the following content on your workstation **- **Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location, replace `<bucket-name>` with your own bucket name:

   ```
   [{
       "Name": "iceberg-test-job",
       "Type": "spark",
       "ActionOnFailure": "CONTINUE",
       "Args": [
           "--deploy-mode",
           "client",
           "--conf",
           "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
           "--conf",
           "spark.sql.catalog.iceberg_catalog=org.apache.iceberg.spark.SparkCatalog",
           "--conf",
           "spark.sql.catalog.iceberg_catalog.type=glue",
           "--conf",
           "spark.sql.catalog.iceberg_catalog.warehouse=s3://<bucket-name>/<warehouse-dir>/",
           "s3://<bucket-name>/code/iceberg-job.py"
       ]
   }]
   ```

   You can register both catalogs at once (for example, `iceberg_catalog` or `spark_catalog` for self-managed Iceberg and `s3_tables_catalog` for S3 Tables) by including both sets of `spark.sql.catalog.<name>.*` entries — add the S3 Tables catalog properties from [Amazon S3 Tables catalog configuration](#emr-amazon-s3-tables). Then reference each table by its qualified catalog name in the same SQL query.

1. Modify the configuration file for your specific Spark job by customizing the Iceberg configuration options that are highlighted in bold.

1. Submit the step by using the AWS Command Line Interface (AWS CLI). Run the command in the directory where the `emr_step_iceberg.json` file is located.

   ```
   aws emr add-steps --cluster-id <cluster_id> --steps file://emr_step_iceberg.json
   ```

#### Amazon EMR Serverless
<a name="amazon-emr-serverless"></a>

To submit an Iceberg Spark job to EMR Serverless by using the AWS CLI:

1. Create the file `emr_serverless_iceberg.json` with the following content on your workstation **- **Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location, replace `<bucket-name>` with your own bucket name:

   ```
   {
       "applicationId": "<APPLICATION_ID>",
       "executionRoleArn": "<ROLE_ARN>",
       "name": "iceberg-test-job",
       "jobDriver": {
           "sparkSubmit": {
               "entryPoint": "s3://<bucket-name>/code/iceberg-job.py",
               "entryPointArguments": []
           }
       },
       "configurationOverrides": {
           "applicationConfiguration": [{
               "classification": "spark-defaults",
               "properties": {
                   "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
                   "spark.sql.catalog.iceberg_catalog": "org.apache.iceberg.spark.SparkCatalog",
                   "spark.sql.catalog.iceberg_catalog.type": "glue",
                   "spark.sql.catalog.iceberg_catalog.warehouse": "s3://<bucket-name>/<warehouse-dir>/",
                   "spark.jars":"/usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar"
               }
           }],
           "monitoringConfiguration": {
               "s3MonitoringConfiguration": {
                   "logUri": "s3://<bucket-name>/emr-serverless/logs/"
               }
           }
       }
   }
   ```

**NOTE** You can register both catalogs at once (for example, `iceberg_catalog` or `spark_catalog` for self-managed Iceberg and `s3_tables_catalog` for S3 Tables) by including both sets of `spark.sql.catalog.<name>.*` entries — add the S3 Tables catalog properties from [Amazon S3 Tables catalog configuration](#emr-amazon-s3-tables). Then reference each table by its qualified catalog name in the same SQL query.

**NOTE** When using Amazon EMR release 8.x, specify `/usr/share/aws/iceberg/lib/iceberg-spark4-runtime.jar` for the `spark.jars` configuration.

1. Modify the configuration file for your specific Spark job by customizing the Iceberg configuration options that are highlighted in bold.

1. Submit the job by using the AWS CLI. Run the command in the directory where the `emr_serverless_iceberg.json` file is located:

   ```
   aws emr-serverless start-job-run --cli-input-json file://emr_serverless_iceberg.json
   ```

To submit an Iceberg Spark job to EMR Serverless by using the EMR Studio console:

1. Follow the instructions in the [EMR Serverless documentation](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-studio.html).

1. For **Job configuration**, use the Iceberg configuration for Spark provided for the AWS CLI and customize the highlighted fields for Iceberg. For detailed instructions, see [Using Apache Iceberg with EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-iceberg.html) in the Amazon EMR documentation.

#### Amazon EMR on EKS
<a name="amazon-emr-on-eks"></a>

To submit an Iceberg Spark job to Amazon EMR on EKS by using the AWS CLI:

1. Create the file `emr_eks_iceberg.json` with the following content on your workstation **- **Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location, replace `<bucket-name>` with your own bucket name:

   ```
   {
       "name": "iceberg-test-job",
       "virtualClusterId": "<VIRTUAL_CLUSTER_ID>",
       "executionRoleArn": "<ROLE_ARN>",
       "releaseLabel": "emr-7.14.0-latest",
       "jobDriver": {
           "sparkSubmitJobDriver": {
               "entryPoint": "s3://<bucket-name>/code/iceberg-job.py",
               "entryPointArguments": [],
               "sparkSubmitParameters": "--jars local:///usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar"
           }
       },
       "configurationOverrides": {
           "applicationConfiguration": [{
               "classification": "spark-defaults",
               "properties": {
                   "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
                   "spark.sql.catalog.iceberg_catalog": "org.apache.iceberg.spark.SparkCatalog",
                   "spark.sql.catalog.iceberg_catalog.type": "glue",
                   "spark.sql.catalog.iceberg_catalog.warehouse": "s3://<bucket-name>/<warehouse-dir>/"
               }
           }],
           "monitoringConfiguration": {
               "persistentAppUI": "ENABLED",
               "s3MonitoringConfiguration": {
                   "logUri": "s3://<bucket-name>/emr-eks/logs/"
               }
           }
       }
   }
   ```

**NOTE** You can register both catalogs at once (for example, `iceberg_catalog` or `spark_catalog` for self-managed Iceberg and `s3_tables_catalog` for S3 Tables) by including both sets of `spark.sql.catalog.<name>.*` entries — add the S3 Tables catalog properties from [Amazon S3 Tables catalog configuration](#emr-amazon-s3-tables). Then reference each table by its qualified catalog name in the same SQL query.

**NOTE** When using Amazon EMR release 8.x, specify `/usr/share/aws/iceberg/lib/iceberg-spark4-runtime.jar` for the `spark.jars` configuration.

1. Modify the configuration file for your Spark job by customizing the Iceberg configuration options that are highlighted in bold.

1. Submit the job by using the AWS CLI. Run the following command in the directory where the `emr_eks_iceberg.json` file is located:

   ```
   aws emr-containers start-job-run --cli-input-json file://emr_eks_iceberg.json
   ```

For detailed instructions, see [Using Apache Iceberg with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-iceberg.html) in the Amazon EMR on EKS documentation.

## Spark code examples
<a name="spark-code-examples"></a>

Once your Amazon EMR cluster is running and the Spark catalogs described above are registered, the day-to-day SQL and DataFrame code is engine-agnostic. For end-to-end examples — `CREATE TABLE`, `INSERT`, `UPDATE`, `MERGE INTO`, `DELETE`, reads, time travel, incremental queries, and metadata tables — see [Working with Iceberg tables by using Apache Spark](iceberg-spark.md).
