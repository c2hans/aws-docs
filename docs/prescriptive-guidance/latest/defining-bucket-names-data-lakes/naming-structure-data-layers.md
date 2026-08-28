---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/naming-structure-data-layers.html
---

# Naming Amazon S3 buckets
<a name="naming-structure-data-layers"></a>

The following sections provide naming structures for Amazon Simple Storage Service (Amazon S3) buckets in your data lake layers. However, you can customize the Amazon S3 bucket and path names according to your organization's requirements. We recommend that you create separate buckets for each individual layer because archiving, versioning, access, and encryption requirements can vary for each layer.

The following diagram shows the recommended naming structure for Amazon S3 buckets in the recommended data lake layers. The naming structure separates multiple business units, file formats, and partitions.

![The naming approach varies for S3 buckets according to the data layer that they are intended for.](http://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/images/guide-img/d76f2946-d940-4cf3-ac21-937dd4709e95/images/8c192691-f975-4408-b909-a1bbfa6dda88.png)

**Important**
Amazon S3 buckets must follow the naming guidelines from [Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) in the Amazon S3 documentation.

You can adapt data partitions according to your organization's requirements. However, you should use lowercase and key-value pairs (for example, `year=yyyy` instead of `yyyy`) so that you can update the catalog with the `MSCK REPAIR TABLE` command.

Defining a partition strategy depends on the nature of your data and, most importantly, the nature of your user queries. We recommend that you analyze consumption and data processing patterns to find the most suitable strategy for your organization. In general, it makes sense to provide higher hierarchy levels, such as `year=yyyy`, `month=mm`, and `day=dd`, on the raw data layer and lower hierarchy levels on consumption data layers, such as the stage layer and analytics layer. This is because raw data layers usually do not have the complex consumption patterns of data processing pipelines.

## Landing zone Amazon S3 bucket
<a name="landing-zone-naming-structure"></a>

You require an Amazon S3 bucket for your landing zone if sensitive datasets contain elements that must be masked before data is moved to the raw bucket.

The following table provides the naming structure, a description of the naming structure, and a name example for the Amazon S3 bucket in your landing zone layer.

|
|
| Naming format | Example |
| --- |--- |
| `s3://companyname-landingzoneawsregion-awsaccount\|uniqidenv/source/source_region/table/year=yyyy/month=mm/day=dd/table_<yearmonthday>.avro\|csv`+ `companyname` – The organization's name (optional)+ `awsregion` – The AWS Region, such as `us-east-1` or `sa-east-1`+ `awsaccount\|uniqid` – The unique identifier or AWS account ID+ `env` – The deployment environment, such as `dev`, `test`, or `prod`+ `source` – The source or content, such as MySQL database, ecommerce, or SAP+ `source_region` – Global business region, such as `us` or `asia`+ `table` – `tb_customer`, `tb_transactions`, or `tb_products` | `s3://anycompany-landingzoneuseast1-12345-dev/socialmedia/us/tb_products/year=2021/month=03/day=01/products_20210301.csv` |

## Raw layer Amazon S3 bucket
<a name="raw-data-layer-naming-structure"></a>

The raw data layer contains ingested data that has not been transformed and is in its original file format, such as  JSON or CSV. This data is typically organized by data source and the date that it was ingested into the raw data layer's Amazon S3 bucket.

The following table provides the naming structure, a description of the naming structure, and a name example for the Amazon S3 bucket in your raw data layer.

|
|
| Naming format | Example |
| --- |--- |
| `s3://companyname-raw-awsregion-awsaccount\|uniqid-env/source/source_region/table/year=yyyy/month=mm/day=dd/table_<yearmonthday>.avro\|csv`+ `companyname` – The organization's name (optional)+ `awsregion` – The AWS Region, such as `us-east-1` or `sa-east-1`+ `awsaccount\|uniqid` – The unique identifier or AWS account ID+ `env` – The deployment environment, such as `dev`, `test`, or `prod`+ `source` – The source or content, such as MySQL database, ecommerce, or SAP+ `source_region` – Global business region, such as `us` or `asia`+ `table` – `tb_customer`, `tb_transactions`, or `tb_products` | `s3://anycompany-raw-useast1-12345-dev/socialmedia/us/tb_products/year=2021/month=03/day=01/products_20210301.csv` |

## Stage layer Amazon S3 bucket
<a name="stage-data-layer-naming-structure"></a>

Data in the stage layer is read and transformed from the raw layer (for example, by using an AWS Glue or Amazon EMR job). This process validates the data (for example, by checking data types and headers) and then stores it in a consumption-ready file format, such as Apache Parquet. The metadata is stored in a table in the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html).

The following table provides the naming structure, a description of the naming structure, and a name example for the Amazon S3 bucket in your stage data layer.

|
|
| Naming format | Example |
| --- |--- |
| `s3://companyname-stageawsregion-awsaccount\|uniqidenv/source/source_region/ business_unit/table/<partitions>/table_<table_name>_<yearmonthday>.snap`+ `companyname` – The organization's name (optional)+ `awsregion` – The AWS Region, such as `us-east-1` or `sa-east-1`+ `awsaccount\|uniqid` – The unique identifier or AWS account ID+ `env` – The deployment environment, such as `dev`, `test`, or `prod`+ `source` – The source or content, such as MySQL database, ecommerce, or SAP+ `source_region` – Global business region, such as `us` or `asia`+ `business_unit` – The business unit that the data is processed for+ `table` – `tb_customer`, `tb_transactions`, or `tb_products`+ `partitions` – Partitions that provide the best performance for the consumer, allowing the query engine to avoid full data scans | `s3://anycompany-stagesaeast1-12345-dev/sap/br/customers/validated/dt=2021-03-01/table_customers_20210301.snappy.parquet py.parquet` |

## Analytics layer Amazon S3 bucket
<a name="analytics-data-layer-naming-structure"></a>

The analytics layer is similar to the stage layer because the data is in a processed file format, but the data is then aggregated according to your organization's requirements.

The following table provides the naming structure, a description of the naming structure, and a name example for the Amazon S3 bucket in your analytics data layer.

|
|
| Naming format | Example |
| --- |--- |
| `s3://companyname-analytics-awsregion-awsaccount\|uniqid-env/source_region/business_unit/tb_<region>_<table_name>_<file_format>/<partition_0>/<partition_1>/.../<partition_n>/xxxxx.<compression>.<file_format>`+ `companyname` – The organization's name (optional)+ `awsregion` – The AWS Region, such as `us-east-1` or `sa-east-1`+ `awsaccount\|uniqid` – The unique identifier or AWS account ID+ `env` – The deployment environment, such as `dev`, `test`, or `prod`+ `source` – The source or content, such as MySQL database, ecommerce, or SAP+ `source_region` – Global business region, such as `us` or `asia`+ `business_unit` – The business unit that the data is processed for+ `table` – `tb_customer`, `tb_transactions`, or `tb_products`+ `partitions` – Partitions that provide the best performance for the consumer, allowing the query engine to avoid full data scans | `s3://anycompany-analytics-useast1-12345-dev/us/sales/tb_us_customers_parquet/<partitions>/part-000001-20218c886790.c000.snappy.parquet` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
