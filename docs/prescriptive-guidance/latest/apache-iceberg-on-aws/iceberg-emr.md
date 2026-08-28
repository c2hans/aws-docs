---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-emr.html
---

# Working with Iceberg in Amazon EMR
<a name="iceberg-emr"></a>

Amazon EMR provides petabyte-scale data processing, interactive analytics, and machine learning in the cloud by using open source frameworks such as Apache Spark, Apache Hive, Flink, and Trino.

**Note**
This guide uses Apache Spark for examples.

Amazon EMR supports multiple deployment options: Amazon EMR on EC2, Amazon EMR on EKS, Amazon EMR Serverless, and Amazon EMR on AWS Outposts. To choose a deployment option for your workload, see the [Amazon EMR FAQ](https://aws.amazon.com/emr/faqs/).

## Version and feature compatibility
<a name="emr-version"></a>

Amazon EMR version 6.5.0 and later versions support Apache Iceberg natively. For a list of supported Iceberg versions for each Amazon EMR release, see [Iceberg release history](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Iceberg-release-history.html) in the Amazon EMR documentation. Also review the sections under [Use a cluster with Iceberg](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html) to see which Iceberg features are supported in Amazon EMR on different frameworks.

We recommend that you use the latest Amazon EMR version to benefit from the latest supported Iceberg version. The code examples and configurations in this section assume that you're using Amazon EMR release **emr-7.8.0**.

## Creating an Amazon EMR cluster with Iceberg
<a name="emr-cluster"></a>

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

## Developing Iceberg applications in Amazon EMR
<a name="emr-apps"></a>

To develop the Spark code for your Iceberg applications, you can use [Amazon EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html), which is a web-based integrated development environment (IDE) for fully managed Jupyter notebooks that run on Amazon EMR clusters.

### Using Amazon EMR Studio notebooks
<a name="using-9999999999999999emr--studio-notebooks.6e529f29-03e3-5c5d-ad47-60acaf3151e8"></a>

You can interactively develop Spark applications in Amazon EMR Studio Workspace notebooks and connect those notebooks to your Amazon EMR on EC2 clusters or Amazon EMR on EKS managed endpoints. See AWS service documentation for instructions on setting up an EMR Studio for [Amazon EMR on EC2](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-set-up.html) and [Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-create-eks-cluster.html).

To use Iceberg in EMR Studio, follow these steps:

1. Launch an Amazon EMR cluster with Iceberg enabled, as instructed in [Use a cluster with Iceberg Installed](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg-use-cluster.html).

1. Set up an EMR Studio. For instructions, see [Set up an Amazon EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-set-up.html).

1. Open an EMR Studio Workspace notebook and run the following code as the first cell in the notebook to configure your Spark session for using Iceberg:

   ```
   %%configure -f
   {
       "conf": {
           "spark.sql.catalog.<catalog_name>": "org.apache.iceberg.spark.SparkCatalog",
           "spark.sql.catalog.<catalog_name>.warehouse": "s3://YOUR-BUCKET-NAME/YOUR-FOLDER-NAME/",
           "spark.sql.catalog.<catalog_name>.type": "glue",
           "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
       }
   }
   ```

   where:
   + `<catalog_name>` is your Iceberg Spark session catalog name. Replace it with a name of your choice, and remember to change the references throughout all configurations that are associated with this catalog. In your code, you can refer to your Iceberg tables with the fully qualified table name, including the Spark session catalog name, as follows:

     ```
     <catalog_name>.<database_name>.<table_name>
     ```

     Alternatively, you can change the default catalog to the Iceberg catalog that you defined by setting `spark.sql.defaultCatalog` to your catalog name. This second approach enables you to refer to tables without the catalog prefix, which can simplify your queries.
   + `<catalog_name>.warehouse` points to the Amazon S3 path where you want to store your data and metadata.
   + To make the catalog an AWS Glue Data Catalog, set `spark.sql.catalog.<catalog_name>.type` to `glue`. This key is required to point to an implementation class for any custom catalog implementation. The [General best practices](best-practices-general.md) section later in this guide describes the different Iceberg-supported catalogs.

1. You can now start interactively developing your Spark application for Iceberg in the notebook, as you would for any other Spark application.

For more information about configuring Spark for Apache Iceberg by using Amazon EMR Studio, see the blog post [Build a high-performance, ACID compliant, evolving data lake using Apache Iceberg on Amazon EMR](https://aws.amazon.com/blogs/big-data/build-a-high-performance-acid-compliant-evolving-data-lake-using-apache-iceberg-on-amazon-emr/).

### Running Iceberg jobs in Amazon EMR
<a name="running-iceberg-jobs-in-9999999999999999emr-.568e92fd-91a3-50e1-b407-c0b3ac41c73c"></a>

After you develop the Spark application code for your Iceberg workload, you can run it on any Amazon EMR deployment option that supports Iceberg (see the [Amazon EMR FAQ](https://aws.amazon.com/emr/faqs/#Deployment_options)).

As with other Spark jobs, you can submit work to an Amazon EMR on EC2 cluster by adding steps or by interactively submitting Spark jobs to the master node. To run a Spark job, see the following Amazon EMR documentation pages:
+ For an overview of the different options for submitting work to an Amazon EMR on EC2 cluster and detailed instructions for each option, see [Submit work to a cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-work-with-steps.html).
+ For Amazon EMR on EKS, see [Running Spark jobs with StartJobRun](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/job-runs.html).
+ For EMR Serverless, see [Running jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs.html).

The following sections provide an example for each Amazon EMR deployment option.

#### Amazon EMR on EC2
<a name="9999999999999999emr--on-ec2.7c4330e6-d992-5f9a-92f1-e35af8bde1cf"></a>

You can use these steps to submit the Iceberg Spark job:

1. Create the file `emr_step_iceberg.json` with the following content on your workstation:

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
           "spark.sql.catalog.<catalog_name>=org.apache.iceberg.spark.SparkCatalog",
           "--conf",
           "spark.sql.catalog.<catalog_name>.type=glue",
           "--conf",
           "spark.sql.catalog.<catalog_name>.warehouse=s3://YOUR-BUCKET-NAME/YOUR-FOLDER-NAME/",
           "s3://YOUR-BUCKET-NAME/code/iceberg-job.py"
       ]
   }]
   ```

1. Modify the configuration file for your specific Spark job by customizing the Iceberg configuration options that are highlighted in bold.

1. Submit the step by using the AWS Command Line Interface (AWS CLI). Run the command in the directory where the `emr_step_iceberg.json` file is located.

   ```
   aws emr add-steps --cluster-id <cluster_id> --steps file://emr_step_iceberg.json
   ```

#### Amazon EMR Serverless
<a name="9999999999999999emrserverlesslong-.7316866a-14c3-545c-99af-4eefb82212c1"></a>

To submit an Iceberg Spark job to EMR Serverless by using the AWS CLI:

1. Create the file `emr_serverless_iceberg.json` with the following content on your workstation:

   ```
   {
       "applicationId": "<APPLICATION_ID>",
       "executionRoleArn": "<ROLE_ARN>",
       "name": "iceberg-test-job",
       "jobDriver": {
           "sparkSubmit": {
               "entryPoint": "s3://YOUR-BUCKET-NAME/code/iceberg-job.py",
               "entryPointArguments": []
           }
       },
       "configurationOverrides": {
           "applicationConfiguration": [{
               "classification": "spark-defaults",
               "properties": {
                   "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
                   "spark.sql.catalog.<catalog_name>": "org.apache.iceberg.spark.SparkCatalog",
                   "spark.sql.catalog.<catalog_name>.type": "glue",
                   "spark.sql.catalog.<catalog_name>.warehouse": "s3://YOUR-BUCKET-NAME/YOUR-FOLDER-NAME/",
                   "spark.jars":"/usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar",
                  "spark.hadoop.hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"
               }
           }],
           "monitoringConfiguration": {
               "s3MonitoringConfiguration": {
                   "logUri": "s3://YOUR-BUCKET-NAME/emr-serverless/logs/"
               }
           }
       }
   }
   ```

1. Modify the configuration file for your specific Spark job by customizing the Iceberg configuration options that are highlighted in bold.

1. Submit the job by using the AWS CLI. Run the command in the directory where the `emr_serverless_iceberg.json` file is located:

   ```
   aws emr-serverless start-job-run --cli-input-json file://emr_serverless_iceberg.json
   ```

To submit an Iceberg Spark job to EMR Serverless by using the EMR Studio console:

1. Follow the instructions in the [EMR Serverless documentation](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-studio.html).

2. For **Job configuration**, use the Iceberg configuration for Spark provided for the AWS CLI and customize the highlighted fields for Iceberg. For detailed instructions, see [Using Apache Iceberg with EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-iceberg.html) in the Amazon EMR documentation.

#### Amazon EMR on EKS
<a name="9999999999999999emr--on-eks.0412ab42-efa2-5936-9c09-3ed24000033c"></a>

To submit an Iceberg Spark job to Amazon EMR on EKS by using the AWS CLI:

1. Create the file `emr_eks_iceberg.json` with the following content on your workstation:

   ```
   {
       "name": "iceberg-test-job",
       "virtualClusterId": "<VIRTUAL_CLUSTER_ID>",
       "executionRoleArn": "<ROLE_ARN>",
       "releaseLabel": "emr-6.9.0-latest",
       "jobDriver": {
           "sparkSubmitJobDriver": {
               "entryPoint": "s3://YOUR-BUCKET-NAME/code/iceberg-job.py",
               "entryPointArguments": [],
               "sparkSubmitParameters": "--jars local:///usr/share/aws/iceberg/lib/iceberg-spark3-runtime.jar"
           }
       },
       "configurationOverrides": {
           "applicationConfiguration": [{
               "classification": "spark-defaults",
               "properties": {
                   "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
                   "spark.sql.catalog.<catalog_name>": "org.apache.iceberg.spark.SparkCatalog",
                   "spark.sql.catalog.<catalog_name>.type": "glue",
                   "spark.sql.catalog.<catalog_name>.warehouse": "s3://YOUR-BUCKET-NAME/YOUR-FOLDER-NAME/",
                   "spark.hadoop.hive.metastore.client.factory.class": "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"
               }
           }],
           "monitoringConfiguration": {
               "persistentAppUI": "ENABLED",
               "s3MonitoringConfiguration": {
                   "logUri": "s3://YOUR-BUCKET-NAME/emr-serverless/logs/"
               }
           }
       }
   }
   ```

1. Modify the configuration file for your Spark job by customizing the Iceberg configuration options that are highlighted in bold.

1. Submit the job by using the AWS CLI. Run the following command in the directory where the `emr_eks_iceberg.json` file is located:

   ```
   aws emr-containers start-job-run --cli-input-json file://emr_eks_iceberg.json
   ```

For detailed instructions, see [Using Apache Iceberg with Amazon EMR on EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/tutorial-iceberg.html) in the Amazon EMR on EKS documentation.

## Best practices for Amazon EMR
<a name="emr-best-practices"></a>

This section provides general guidelines for tuning Spark jobs in Amazon EMR to optimize reading and writing data to Iceberg tables. For Iceberg-specific best practices, see the [Best practices](best-practices.md) section later in this guide.
+ **Use the latest version of Amazon EMR** – Amazon EMR provides Spark optimizations out of the box with the Amazon EMR Spark runtime. AWS improves the performance of the Spark runtime engine with each new release.
+ **Determine the optimal infrastructure for your Spark workloads** – Spark workloads might require different types of hardware for different job characteristics to ensure optimal performance. Amazon EMR [supports several instance types](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-supported-instance-types.html) (such as compute optimized, memory optimized, general purpose, and storage optimized) to cover all types of processing requirements. When you onboard new workloads, we recommend that you benchmark with general instance types such as M5 or M6g. Monitor the operating system (OS) and YARN metrics from Ganglia and Amazon CloudWatch to determine the system bottlenecks (CPU, memory, storage, and I/O) at peak load and choose appropriate hardware.
+ **Tune **`spark.sql.shuffle.partitions` – Set the `spark.sql.shuffle.partitions` property to the total number of virtual cores (vCores) in your cluster or to a multiple of that value (typically, 1 to 2 times the total number of vCores). This setting affects the parallelism of Spark when you use hash and range partitioning as the write distribution mode. It requests a shuffle before writing to organize the data, which ensures partition alignment.
+ **Enable managed scaling** – For almost all use cases, we recommend that you enable managed scaling and dynamic allocation. However, if you have a workload that has a predictable pattern, we suggest that you disable automatic scaling and dynamic allocation. When managed scaling is enabled, we recommend that you use Spot Instances to reduce costs. Use Spot Instances for task nodes instead of core or master nodes. When you use Spot Instances, use instance fleets with multiple instance types per fleet to ensure spot availability.
+ **Use broadcast join when possible** – Broadcast (mapside) join is the most optimal join, as long as one of your tables is small enough to fit in the memory of your smallest node (in the order of MBs) and you are performing an equi (=) join. All join types except for full outer joins are supported. A broadcast join broadcasts the smaller table as a hash table across all worker nodes in memory. After the small table has been broadcast, you cannot make changes to it. Because the hash table is locally in the Java virtual machine (JVM), it can be merged easily with the large table based on the join condition by using a hash join. Broadcast joins provide high performance because of minimal shuffle overhead.
+ **Tune the garbage collector** – If garbage collection (GC) cycles are slow, consider switching from the default parallel garbage collector to G1GC for better performance. To optimize GC performance, you can fine-tune the GC parameters. To track GC performance, you can monitor it by using the Spark UI. Ideally, the GC time should be less than or equal to 1 percent of the total task runtime.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
