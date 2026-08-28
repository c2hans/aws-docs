---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Endpoint.html
---

# Endpoint
<a name="API_Endpoint"></a>

Describes an endpoint of a database instance in response to operations such as the following:
+  `CreateEndpoint`
+  `DescribeEndpoint`
+  `ModifyEndpoint`

## Contents
<a name="API_Endpoint_Contents"></a>

 ** CertificateArn **   <a name="DMS-Type-Endpoint-CertificateArn"></a>
The Amazon Resource Name (ARN) used for SSL connection to the endpoint.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-Endpoint-DatabaseName"></a>
The name of the database at the endpoint.
Type: String
Required: No

 ** DmsTransferSettings **   <a name="DMS-Type-Endpoint-DmsTransferSettings"></a>
The settings for the AWS DMS Transfer type source. For more information, see the DmsTransferSettings structure.
Type: [DmsTransferSettings](API_DmsTransferSettings.md) object
Required: No

 ** DocDbSettings **   <a name="DMS-Type-Endpoint-DocDbSettings"></a>
Provides information that defines a DocumentDB endpoint.
Type: [DocDbSettings](API_DocDbSettings.md) object
Required: No

 ** DynamoDbSettings **   <a name="DMS-Type-Endpoint-DynamoDbSettings"></a>
The settings for the DynamoDB target endpoint. For more information, see the `DynamoDBSettings` structure.
Type: [DynamoDbSettings](API_DynamoDbSettings.md) object
Required: No

 ** ElasticsearchSettings **   <a name="DMS-Type-Endpoint-ElasticsearchSettings"></a>
The settings for the OpenSearch source endpoint. For more information, see the `ElasticsearchSettings` structure.
Type: [ElasticsearchSettings](API_ElasticsearchSettings.md) object
Required: No

 ** EndpointArn **   <a name="DMS-Type-Endpoint-EndpointArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
Type: String
Required: No

 ** EndpointIdentifier **   <a name="DMS-Type-Endpoint-EndpointIdentifier"></a>
The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
Type: String
Required: No

 ** EndpointType **   <a name="DMS-Type-Endpoint-EndpointType"></a>
The type of endpoint. Valid values are `source` and `target`.
Type: String
Valid Values: `source | target`
Required: No

 ** EngineDisplayName **   <a name="DMS-Type-Endpoint-EngineDisplayName"></a>
The expanded name for the engine name. For example, if the `EngineName` parameter is "aurora", this value would be "Amazon Aurora MySQL".
Type: String
Required: No

 ** EngineName **   <a name="DMS-Type-Endpoint-EngineName"></a>
The database engine name. Valid values, depending on the EndpointType, include `"mysql"`, `"oracle"`, `"postgres"`, `"mariadb"`, `"aurora"`, `"aurora-postgresql"`, `"redshift"`, `"redshift-serverless"`, `"s3"`, `"db2"`, `"db2-zos"`, `"azuredb"`, `"sybase"`, `"dynamodb"`, `"mongodb"`, `"kinesis"`, `"kafka"`, `"elasticsearch"`, `"documentdb"`, `"sqlserver"`, `"neptune"`, and `"babelfish"`.
Type: String
Required: No

 ** ExternalId **   <a name="DMS-Type-Endpoint-ExternalId"></a>
 Value returned by a call to CreateEndpoint that can be used for cross-account validation. Use it on a subsequent call to CreateEndpoint to create the endpoint with a cross-account.
Type: String
Required: No

 ** ExternalTableDefinition **   <a name="DMS-Type-Endpoint-ExternalTableDefinition"></a>
The external table definition.
Type: String
Required: No

 ** ExtraConnectionAttributes **   <a name="DMS-Type-Endpoint-ExtraConnectionAttributes"></a>
Additional connection attributes used to connect to the endpoint.
Type: String
Required: No

 ** GcpMySQLSettings **   <a name="DMS-Type-Endpoint-GcpMySQLSettings"></a>
Settings in JSON format for the source GCP MySQL endpoint.
Type: [GcpMySQLSettings](API_GcpMySQLSettings.md) object
Required: No

 ** IBMDb2Settings **   <a name="DMS-Type-Endpoint-IBMDb2Settings"></a>
The settings for the IBM Db2 LUW source endpoint. For more information, see the `IBMDb2Settings` structure.
Type: [IBMDb2Settings](API_IBMDb2Settings.md) object
Required: No

 ** IsReadOnly **   <a name="DMS-Type-Endpoint-IsReadOnly"></a>
Indicates whether the endpoint is read-only. When set to `true`, this endpoint is managed by AWS DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only endpoints through their associated zero-ETL integration.
Type: Boolean
Required: No

 ** KafkaSettings **   <a name="DMS-Type-Endpoint-KafkaSettings"></a>
The settings for the Apache Kafka target endpoint. For more information, see the `KafkaSettings` structure.
Type: [KafkaSettings](API_KafkaSettings.md) object
Required: No

 ** KinesisSettings **   <a name="DMS-Type-Endpoint-KinesisSettings"></a>
The settings for the Amazon Kinesis target endpoint. For more information, see the `KinesisSettings` structure.
Type: [KinesisSettings](API_KinesisSettings.md) object
Required: No

 ** KmsKeyId **   <a name="DMS-Type-Endpoint-KmsKeyId"></a>
An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.
If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key.
 AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** LakehouseSettings **   <a name="DMS-Type-Endpoint-LakehouseSettings"></a>
Settings in JSON format for the target Lakehouse endpoint. This parameter applies to endpoints that are automatically created by DMS for a Lakehouse data warehouse as part of a zero-ETL integration.
Type: [LakehouseSettings](API_LakehouseSettings.md) object
Required: No

 ** MicrosoftSQLServerSettings **   <a name="DMS-Type-Endpoint-MicrosoftSQLServerSettings"></a>
The settings for the Microsoft SQL Server source and target endpoint. For more information, see the `MicrosoftSQLServerSettings` structure.
Type: [MicrosoftSQLServerSettings](API_MicrosoftSQLServerSettings.md) object
Required: No

 ** MongoDbSettings **   <a name="DMS-Type-Endpoint-MongoDbSettings"></a>
The settings for the MongoDB source endpoint. For more information, see the `MongoDbSettings` structure.
Type: [MongoDbSettings](API_MongoDbSettings.md) object
Required: No

 ** MySQLSettings **   <a name="DMS-Type-Endpoint-MySQLSettings"></a>
The settings for the MySQL source and target endpoint. For more information, see the `MySQLSettings` structure.
Type: [MySQLSettings](API_MySQLSettings.md) object
Required: No

 ** NeptuneSettings **   <a name="DMS-Type-Endpoint-NeptuneSettings"></a>
The settings for the Amazon Neptune target endpoint. For more information, see the `NeptuneSettings` structure.
Type: [NeptuneSettings](API_NeptuneSettings.md) object
Required: No

 ** OracleSettings **   <a name="DMS-Type-Endpoint-OracleSettings"></a>
The settings for the Oracle source and target endpoint. For more information, see the `OracleSettings` structure.
Type: [OracleSettings](API_OracleSettings.md) object
Required: No

 ** Port **   <a name="DMS-Type-Endpoint-Port"></a>
The port value used to access the endpoint.
Type: Integer
Required: No

 ** PostgreSQLSettings **   <a name="DMS-Type-Endpoint-PostgreSQLSettings"></a>
The settings for the PostgreSQL source and target endpoint. For more information, see the `PostgreSQLSettings` structure.
Type: [PostgreSQLSettings](API_PostgreSQLSettings.md) object
Required: No

 ** RedisSettings **   <a name="DMS-Type-Endpoint-RedisSettings"></a>
The settings for the Redis target endpoint. For more information, see the `RedisSettings` structure.
Type: [RedisSettings](API_RedisSettings.md) object
Required: No

 ** RedshiftSettings **   <a name="DMS-Type-Endpoint-RedshiftSettings"></a>
Settings for the Amazon Redshift endpoint.
Type: [RedshiftSettings](API_RedshiftSettings.md) object
Required: No

 ** S3Settings **   <a name="DMS-Type-Endpoint-S3Settings"></a>
The settings for the S3 target endpoint. For more information, see the `S3Settings` structure.
Type: [S3Settings](API_S3Settings.md) object
Required: No

 ** ServerName **   <a name="DMS-Type-Endpoint-ServerName"></a>
The name of the server at the endpoint.
Type: String
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-Endpoint-ServiceAccessRoleArn"></a>
The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the `iam:PassRole` action.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-Endpoint-SslMode"></a>
The SSL mode used to connect to the endpoint. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

 ** Status **   <a name="DMS-Type-Endpoint-Status"></a>
The status of the endpoint.
Type: String
Required: No

 ** SybaseSettings **   <a name="DMS-Type-Endpoint-SybaseSettings"></a>
The settings for the SAP ASE source and target endpoint. For more information, see the `SybaseSettings` structure.
Type: [SybaseSettings](API_SybaseSettings.md) object
Required: No

 ** TimestreamSettings **   <a name="DMS-Type-Endpoint-TimestreamSettings"></a>
The settings for the Amazon Timestream target endpoint. For more information, see the `TimestreamSettings` structure.
Type: [TimestreamSettings](API_TimestreamSettings.md) object
Required: No

 ** Username **   <a name="DMS-Type-Endpoint-Username"></a>
The user name used to connect to the endpoint.
Type: String
Required: No

## See Also
<a name="API_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Endpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Endpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Endpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
