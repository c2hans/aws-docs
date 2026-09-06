---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GlueConnection.html
---

# GlueConnection
<a name="API_GlueConnection"></a>

The AWS Glue connection.

## Contents
<a name="API_GlueConnection_Contents"></a>

 ** athenaProperties **   <a name="datazone-Type-GlueConnection-athenaProperties"></a>
The Amazon Athena properties of the AWS Glue connection.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** authenticationConfiguration **   <a name="datazone-Type-GlueConnection-authenticationConfiguration"></a>
The authentication configuration of the AWS Glue connection.
Type: [AuthenticationConfiguration](API_AuthenticationConfiguration.md) object
Required: No

 ** compatibleComputeEnvironments **   <a name="datazone-Type-GlueConnection-compatibleComputeEnvironments"></a>
The compatible compute environments of the AWS Glue connection.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `SPARK | ATHENA | PYTHON`
Required: No

 ** connectionProperties **   <a name="datazone-Type-GlueConnection-connectionProperties"></a>
The properties of the AWS Glue connection.
Type: String to string map
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** connectionSchemaVersion **   <a name="datazone-Type-GlueConnection-connectionSchemaVersion"></a>
The connection schema version of the AWS Glue connection.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2.
Required: No

 ** connectionType **   <a name="datazone-Type-GlueConnection-connectionType"></a>
The type of the AWS Glue connection.
Type: String
Valid Values: `ATHENA | BIGQUERY | DATABRICKS | DOCUMENTDB | DYNAMODB | HYPERPOD | IAM | MYSQL | OPENSEARCH | ORACLE | POSTGRESQL | REDSHIFT | S3 | SAPHANA | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | VERTICA | WORKFLOWS_MWAA | AMAZON_Q | MLFLOW | VPC | GIT`
Required: No

 ** creationTime **   <a name="datazone-Type-GlueConnection-creationTime"></a>
The creation time of the AWS Glue connection.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-GlueConnection-description"></a>
The description of the AWS Glue connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** lastConnectionValidationTime **   <a name="datazone-Type-GlueConnection-lastConnectionValidationTime"></a>
The last validation time of the AWS Glue connection.
Type: Timestamp
Required: No

 ** lastUpdatedBy **   <a name="datazone-Type-GlueConnection-lastUpdatedBy"></a>
The user who last updated the AWS Glue connection.
Type: String
Required: No

 ** lastUpdatedTime **   <a name="datazone-Type-GlueConnection-lastUpdatedTime"></a>
The timestamp at which the AWS Glue connection was last updated.
Type: Timestamp
Required: No

 ** matchCriteria **   <a name="datazone-Type-GlueConnection-matchCriteria"></a>
The match criteria of the AWS Glue connection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** name **   <a name="datazone-Type-GlueConnection-name"></a>
The name of the AWS Glue connection.
Type: String
Required: No

 ** physicalConnectionRequirements **   <a name="datazone-Type-GlueConnection-physicalConnectionRequirements"></a>
The physical connection requirements of the AWS Glue connection.
Type: [PhysicalConnectionRequirements](API_PhysicalConnectionRequirements.md) object
Required: No

 ** pythonProperties **   <a name="datazone-Type-GlueConnection-pythonProperties"></a>
The Python properties of the AWS Glue connection.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** sparkProperties **   <a name="datazone-Type-GlueConnection-sparkProperties"></a>
The Spark properties of the AWS Glue connection.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** status **   <a name="datazone-Type-GlueConnection-status"></a>
The status of the AWS Glue connection.
Type: String
Valid Values: `CREATING | CREATE_FAILED | DELETING | DELETE_FAILED | READY | UPDATING | UPDATE_FAILED | DELETED`
Required: No

 ** statusReason **   <a name="datazone-Type-GlueConnection-statusReason"></a>
The status reason of the AWS Glue connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

## See Also
<a name="API_GlueConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GlueConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GlueConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GlueConnection)
