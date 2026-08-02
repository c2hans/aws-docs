---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_DataCatalog.html
---

# DataCatalog
<a name="API_DataCatalog"></a>

Contains information about a data catalog in an AWS account.

**Note**
In the Athena console, data catalogs are listed as "data sources" on the **Data sources** page under the **Data source name** column.

## Contents
<a name="API_DataCatalog_Contents"></a>

 ** Name **   <a name="athena-Type-DataCatalog-Name"></a>
The name of the data catalog. The catalog name must be unique for the AWS account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Type **   <a name="athena-Type-DataCatalog-Type"></a>
The type of data catalog to create: `LAMBDA` for a federated catalog, `GLUE` for an AWS Glue Data Catalog, and `HIVE` for an external Apache Hive metastore. `FEDERATED` is a federated catalog for which Athena creates the connection and the Lambda function for you based on the parameters that you pass.
Type: String
Valid Values: `LAMBDA | GLUE | HIVE | FEDERATED`
Required: Yes

 ** ConnectionType **   <a name="athena-Type-DataCatalog-ConnectionType"></a>
The type of connection for a `FEDERATED` data catalog (for example, `REDSHIFT`, `MYSQL`, or `SQLSERVER`). For information about individual connectors, see [Available data source connectors](https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html).
Type: String
Valid Values: `DYNAMODB | MYSQL | POSTGRESQL | REDSHIFT | ORACLE | SYNAPSE | SQLSERVER | DB2 | OPENSEARCH | BIGQUERY | GOOGLECLOUDSTORAGE | HBASE | DOCUMENTDB | CMDB | TPCDS | TIMESTREAM | SAPHANA | SNOWFLAKE | DATALAKEGEN2 | DB2AS400`
Required: No

 ** Description **   <a name="athena-Type-DataCatalog-Description"></a>
An optional description of the data catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Error **   <a name="athena-Type-DataCatalog-Error"></a>
Text of the error that occurred during data catalog creation or deletion.
Type: String
Required: No

 ** Parameters **   <a name="athena-Type-DataCatalog-Parameters"></a>
Specifies the Lambda function or functions to use for the data catalog. This is a mapping whose values depend on the catalog type.
+ For the `HIVE` data catalog type, use the following syntax. The `metadata-function` parameter is required. `The sdk-version` parameter is optional and defaults to the currently supported version.

   `metadata-function=lambda_arn, sdk-version=version_number `
+ For the `LAMBDA` data catalog type, use one of the following sets of required parameters, but not both.
  + If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.

     `metadata-function=lambda_arn, record-function=lambda_arn `
  +  If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.

     `function=lambda_arn `
+ The `GLUE` type takes a catalog ID parameter and is required. The ` catalog_id ` is the account ID of the AWS account to which the AWS Glue catalog belongs.

   `catalog-id=catalog_id `
  + The `GLUE` data catalog type also applies to the default `AwsDataCatalog` that already exists in your account, of which you can have only one and cannot modify.
+ The `FEDERATED` data catalog type uses one of the following parameters, but not both. Use `connection-arn` for an existing AWS Glue connection. Use `connection-type` and `connection-properties` to specify the configuration setting for a new connection.
  +  `connection-arn:<glue_connection_arn_to_reuse> `
  +  `connection-type:MYSQL|REDSHIFT|...., connection-properties:"<json_string>"`

    For * `<json_string>` *, use escaped JSON text, as in the following example.

     `"{\"spill_bucket\":\"my_spill\",\"spill_prefix\":\"athena-spill\",\"host\":\"abc12345.snowflakecomputing.com\",\"port\":\"1234\",\"warehouse\":\"DEV_WH\",\"database\":\"TEST\",\"schema\":\"PUBLIC\",\"SecretArn\":\"arn:aws:secretsmanager:ap-south-1:111122223333:secret:snowflake-XHb67j\"}"`
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 51200.
Required: No

 ** Status **   <a name="athena-Type-DataCatalog-Status"></a>
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

## See Also
<a name="API_DataCatalog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/DataCatalog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/DataCatalog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/DataCatalog)
