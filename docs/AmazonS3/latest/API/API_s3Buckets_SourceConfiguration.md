---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_SourceConfiguration.html
---

# SourceConfiguration
<a name="API_s3Buckets_SourceConfiguration"></a>

The source to migrate from. Set exactly one member, and set `sourceType` to match it.

## Contents
<a name="API_s3Buckets_SourceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** glueTable **   <a name="AmazonS3-Type-s3Buckets_SourceConfiguration-glueTable"></a>
An AWS Glue Data Catalog table to migrate. The table must be an external Apache Hive table whose data is stored as Parquet in a general purpose bucket in the same account and Region as the table bucket. Views, transactional (ACID) tables, tables in an open table format such as Apache Iceberg, and tables registered with AWS Lake Formation can't be migrated. If the table can't be migrated, the migration fails, and the table compatibility report lists the reason.
Type: [GlueTableSource](API_s3Buckets_GlueTableSource.md) object
Required: No

## See Also
<a name="API_s3Buckets_SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/SourceConfiguration)
