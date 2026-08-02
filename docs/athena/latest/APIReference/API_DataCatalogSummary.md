---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_DataCatalogSummary.html
---

# DataCatalogSummary
<a name="API_DataCatalogSummary"></a>

The summary information for the data catalog, which includes its name and type.

## Contents
<a name="API_DataCatalogSummary_Contents"></a>

 ** CatalogName **   <a name="athena-Type-DataCatalogSummary-CatalogName"></a>
The name of the data catalog. The catalog name is unique for the AWS account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ConnectionType **   <a name="athena-Type-DataCatalogSummary-ConnectionType"></a>
The type of connection for a `FEDERATED` data catalog (for example, `REDSHIFT`, `MYSQL`, or `SQLSERVER`). For information about individual connectors, see [Available data source connectors](https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html).
Type: String
Valid Values: `DYNAMODB | MYSQL | POSTGRESQL | REDSHIFT | ORACLE | SYNAPSE | SQLSERVER | DB2 | OPENSEARCH | BIGQUERY | GOOGLECLOUDSTORAGE | HBASE | DOCUMENTDB | CMDB | TPCDS | TIMESTREAM | SAPHANA | SNOWFLAKE | DATALAKEGEN2 | DB2AS400`
Required: No

 ** Error **   <a name="athena-Type-DataCatalogSummary-Error"></a>
Text of the error that occurred during data catalog creation or deletion.
Type: String
Required: No

 ** Status **   <a name="athena-Type-DataCatalogSummary-Status"></a>
The status of the creation or deletion of the data catalog.
+ The `LAMBDA`, `GLUE`, and `HIVE` data catalog types are created synchronously. Their status is either `CREATE_COMPLETE` or `CREATE_FAILED`.
+ The `FEDERATED` data catalog type is created asynchronously.
Data catalog creation status:
+  `CREATE_IN_PROGRESS`: Federated data catalog creation in progress.
+  `CREATE_COMPLETE`: Data catalog creation complete.
+  `CREATE_FAILED`: Data catalog could not be created.
+  `CREATE_FAILED_CLEANUP_IN_PROGRESS`: Federated data catalog creation failed and is being removed.
+  `CREATE_FAILED_CLEANUP_COMPLETE`: Federated data catalog creation failed and was removed.
+  `CREATE_FAILED_CLEANUP_FAILED`: Federated data catalog creation failed but could not be removed.
Data catalog deletion status:
+  `DELETE_IN_PROGRESS`: Federated data catalog deletion in progress.
+  `DELETE_COMPLETE`: Federated data catalog deleted.
+  `DELETE_FAILED`: Federated data catalog could not be deleted.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | CREATE_FAILED_CLEANUP_IN_PROGRESS | CREATE_FAILED_CLEANUP_COMPLETE | CREATE_FAILED_CLEANUP_FAILED | DELETE_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED`
Required: No

 ** Type **   <a name="athena-Type-DataCatalogSummary-Type"></a>
The data catalog type.
Type: String
Valid Values: `LAMBDA | GLUE | HIVE | FEDERATED`
Required: No

## See Also
<a name="API_DataCatalogSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/DataCatalogSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/DataCatalogSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/DataCatalogSummary)
