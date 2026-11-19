---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/governance.html
---

# Governance and access control

Iceberg itself is a table format, so governance is handled by the surrounding AWS services. On AWS, your Iceberg tables live in one of two places, and the access-control options differ slightly between them:
+ **Self-managed Iceberg on general-purpose Amazon S3.** You own the S3 bucket, the data files, and the Iceberg metadata. Tables are registered in a catalog (AWS Glue Data Catalog).
+ **Amazon S3 Tables.** AWS manages the storage (a table bucket), runs continuous table maintenance, and exposes tables through the built-in S3 Tables catalog, which can be surfaced in AWS Glue Data Catalog.

For both options, you can choose between two access-control modes: **IAM-based authorization **and **AWS Lake Formation**. Lake Formation is the way to add fine-grained access control (column, row, and cell filters) and cross-account sharing on top of the base IAM model.

## Access control for self-managed Iceberg on Amazon S3
<a name="access-control-for-self-managed-iceberg-on-amazon-s3.8afb3250-bbb7-5cbe-adf4-205bb375dd45"></a>

|
|
| **Mode** | **How access is decided** | **What the catalog returns** |
| --- |--- |--- |
| IAM | IAM policies on AWS Glue Data Catalog objects and on the underlying S3 bucket, prefix, and objects. <br />Representative IAM actions to allow, depending on the access needed (read, write, or table management): • AWS Glue (reads): `glue:GetDatabase`, `glue:GetTable`, `glue:GetTables`, `glue:GetPartitions` • AWS Glue (writes and table management): `glue:CreateTable`, `glue:UpdateTable`, `glue:DeleteTable` • Amazon S3 (reads): `s3:ListBucket`, `s3:GetBucketLocation`, `s3:GetObject` • Amazon S3 (writes): `s3:PutObject`, `s3:DeleteObject` | Table metadata only. The client reads data from S3 using its own IAM permissions. |
| Lake Formation | Lake Formation grants on the database, table, and columns, plus the IAM permissions needed to call Glue and Lake Formation APIs. Supports column, row, and cell filters for Lake Formation integrated engines (Amazon Athena, Amazon Redshift, Amazon EMR, AWS Glue). <br />Representative IAM actions to allow, depending on the access needed (read, write, or table management): • AWS Glue (reads): `glue:GetDatabase`, `glue:GetTable`, `glue:GetTables`, `glue:GetPartitions` • AWS Glue (writes and table management): `glue:CreateTable`, `glue:UpdateTable`, `glue:DeleteTable` • Lake Formation: `lakeformation:GetDataAccess` on the end-user principal. • Amazon S3: not required on the client. The IAM role registered with Lake Formation holds the S3 permissions and is used to vend credentials. | Table metadata plus, when the data location is registered with Lake Formation, temporary scoped S3 credentials vended for the table. The client does not need direct S3 permissions. |

For the steps to register a general-purpose Amazon S3 location with Lake Formation, see [Adding an Amazon S3 location to your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/register-data-lake.html) in the AWS Lake Formation documentation.

## Access control for Amazon S3 Tables
<a name="access-control-for-amazon-s3-tables.45575e9d-e394-5c78-8051-e5fb4a2100bb"></a>

|
|
| **Mode** | **How access is decided** | **What the catalog returns** |
| --- |--- |--- |
| IAM | IAM policies on AWS Glue Data Catalog objects and on S3 Tables resources (table bucket, namespace, and table), plus optional resource-based policies on the table bucket. Representative IAM actions to allow: • AWS Glue (reads): `glue:GetCatalog`, `glue:GetDatabase`, `glue:GetTable`, `glue:GetTables` • S3 Tables (reads): `s3tables:GetTableBucket`, `s3tables:ListNamespaces`, `s3tables:GetNamespace`, `s3tables:ListTables`, `s3tables:GetTable`, `s3tables:GetTableData`, `s3tables:GetTableMetadataLocation` • S3 Tables (writes and table management): `s3tables:CreateTable`, `s3tables:PutTableData`, `s3tables:UpdateTableMetadataLocation`, `s3tables:DeleteTable` | Table metadata only. The client reads the table using its own IAM permissions against S3 Tables. |
| Lake Formation | Lake Formation grants on the database, table, and columns, plus the IAM permissions needed to call Glue and Lake Formation APIs. Supports column, row, and cell filters for Lake Formation integrated engines (Amazon Athena, Amazon Redshift, Amazon EMR, AWS Glue).<br />Representative IAM actions to allow, depending on the access needed (read, write, or table management): • AWS Glue (reads): `glue:GetCatalog`, `glue:GetDatabase`, `glue:GetTable`, `glue:GetTables` • AWS Glue (writes and table management): `glue:CreateTable`, `glue:UpdateTable`, `glue:DeleteTable` • Lake Formation: `lakeformation:GetDataAccess` on the end-user principal. • S3 Tables: not required on the client. Lake Formation vends scoped credentials that cover the required `s3tables:*` actions. | Table metadata plus, when the table bucket is registered with Lake Formation, temporary scoped S3 credentials vended for the table. The client does not need direct S3 permissions. |

Registration happens as a side effect of enabling the S3 Tables integration with AWS Glue Data Catalog and Lake Formation. For the setup steps, see [Amazon S3 Tables integration with AWS Glue Data Catalog and AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/create-s3-tables-catalog.html) in the AWS Lake Formation documentation.

## AWS Glue Iceberg REST catalog and credential vending
<a name="aws-glue-iceberg-rest-catalog-and-credential-vending.a4820086-97af-5b46-b21d-712985486373"></a>

The AWS Glue Iceberg REST catalog is the common entry point that lets any Iceberg REST-compatible client (Apache Spark, Apache Flink, Trino, PyIceberg, DuckDB, and others) work with both storage options through the same protocol. Its behavior depends on how the table's data location is governed:
+ If the table's data location is **registered with AWS Lake Formation**, the REST catalog operates in **full table access** mode. The `LoadTable` response includes temporary, scoped S3 credentials (credential vending), so the client does not need direct S3 permissions, but only table-level grants apply. Fine-grained access control (column, row, and cell filters, and LF-Tag policies that resolve to data filters) is not enforced through the REST catalog, and if any fine-grained permissions are defined on the table, access through the REST catalog is denied automatically. Full table access must be explicitly enabled on the Lake Formation **Application integration** settings page. See [Application integration for full table access](https://docs.aws.amazon.com/lake-formation/latest/dg/full-table-credential-vending.html) in the AWS documentation.
+ If the data location is **not registered with Lake Formation**, the REST catalog returns metadata only, and the client reads S3 with its own IAM permissions. No Lake Formation enforcement applies.

In short: through the Iceberg REST catalog, Lake Formation governs access at the table level with vended credentials but does not apply column, row, or cell filters. If you need fine-grained access control, access the table through the AWS Glue Data Catalog from a query service that enforces Lake Formation policies natively (such as Amazon Athena or Amazon Redshift) rather than through the Iceberg REST catalog.

## Choosing a mode
<a name="choosing-a-mode.8df723aa-70d0-5f82-926f-d4b0f874048a"></a>
+ Use **IAM** when table-level access is sufficient, you do not need column, row, or cell filters, and permissions can be managed directly through IAM policies on Glue Data Catalog and S3 resources.
+ Use **Lake Formation** when you need any of the following: column, row, or cell filters; LF-Tag based access control (attribute-based grants against tag expressions, within or across accounts); cross-account sharing through AWS RAM; a single policy surface that covers both self-managed Iceberg and S3 Tables; or credential vending so clients do not need direct S3 permissions.

For an example of querying Iceberg tables by using Amazon Athena and AWS Lake Formation, see the AWS blog post [Interact with Apache Iceberg tables using Amazon Athena and cross account fine-grained permissions using AWS Lake Formation](https://aws.amazon.com/blogs/big-data/interact-with-apache-iceberg-tables-using-amazon-athena-and-cross-account-fine-grained-permissions-using-aws-lake-formation/).
