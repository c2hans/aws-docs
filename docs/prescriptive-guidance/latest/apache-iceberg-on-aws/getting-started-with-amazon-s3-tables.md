---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/getting-started-with-amazon-s3-tables.html
---

# Getting started with Amazon S3 Tables

This section covers the S3 Tables concepts you need to know and the two setup steps that make table buckets usable from the rest of this guide: creating a table bucket and enabling the AWS analytics services integration so the bucket surfaces in the AWS Glue Data Catalog as `s3tablescatalog/<table-bucket-name>`.

## Concepts and hierarchy
<a name="concepts-and-hierarchy"></a>

S3 Tables organizes tabular data in a three-level hierarchy inside a purpose-built S3 bucket type called a **table bucket**:

```
Table bucket                     (purpose-built S3 bucket)
└── Namespace                    (grouping within a bucket; equivalent to a database or schema)
    └── Table                    (Iceberg table)
```
+ **Table bucket** — a dedicated S3 bucket type that stores Iceberg tables as first-class subresources. You can create multiple table buckets in the same AWS account and Region. A table bucket has its own ARN and IAM policy surface (`s3tables:*`). Data lands under an S3-owned prefix inside the bucket; you do not address individual objects directly.
+ **Namespace** — a logical grouping of tables inside a table bucket. Analytics engines treat a namespace as a database or schema.
+ **Table** — an Iceberg table. The Iceberg format version (V2 or V3) is set by the writing client via the `format-version` table property; see the service-specific pages for how to create V3 tables. Table maintenance (compaction, snapshot expiration, unreferenced-file removal) is enabled by default and runs automatically; it can be tuned or disabled per table or table bucket via configuration APIs. — see [Maintenance in Amazon S3 Tables](maintenance-in-amazon-s3-tables.md).

## Create a table bucket
<a name="create-a-table-bucket"></a>

Create the table bucket with the following command (replace `<table-bucket-name>` with your own table bucket name. Table buckets can't be renamed after you create them):

```
aws s3tables create-table-bucket \
    --name <table-bucket-name> \
    --region us-east-1
```

You can also create table buckets from the Amazon S3 console (**Table buckets** in the left navigation) or with the `s3tables`[ CDK / CloudFormation resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Tables.html).

## Create a namespace
<a name="create-a-namespace"></a>

Namespaces are created inside a table bucket. From the CLI (replace `<table-bucket-name>` with your own table bucket name):

```
aws s3tables create-namespace \
    --table-bucket-arn arn:aws:s3tables:us-east-1:123456789012:bucket/<table-bucket-name> \
    --namespace sales
```

Once the integration described in the next section is enabled, you can also create namespaces through SQL from any AWS analytics engine (for example, `CREATE DATABASE "s3tablescatalog/<table-bucket-name>".sales` in Athena, `CREATE NAMESPACE s3_tables_catalog.sales` in Spark, ...).

## Enable the AWS analytics services integration
<a name="enable-the-aws-analytics-services-integration"></a>

To query and manage Iceberg tables/namespaces in S3 Tables from Analytics services (e.g., Amazon Athena, Amazon Redshift, Amazon EMR, AWS Glue, Amazon Data Firehose, PyIceberg, ...), enable the integration between S3 Tables and AWS analytics services. This one-time, account\+Region setup registers each of your table buckets as a federated catalog in the AWS Glue Data Catalog named `s3tablescatalog/<table-bucket-name>` and populates the Data Catalog with objects that mirror your namespaces and tables.

The integration is a **prerequisite for accessing S3 Tables from AWS analytics services regardless of the authorization model you plan to use** (IAM only or AWS Lake Formation). Access control is configured separately, as described in [Governance and access control](governance.md).

To enable the integration, run **Enable integration** in the Amazon S3 console (**Table buckets** view), or use the AWS CLI / CloudFormation equivalents. For the full step-by-step (IAM permissions for the caller, CLI catalog.json, cross-account setup), see [Integrating Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html).

Once you enable the AWS analytics services integration, the S3 Tables hierarchy shows up in the AWS Glue Data Catalog as follows:
+ **Federated catalog** — `s3tablescatalog` is created automatically the first time the integration is enabled in an account/Region.
+ **Child catalogs** — each S3 table bucket becomes a child catalog under `s3tablescatalog`.
+ **Databases** — each S3 namespace within a table bucket becomes a database.
+ **Tables** — each S3 table within a namespace becomes a table.

For example, if you have an S3 table bucket named `<table-bucket-name>` with a namespace `sales` containing a table `transactions`, the full path in the Data Catalog is:

```
s3tablescatalog/<table-bucket-name>/sales/transactions
```

This is the same identifier that analytics engines use when they qualify a query — for instance, from Athena: `"s3tablescatalog/<table-bucket-name>"."sales"."transactions"`.
