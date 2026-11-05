---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_GlueTableSource.html
---

# GlueTableSource
<a name="API_s3Buckets_GlueTableSource"></a>

An AWS Glue Data Catalog table to migrate. The table must be an external Apache Hive table whose data is stored as Parquet in a general purpose bucket in the same account and Region as the table bucket. Views, transactional (ACID) tables, tables in an open table format such as Apache Iceberg, and tables registered with AWS Lake Formation can't be migrated. If the table can't be migrated, the migration fails, and the table compatibility report lists the reason.

## Contents
<a name="API_s3Buckets_GlueTableSource_Contents"></a>

 ** catalogId **   <a name="AmazonS3-Type-s3Buckets_GlueTableSource-catalogId"></a>
The ID of the Data Catalog that contains the table. It must be your account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** databaseName **   <a name="AmazonS3-Type-s3Buckets_GlueTableSource-databaseName"></a>
The name of the database that contains the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** tableName **   <a name="AmazonS3-Type-s3Buckets_GlueTableSource-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_s3Buckets_GlueTableSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/GlueTableSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/GlueTableSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/GlueTableSource)
