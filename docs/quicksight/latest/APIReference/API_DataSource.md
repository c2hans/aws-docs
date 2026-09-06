---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSource.html
---

# DataSource
<a name="API_DataSource"></a>

The structure of a data source.

## Contents
<a name="API_DataSource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AlternateDataSourceParameters **   <a name="QS-Type-DataSource-AlternateDataSourceParameters"></a>
A set of alternate data source parameters that you want to share for the credentials stored with this data source. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the `DataSourceParameters` structure that's in the request with the structures in the `AlternateDataSourceParameters` allow list. If the structures are an exact match, the request is allowed to use the credentials from this existing data source. If the `AlternateDataSourceParameters` list is null, the `Credentials` originally used with this `DataSourceParameters` are automatically allowed.
Type: Array of [DataSourceParameters](API_DataSourceParameters.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Arn **   <a name="QS-Type-DataSource-Arn"></a>
The Amazon Resource Name (ARN) of the data source.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-DataSource-CreatedTime"></a>
The time that this data source was created.
Type: Timestamp
Required: No

 ** CredentialStatus **   <a name="QS-Type-DataSource-CredentialStatus"></a>
The credential verification status of the data source. Valid values include:
+  `CONNECTED` – Credential validation succeeded.
+  `AUTH_FAILED` – Credential validation failed.
+  `NOT_VERIFIED` – Credential validation has not been performed.
Type: String
Valid Values: `CONNECTED | AUTH_FAILED | NOT_VERIFIED`
Required: No

 ** DataSourceId **   <a name="QS-Type-DataSource-DataSourceId"></a>
The ID of the data source. This ID is unique per AWS Region for each AWS account.
Type: String
Required: No

 ** DataSourceParameters **   <a name="QS-Type-DataSource-DataSourceParameters"></a>
The parameters that Quick Sight uses to connect to your underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.
Type: [DataSourceParameters](API_DataSourceParameters.md) object
Required: No

 ** ErrorInfo **   <a name="QS-Type-DataSource-ErrorInfo"></a>
Error information from the last update or the creation of the data source.
Type: [DataSourceErrorInfo](API_DataSourceErrorInfo.md) object
Required: No

 ** LastCredentialVerifiedAt **   <a name="QS-Type-DataSource-LastCredentialVerifiedAt"></a>
The time that the credentials were last verified.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-DataSource-LastUpdatedTime"></a>
The last time that this data source was updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-DataSource-Name"></a>
A display name for the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SecretArn **   <a name="QS-Type-DataSource-SecretArn"></a>
The Amazon Resource Name (ARN) of the secret associated with the data source in Amazon Secrets Manager.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:[-a-z0-9]*:secretsmanager:[-a-z0-9]*:[0-9]{12}:secret:.+`
Required: No

 ** SslProperties **   <a name="QS-Type-DataSource-SslProperties"></a>
Secure Socket Layer (SSL) properties that apply when Quick Sight connects to your underlying source.
Type: [SslProperties](API_SslProperties.md) object
Required: No

 ** Status **   <a name="QS-Type-DataSource-Status"></a>
The HTTP status of the request.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** Type **   <a name="QS-Type-DataSource-Type"></a>
The type of the data source. This type indicates which database engine the data source connects to.
Type: String
Valid Values: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | GITHUB | JIRA | MARIADB | MYSQL | ORACLE | POSTGRESQL | PRESTO | REDSHIFT | S3 | S3_TABLES | SALESFORCE | SERVICENOW | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | TWITTER | TIMESTREAM | AMAZON_OPENSEARCH | EXASOL | DATABRICKS | STARBURST | TRINO | BIGQUERY | GOOGLESHEETS | GOOGLE_DRIVE | CONFLUENCE | SHAREPOINT | ONE_DRIVE | WEB_CRAWLER | S3_KNOWLEDGE_BASE | QBUSINESS`
Required: No

 ** VpcConnectionProperties **   <a name="QS-Type-DataSource-VpcConnectionProperties"></a>
The VPC connection information. You need to use this parameter only when you want Quick Sight to use a VPC connection when connecting to your underlying source.
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object
Required: No

## See Also
<a name="API_DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSource)
