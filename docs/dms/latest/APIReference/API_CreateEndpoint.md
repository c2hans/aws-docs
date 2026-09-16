---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateEndpoint.html
---

# CreateEndpoint
<a name="API_CreateEndpoint"></a>

Creates an endpoint using the provided settings.

**Note**
For a MySQL source or target endpoint, don't explicitly specify the database using the `DatabaseName` request parameter on the `CreateEndpoint` API call. Specifying `DatabaseName` when you create a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the AWS DMS task.

## Request Syntax
<a name="API_CreateEndpoint_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}",
   "DatabaseName": "{{string}}",
   "DmsTransferSettings": {
      "BucketName": "{{string}}",
      "ServiceAccessRoleArn": "{{string}}"
   },
   "DocDbSettings": {
      "DatabaseName": "{{string}}",
      "DocsToInvestigate": {{number}},
      "ExtractDocId": {{boolean}},
      "KmsKeyId": "{{string}}",
      "NestingLevel": "{{string}}",
      "Password": "{{string}}",
      "Port": {{number}},
      "ReplicateShardCollections": {{boolean}},
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "Username": "{{string}}",
      "UseUpdateLookUp": {{boolean}}
   },
   "DynamoDbSettings": {
      "ServiceAccessRoleArn": "{{string}}"
   },
   "ElasticsearchSettings": {
      "EndpointUri": "{{string}}",
      "ErrorRetryDuration": {{number}},
      "FullLoadErrorPercentage": {{number}},
      "ServiceAccessRoleArn": "{{string}}",
      "UseNewMappingType": {{boolean}}
   },
   "EndpointIdentifier": "{{string}}",
   "EndpointType": "{{string}}",
   "EngineName": "{{string}}",
   "ExternalTableDefinition": "{{string}}",
   "ExtraConnectionAttributes": "{{string}}",
   "GcpMySQLSettings": {
      "AfterConnectScript": "{{string}}",
      "CleanSourceMetadataOnMismatch": {{boolean}},
      "DatabaseName": "{{string}}",
      "EventsPollInterval": {{number}},
      "MaxFileSize": {{number}},
      "ParallelLoadThreads": {{number}},
      "Password": "{{string}}",
      "Port": {{number}},
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "ServerTimezone": "{{string}}",
      "TargetDbType": "{{string}}",
      "Username": "{{string}}"
   },
   "IBMDb2Settings": {
      "CurrentLsn": "{{string}}",
      "DatabaseName": "{{string}}",
      "KeepCsvFiles": {{boolean}},
      "LoadTimeout": {{number}},
      "MaxFileSize": {{number}},
      "MaxKBytesPerRead": {{number}},
      "Password": "{{string}}",
      "Port": {{number}},
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "SetDataCaptureChanges": {{boolean}},
      "Username": "{{string}}",
      "WriteBufferSize": {{number}}
   },
   "KafkaSettings": {
      "Broker": "{{string}}",
      "IncludeControlDetails": {{boolean}},
      "IncludeNullAndEmpty": {{boolean}},
      "IncludePartitionValue": {{boolean}},
      "IncludeTableAlterOperations": {{boolean}},
      "IncludeTransactionDetails": {{boolean}},
      "MessageFormat": "{{string}}",
      "MessageMaxBytes": {{number}},
      "NoHexPrefix": {{boolean}},
      "PartitionIncludeSchemaTable": {{boolean}},
      "SaslMechanism": "{{string}}",
      "SaslPassword": "{{string}}",
      "SaslUsername": "{{string}}",
      "SecurityProtocol": "{{string}}",
      "SslCaCertificateArn": "{{string}}",
      "SslClientCertificateArn": "{{string}}",
      "SslClientKeyArn": "{{string}}",
      "SslClientKeyPassword": "{{string}}",
      "SslEndpointIdentificationAlgorithm": "{{string}}",
      "Topic": "{{string}}",
      "UseLargeIntegerValue": {{boolean}}
   },
   "KinesisSettings": {
      "IncludeControlDetails": {{boolean}},
      "IncludeNullAndEmpty": {{boolean}},
      "IncludePartitionValue": {{boolean}},
      "IncludeTableAlterOperations": {{boolean}},
      "IncludeTransactionDetails": {{boolean}},
      "MessageFormat": "{{string}}",
      "NoHexPrefix": {{boolean}},
      "PartitionIncludeSchemaTable": {{boolean}},
      "ServiceAccessRoleArn": "{{string}}",
      "StreamArn": "{{string}}",
      "UseLargeIntegerValue": {{boolean}}
   },
   "KmsKeyId": "{{string}}",
   "MicrosoftSQLServerSettings": {
      "AuthenticationMethod": "{{string}}",
      "BcpPacketSize": {{number}},
      "ControlTablesFileGroup": "{{string}}",
      "DatabaseName": "{{string}}",
      "ForceLobLookup": {{boolean}},
      "Password": "{{string}}",
      "Port": {{number}},
      "QuerySingleAlwaysOnNode": {{boolean}},
      "ReadBackupOnly": {{boolean}},
      "SafeguardPolicy": "{{string}}",
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "TlogAccessMode": "{{string}}",
      "TrimSpaceInChar": {{boolean}},
      "UseBcpFullLoad": {{boolean}},
      "Username": "{{string}}",
      "UseThirdPartyBackupDevice": {{boolean}}
   },
   "MongoDbSettings": {
      "AuthMechanism": "{{string}}",
      "AuthSource": "{{string}}",
      "AuthType": "{{string}}",
      "DatabaseName": "{{string}}",
      "DocsToInvestigate": "{{string}}",
      "ExtractDocId": "{{string}}",
      "KmsKeyId": "{{string}}",
      "NestingLevel": "{{string}}",
      "Password": "{{string}}",
      "Port": {{number}},
      "ReplicateShardCollections": {{boolean}},
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "Username": "{{string}}",
      "UseUpdateLookUp": {{boolean}}
   },
   "MySQLSettings": {
      "AfterConnectScript": "{{string}}",
      "AuthenticationMethod": "{{string}}",
      "CleanSourceMetadataOnMismatch": {{boolean}},
      "DatabaseName": "{{string}}",
      "EventsPollInterval": {{number}},
      "ExecuteTimeout": {{number}},
      "MaxFileSize": {{number}},
      "ParallelLoadThreads": {{number}},
      "Password": "{{string}}",
      "Port": {{number}},
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "ServerTimezone": "{{string}}",
      "ServiceAccessRoleArn": "{{string}}",
      "TargetDbType": "{{string}}",
      "Username": "{{string}}"
   },
   "NeptuneSettings": {
      "ErrorRetryDuration": {{number}},
      "IamAuthEnabled": {{boolean}},
      "MaxFileSize": {{number}},
      "MaxRetryCount": {{number}},
      "S3BucketFolder": "{{string}}",
      "S3BucketName": "{{string}}",
      "ServiceAccessRoleArn": "{{string}}"
   },
   "OracleSettings": {
      "AccessAlternateDirectly": {{boolean}},
      "AdditionalArchivedLogDestId": {{number}},
      "AddSupplementalLogging": {{boolean}},
      "AllowSelectNestedTables": {{boolean}},
      "ArchivedLogDestId": {{number}},
      "ArchivedLogsOnly": {{boolean}},
      "AsmPassword": "{{string}}",
      "AsmServer": "{{string}}",
      "AsmUser": "{{string}}",
      "AuthenticationMethod": "{{string}}",
      "CharLengthSemantics": "{{string}}",
      "ConvertTimestampWithZoneToUTC": {{boolean}},
      "DatabaseName": "{{string}}",
      "DirectPathNoLog": {{boolean}},
      "DirectPathParallelLoad": {{boolean}},
      "EnableHomogenousTablespace": {{boolean}},
      "ExtraArchivedLogDestIds": [ {{number}} ],
      "FailTasksOnLobTruncation": {{boolean}},
      "NumberDatatypeScale": {{number}},
      "OpenTransactionWindow": {{number}},
      "OraclePathPrefix": "{{string}}",
      "ParallelAsmReadThreads": {{number}},
      "Password": "{{string}}",
      "Port": {{number}},
      "ReadAheadBlocks": {{number}},
      "ReadTableSpaceName": {{boolean}},
      "ReplacePathPrefix": {{boolean}},
      "RetryInterval": {{number}},
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerOracleAsmAccessRoleArn": "{{string}}",
      "SecretsManagerOracleAsmSecretId": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "SecurityDbEncryption": "{{string}}",
      "SecurityDbEncryptionName": "{{string}}",
      "ServerName": "{{string}}",
      "SpatialDataOptionToGeoJsonFunctionName": "{{string}}",
      "StandbyDelayTime": {{number}},
      "TrimSpaceInChar": {{boolean}},
      "UseAlternateFolderForOnline": {{boolean}},
      "UseBFile": {{boolean}},
      "UseDirectPathFullLoad": {{boolean}},
      "UseLogminerReader": {{boolean}},
      "UsePathPrefix": "{{string}}",
      "Username": "{{string}}"
   },
   "Password": "{{string}}",
   "Port": {{number}},
   "PostgreSQLSettings": {
      "AfterConnectScript": "{{string}}",
      "AuthenticationMethod": "{{string}}",
      "BabelfishDatabaseName": "{{string}}",
      "CaptureDdls": {{boolean}},
      "DatabaseMode": "{{string}}",
      "DatabaseName": "{{string}}",
      "DdlArtifactsSchema": "{{string}}",
      "DisableUnicodeSourceFilter": {{boolean}},
      "ExecuteTimeout": {{number}},
      "FailTasksOnLobTruncation": {{boolean}},
      "HeartbeatEnable": {{boolean}},
      "HeartbeatFrequency": {{number}},
      "HeartbeatSchema": "{{string}}",
      "MapBooleanAsBoolean": {{boolean}},
      "MapJsonbAsClob": {{boolean}},
      "MapLongVarcharAs": "{{string}}",
      "MaxFileSize": {{number}},
      "Password": "{{string}}",
      "PluginName": "{{string}}",
      "Port": {{number}},
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "ServiceAccessRoleArn": "{{string}}",
      "SlotName": "{{string}}",
      "TrimSpaceInChar": {{boolean}},
      "Username": "{{string}}"
   },
   "RedisSettings": {
      "AuthPassword": "{{string}}",
      "AuthType": "{{string}}",
      "AuthUserName": "{{string}}",
      "Port": {{number}},
      "ServerName": "{{string}}",
      "SslCaCertificateArn": "{{string}}",
      "SslSecurityProtocol": "{{string}}"
   },
   "RedshiftSettings": {
      "AcceptAnyDate": {{boolean}},
      "AfterConnectScript": "{{string}}",
      "BucketFolder": "{{string}}",
      "BucketName": "{{string}}",
      "CaseSensitiveNames": {{boolean}},
      "CompUpdate": {{boolean}},
      "ConnectionTimeout": {{number}},
      "DatabaseName": "{{string}}",
      "DateFormat": "{{string}}",
      "EmptyAsNull": {{boolean}},
      "EncryptionMode": "{{string}}",
      "ExplicitIds": {{boolean}},
      "FileTransferUploadStreams": {{number}},
      "LoadTimeout": {{number}},
      "MapBooleanAsBoolean": {{boolean}},
      "MaxFileSize": {{number}},
      "Password": "{{string}}",
      "Port": {{number}},
      "RemoveQuotes": {{boolean}},
      "ReplaceChars": "{{string}}",
      "ReplaceInvalidChars": "{{string}}",
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "ServerSideEncryptionKmsKeyId": "{{string}}",
      "ServiceAccessRoleArn": "{{string}}",
      "TimeFormat": "{{string}}",
      "TrimBlanks": {{boolean}},
      "TruncateColumns": {{boolean}},
      "Username": "{{string}}",
      "WriteBufferSize": {{number}}
   },
   "ResourceIdentifier": "{{string}}",
   "S3Settings": {
      "AddColumnName": {{boolean}},
      "AddTrailingPaddingCharacter": {{boolean}},
      "BucketFolder": "{{string}}",
      "BucketName": "{{string}}",
      "CannedAclForObjects": "{{string}}",
      "CdcInsertsAndUpdates": {{boolean}},
      "CdcInsertsOnly": {{boolean}},
      "CdcMaxBatchInterval": {{number}},
      "CdcMinFileSize": {{number}},
      "CdcPath": "{{string}}",
      "CompressionType": "{{string}}",
      "CsvDelimiter": "{{string}}",
      "CsvNoSupValue": "{{string}}",
      "CsvNullValue": "{{string}}",
      "CsvRowDelimiter": "{{string}}",
      "DataFormat": "{{string}}",
      "DataPageSize": {{number}},
      "DatePartitionDelimiter": "{{string}}",
      "DatePartitionEnabled": {{boolean}},
      "DatePartitionSequence": "{{string}}",
      "DatePartitionTimezone": "{{string}}",
      "DictPageSizeLimit": {{number}},
      "EnableStatistics": {{boolean}},
      "EncodingType": "{{string}}",
      "EncryptionMode": "{{string}}",
      "ExpectedBucketOwner": "{{string}}",
      "ExternalTableDefinition": "{{string}}",
      "GlueCatalogGeneration": {{boolean}},
      "IgnoreHeaderRows": {{number}},
      "IncludeOpForFullLoad": {{boolean}},
      "MaxFileSize": {{number}},
      "ParquetTimestampInMillisecond": {{boolean}},
      "ParquetVersion": "{{string}}",
      "PreserveTransactions": {{boolean}},
      "Rfc4180": {{boolean}},
      "RowGroupLength": {{number}},
      "ServerSideEncryptionKmsKeyId": "{{string}}",
      "ServiceAccessRoleArn": "{{string}}",
      "TimestampColumnName": "{{string}}",
      "UseCsvNoSupValue": {{boolean}},
      "UseTaskStartTimeForFullLoadTimestamp": {{boolean}}
   },
   "ServerName": "{{string}}",
   "ServiceAccessRoleArn": "{{string}}",
   "SslMode": "{{string}}",
   "SybaseSettings": {
      "DatabaseName": "{{string}}",
      "Password": "{{string}}",
      "Port": {{number}},
      "SecretsManagerAccessRoleArn": "{{string}}",
      "SecretsManagerSecretId": "{{string}}",
      "ServerName": "{{string}}",
      "Username": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TimestreamSettings": {
      "CdcInsertsAndUpdates": {{boolean}},
      "DatabaseName": "{{string}}",
      "EnableMagneticStoreWrites": {{boolean}},
      "MagneticDuration": {{number}},
      "MemoryDuration": {{number}}
   },
   "Username": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateArn](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-CertificateArn"></a>
The Amazon Resource Name (ARN) for the certificate.
Type: String
Required: No

 ** [DatabaseName](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-DatabaseName"></a>
The name of the endpoint database. For a MySQL source or target endpoint, do not specify DatabaseName. To migrate to a specific database, use this setting and `targetDbType`.
Type: String
Required: No

 ** [DmsTransferSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-DmsTransferSettings"></a>
The settings in JSON format for the DMS transfer type of source endpoint.
Possible settings include the following:
+  `ServiceAccessRoleArn` - The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the `iam:PassRole` action.
+  `BucketName` - The name of the S3 bucket to use.
Shorthand syntax for these settings is as follows: `ServiceAccessRoleArn=string,BucketName=string`
JSON syntax for these settings is as follows: `{ "ServiceAccessRoleArn": "string", "BucketName": "string", } `
Type: [DmsTransferSettings](API_DmsTransferSettings.md) object
Required: No

 ** [DocDbSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-DocDbSettings"></a>
Provides information that defines a DocumentDB endpoint.
Type: [DocDbSettings](API_DocDbSettings.md) object
Required: No

 ** [DynamoDbSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-DynamoDbSettings"></a>
Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see [Using Object Mapping to Migrate Data to DynamoDB](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping) in the * AWS Database Migration Service User Guide.*
Type: [DynamoDbSettings](API_DynamoDbSettings.md) object
Required: No

 ** [ElasticsearchSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-ElasticsearchSettings"></a>
Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see [Extra Connection Attributes When Using OpenSearch as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration) in the * AWS Database Migration Service User Guide*.
Type: [ElasticsearchSettings](API_ElasticsearchSettings.md) object
Required: No

 ** [EndpointIdentifier](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-EndpointIdentifier"></a>
The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
Type: String
Required: Yes

 ** [EndpointType](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-EndpointType"></a>
The type of endpoint. Valid values are `source` and `target`.
Type: String
Valid Values: `source | target`
Required: Yes

 ** [EngineName](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-EngineName"></a>
The type of engine for the endpoint. Valid values, depending on the `EndpointType` value, include `"mysql"`, `"oracle"`, `"postgres"`, `"mariadb"`, `"aurora"`, `"aurora-postgresql"`, `"opensearch"`, `"redshift"`, `"s3"`, `"db2"`, `"db2-zos"`, `"azuredb"`, `"sybase"`, `"dynamodb"`, `"mongodb"`, `"kinesis"`, `"kafka"`, `"elasticsearch"`, `"docdb"`, `"sqlserver"`, `"neptune"`, `"babelfish"`, `redshift-serverless`, `aurora-serverless`, `aurora-postgresql-serverless`, `gcp-mysql`, `azure-sql-managed-instance`, `redis`, `dms-transfer`.
Type: String
Required: Yes

 ** [ExternalTableDefinition](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-ExternalTableDefinition"></a>
The external table definition.
Type: String
Required: No

 ** [ExtraConnectionAttributes](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-ExtraConnectionAttributes"></a>
Additional attributes associated with the connection. Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see [Working with AWS DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html) in the * AWS Database Migration Service User Guide.*
Type: String
Required: No

 ** [GcpMySQLSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-GcpMySQLSettings"></a>
Settings in JSON format for the source GCP MySQL endpoint.
Type: [GcpMySQLSettings](API_GcpMySQLSettings.md) object
Required: No

 ** [IBMDb2Settings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-IBMDb2Settings"></a>
Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see [Extra connection attributes when using Db2 LUW as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [IBMDb2Settings](API_IBMDb2Settings.md) object
Required: No

 ** [KafkaSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-KafkaSettings"></a>
Settings in JSON format for the target Apache Kafka endpoint. For more information about the available settings, see [Using object mapping to migrate data to a Kafka topic](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping) in the * AWS Database Migration Service User Guide.*
Type: [KafkaSettings](API_KafkaSettings.md) object
Required: No

 ** [KinesisSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-KinesisSettings"></a>
Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about the available settings, see [Using object mapping to migrate data to a Kinesis data stream](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping) in the * AWS Database Migration Service User Guide.*
Type: [KinesisSettings](API_KinesisSettings.md) object
Required: No

 ** [KmsKeyId](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-KmsKeyId"></a>
An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.
If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key.
 AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** [MicrosoftSQLServerSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-MicrosoftSQLServerSettings"></a>
Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see [Extra connection attributes when using SQL Server as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib) and [ Extra connection attributes when using SQL Server as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [MicrosoftSQLServerSettings](API_MicrosoftSQLServerSettings.md) object
Required: No

 ** [MongoDbSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-MongoDbSettings"></a>
Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see [Endpoint configuration settings when using MongoDB as a source for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration) in the * AWS Database Migration Service User Guide.*
Type: [MongoDbSettings](API_MongoDbSettings.md) object
Required: No

 ** [MySQLSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-MySQLSettings"></a>
Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see [Extra connection attributes when using MySQL as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib) and [Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [MySQLSettings](API_MySQLSettings.md) object
Required: No

 ** [NeptuneSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-NeptuneSettings"></a>
Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see [Specifying graph-mapping rules using Gremlin and R2RML for Amazon Neptune as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings) in the * AWS Database Migration Service User Guide.*
Type: [NeptuneSettings](API_NeptuneSettings.md) object
Required: No

 ** [OracleSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-OracleSettings"></a>
Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see [Extra connection attributes when using Oracle as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib) and [ Extra connection attributes when using Oracle as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [OracleSettings](API_OracleSettings.md) object
Required: No

 ** [Password](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-Password"></a>
The password to be used to log in to the endpoint database.
Type: String
Required: No

 ** [Port](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-Port"></a>
The port used by the endpoint database.
Type: Integer
Required: No

 ** [PostgreSQLSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-PostgreSQLSettings"></a>
Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see [Extra connection attributes when using PostgreSQL as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib) and [ Extra connection attributes when using PostgreSQL as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [PostgreSQLSettings](API_PostgreSQLSettings.md) object
Required: No

 ** [RedisSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-RedisSettings"></a>
Settings in JSON format for the target Redis endpoint.
Type: [RedisSettings](API_RedisSettings.md) object
Required: No

 ** [RedshiftSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-RedshiftSettings"></a>
Provides information that defines an Amazon Redshift endpoint.
Type: [RedshiftSettings](API_RedshiftSettings.md) object
Required: No

 ** [ResourceIdentifier](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-ResourceIdentifier"></a>
A friendly name for the resource identifier at the end of the `EndpointArn` response parameter that is returned in the created `Endpoint` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as `Example-App-ARN1`. For example, this value might result in the `EndpointArn` value `arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`. If you don't specify a `ResourceIdentifier` value, AWS DMS generates a default identifier value for the end of `EndpointArn`.
Type: String
Required: No

 ** [S3Settings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-S3Settings"></a>
Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see [Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring) in the * AWS Database Migration Service User Guide.*
Type: [S3Settings](API_S3Settings.md) object
Required: No

 ** [ServerName](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-ServerName"></a>
The name of the server where the endpoint database resides.
Type: String
Required: No

 ** [ServiceAccessRoleArn](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-ServiceAccessRoleArn"></a>
 The Amazon Resource Name (ARN) for the service access role that you want to use to create the endpoint. The role must allow the `iam:PassRole` action.
Type: String
Required: No

 ** [SslMode](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-SslMode"></a>
The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is `none`
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

 ** [SybaseSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-SybaseSettings"></a>
Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see [Extra connection attributes when using SAP ASE as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib) and [Extra connection attributes when using SAP ASE as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [SybaseSettings](API_SybaseSettings.md) object
Required: No

 ** [Tags](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-Tags"></a>
One or more tags to be assigned to the endpoint.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [TimestreamSettings](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-TimestreamSettings"></a>
Settings in JSON format for the target Amazon Timestream endpoint.
Type: [TimestreamSettings](API_TimestreamSettings.md) object
Required: No

 ** [Username](#API_CreateEndpoint_RequestSyntax) **   <a name="DMS-CreateEndpoint-request-Username"></a>
The user name to be used to log in to the endpoint database.
Type: String
Required: No

## Response Syntax
<a name="API_CreateEndpoint_ResponseSyntax"></a>

```
{
   "Endpoint": {
      "CertificateArn": "string",
      "DatabaseName": "string",
      "DmsTransferSettings": {
         "BucketName": "string",
         "ServiceAccessRoleArn": "string"
      },
      "DocDbSettings": {
         "DatabaseName": "string",
         "DocsToInvestigate": number,
         "ExtractDocId": boolean,
         "KmsKeyId": "string",
         "NestingLevel": "string",
         "Password": "string",
         "Port": number,
         "ReplicateShardCollections": boolean,
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "Username": "string",
         "UseUpdateLookUp": boolean
      },
      "DynamoDbSettings": {
         "ServiceAccessRoleArn": "string"
      },
      "ElasticsearchSettings": {
         "EndpointUri": "string",
         "ErrorRetryDuration": number,
         "FullLoadErrorPercentage": number,
         "ServiceAccessRoleArn": "string",
         "UseNewMappingType": boolean
      },
      "EndpointArn": "string",
      "EndpointIdentifier": "string",
      "EndpointType": "string",
      "EngineDisplayName": "string",
      "EngineName": "string",
      "ExternalId": "string",
      "ExternalTableDefinition": "string",
      "ExtraConnectionAttributes": "string",
      "GcpMySQLSettings": {
         "AfterConnectScript": "string",
         "CleanSourceMetadataOnMismatch": boolean,
         "DatabaseName": "string",
         "EventsPollInterval": number,
         "MaxFileSize": number,
         "ParallelLoadThreads": number,
         "Password": "string",
         "Port": number,
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "ServerTimezone": "string",
         "TargetDbType": "string",
         "Username": "string"
      },
      "IBMDb2Settings": {
         "CurrentLsn": "string",
         "DatabaseName": "string",
         "KeepCsvFiles": boolean,
         "LoadTimeout": number,
         "MaxFileSize": number,
         "MaxKBytesPerRead": number,
         "Password": "string",
         "Port": number,
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "SetDataCaptureChanges": boolean,
         "Username": "string",
         "WriteBufferSize": number
      },
      "IsReadOnly": boolean,
      "KafkaSettings": {
         "Broker": "string",
         "IncludeControlDetails": boolean,
         "IncludeNullAndEmpty": boolean,
         "IncludePartitionValue": boolean,
         "IncludeTableAlterOperations": boolean,
         "IncludeTransactionDetails": boolean,
         "MessageFormat": "string",
         "MessageMaxBytes": number,
         "NoHexPrefix": boolean,
         "PartitionIncludeSchemaTable": boolean,
         "SaslMechanism": "string",
         "SaslPassword": "string",
         "SaslUsername": "string",
         "SecurityProtocol": "string",
         "SslCaCertificateArn": "string",
         "SslClientCertificateArn": "string",
         "SslClientKeyArn": "string",
         "SslClientKeyPassword": "string",
         "SslEndpointIdentificationAlgorithm": "string",
         "Topic": "string",
         "UseLargeIntegerValue": boolean
      },
      "KinesisSettings": {
         "IncludeControlDetails": boolean,
         "IncludeNullAndEmpty": boolean,
         "IncludePartitionValue": boolean,
         "IncludeTableAlterOperations": boolean,
         "IncludeTransactionDetails": boolean,
         "MessageFormat": "string",
         "NoHexPrefix": boolean,
         "PartitionIncludeSchemaTable": boolean,
         "ServiceAccessRoleArn": "string",
         "StreamArn": "string",
         "UseLargeIntegerValue": boolean
      },
      "KmsKeyId": "string",
      "LakehouseSettings": {
         "Arn": "string"
      },
      "MicrosoftSQLServerSettings": {
         "AuthenticationMethod": "string",
         "BcpPacketSize": number,
         "ControlTablesFileGroup": "string",
         "DatabaseName": "string",
         "ForceLobLookup": boolean,
         "Password": "string",
         "Port": number,
         "QuerySingleAlwaysOnNode": boolean,
         "ReadBackupOnly": boolean,
         "SafeguardPolicy": "string",
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "TlogAccessMode": "string",
         "TrimSpaceInChar": boolean,
         "UseBcpFullLoad": boolean,
         "Username": "string",
         "UseThirdPartyBackupDevice": boolean
      },
      "MongoDbSettings": {
         "AuthMechanism": "string",
         "AuthSource": "string",
         "AuthType": "string",
         "DatabaseName": "string",
         "DocsToInvestigate": "string",
         "ExtractDocId": "string",
         "KmsKeyId": "string",
         "NestingLevel": "string",
         "Password": "string",
         "Port": number,
         "ReplicateShardCollections": boolean,
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "Username": "string",
         "UseUpdateLookUp": boolean
      },
      "MySQLSettings": {
         "AfterConnectScript": "string",
         "AuthenticationMethod": "string",
         "CleanSourceMetadataOnMismatch": boolean,
         "DatabaseName": "string",
         "EventsPollInterval": number,
         "ExecuteTimeout": number,
         "MaxFileSize": number,
         "ParallelLoadThreads": number,
         "Password": "string",
         "Port": number,
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "ServerTimezone": "string",
         "ServiceAccessRoleArn": "string",
         "TargetDbType": "string",
         "Username": "string"
      },
      "NeptuneSettings": {
         "ErrorRetryDuration": number,
         "IamAuthEnabled": boolean,
         "MaxFileSize": number,
         "MaxRetryCount": number,
         "S3BucketFolder": "string",
         "S3BucketName": "string",
         "ServiceAccessRoleArn": "string"
      },
      "OracleSettings": {
         "AccessAlternateDirectly": boolean,
         "AdditionalArchivedLogDestId": number,
         "AddSupplementalLogging": boolean,
         "AllowSelectNestedTables": boolean,
         "ArchivedLogDestId": number,
         "ArchivedLogsOnly": boolean,
         "AsmPassword": "string",
         "AsmServer": "string",
         "AsmUser": "string",
         "AuthenticationMethod": "string",
         "CharLengthSemantics": "string",
         "ConvertTimestampWithZoneToUTC": boolean,
         "DatabaseName": "string",
         "DirectPathNoLog": boolean,
         "DirectPathParallelLoad": boolean,
         "EnableHomogenousTablespace": boolean,
         "ExtraArchivedLogDestIds": [ number ],
         "FailTasksOnLobTruncation": boolean,
         "NumberDatatypeScale": number,
         "OpenTransactionWindow": number,
         "OraclePathPrefix": "string",
         "ParallelAsmReadThreads": number,
         "Password": "string",
         "Port": number,
         "ReadAheadBlocks": number,
         "ReadTableSpaceName": boolean,
         "ReplacePathPrefix": boolean,
         "RetryInterval": number,
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerOracleAsmAccessRoleArn": "string",
         "SecretsManagerOracleAsmSecretId": "string",
         "SecretsManagerSecretId": "string",
         "SecurityDbEncryption": "string",
         "SecurityDbEncryptionName": "string",
         "ServerName": "string",
         "SpatialDataOptionToGeoJsonFunctionName": "string",
         "StandbyDelayTime": number,
         "TrimSpaceInChar": boolean,
         "UseAlternateFolderForOnline": boolean,
         "UseBFile": boolean,
         "UseDirectPathFullLoad": boolean,
         "UseLogminerReader": boolean,
         "UsePathPrefix": "string",
         "Username": "string"
      },
      "Port": number,
      "PostgreSQLSettings": {
         "AfterConnectScript": "string",
         "AuthenticationMethod": "string",
         "BabelfishDatabaseName": "string",
         "CaptureDdls": boolean,
         "DatabaseMode": "string",
         "DatabaseName": "string",
         "DdlArtifactsSchema": "string",
         "DisableUnicodeSourceFilter": boolean,
         "ExecuteTimeout": number,
         "FailTasksOnLobTruncation": boolean,
         "HeartbeatEnable": boolean,
         "HeartbeatFrequency": number,
         "HeartbeatSchema": "string",
         "MapBooleanAsBoolean": boolean,
         "MapJsonbAsClob": boolean,
         "MapLongVarcharAs": "string",
         "MaxFileSize": number,
         "Password": "string",
         "PluginName": "string",
         "Port": number,
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "ServiceAccessRoleArn": "string",
         "SlotName": "string",
         "TrimSpaceInChar": boolean,
         "Username": "string"
      },
      "RedisSettings": {
         "AuthPassword": "string",
         "AuthType": "string",
         "AuthUserName": "string",
         "Port": number,
         "ServerName": "string",
         "SslCaCertificateArn": "string",
         "SslSecurityProtocol": "string"
      },
      "RedshiftSettings": {
         "AcceptAnyDate": boolean,
         "AfterConnectScript": "string",
         "BucketFolder": "string",
         "BucketName": "string",
         "CaseSensitiveNames": boolean,
         "CompUpdate": boolean,
         "ConnectionTimeout": number,
         "DatabaseName": "string",
         "DateFormat": "string",
         "EmptyAsNull": boolean,
         "EncryptionMode": "string",
         "ExplicitIds": boolean,
         "FileTransferUploadStreams": number,
         "LoadTimeout": number,
         "MapBooleanAsBoolean": boolean,
         "MaxFileSize": number,
         "Password": "string",
         "Port": number,
         "RemoveQuotes": boolean,
         "ReplaceChars": "string",
         "ReplaceInvalidChars": "string",
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "ServerSideEncryptionKmsKeyId": "string",
         "ServiceAccessRoleArn": "string",
         "TimeFormat": "string",
         "TrimBlanks": boolean,
         "TruncateColumns": boolean,
         "Username": "string",
         "WriteBufferSize": number
      },
      "S3Settings": {
         "AddColumnName": boolean,
         "AddTrailingPaddingCharacter": boolean,
         "BucketFolder": "string",
         "BucketName": "string",
         "CannedAclForObjects": "string",
         "CdcInsertsAndUpdates": boolean,
         "CdcInsertsOnly": boolean,
         "CdcMaxBatchInterval": number,
         "CdcMinFileSize": number,
         "CdcPath": "string",
         "CompressionType": "string",
         "CsvDelimiter": "string",
         "CsvNoSupValue": "string",
         "CsvNullValue": "string",
         "CsvRowDelimiter": "string",
         "DataFormat": "string",
         "DataPageSize": number,
         "DatePartitionDelimiter": "string",
         "DatePartitionEnabled": boolean,
         "DatePartitionSequence": "string",
         "DatePartitionTimezone": "string",
         "DictPageSizeLimit": number,
         "EnableStatistics": boolean,
         "EncodingType": "string",
         "EncryptionMode": "string",
         "ExpectedBucketOwner": "string",
         "ExternalTableDefinition": "string",
         "GlueCatalogGeneration": boolean,
         "IgnoreHeaderRows": number,
         "IncludeOpForFullLoad": boolean,
         "MaxFileSize": number,
         "ParquetTimestampInMillisecond": boolean,
         "ParquetVersion": "string",
         "PreserveTransactions": boolean,
         "Rfc4180": boolean,
         "RowGroupLength": number,
         "ServerSideEncryptionKmsKeyId": "string",
         "ServiceAccessRoleArn": "string",
         "TimestampColumnName": "string",
         "UseCsvNoSupValue": boolean,
         "UseTaskStartTimeForFullLoadTimestamp": boolean
      },
      "ServerName": "string",
      "ServiceAccessRoleArn": "string",
      "SslMode": "string",
      "Status": "string",
      "SybaseSettings": {
         "DatabaseName": "string",
         "Password": "string",
         "Port": number,
         "SecretsManagerAccessRoleArn": "string",
         "SecretsManagerSecretId": "string",
         "ServerName": "string",
         "Username": "string"
      },
      "TimestreamSettings": {
         "CdcInsertsAndUpdates": boolean,
         "DatabaseName": "string",
         "EnableMagneticStoreWrites": boolean,
         "MagneticDuration": number,
         "MemoryDuration": number
      },
      "Username": "string"
   }
}
```

## Response Elements
<a name="API_CreateEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoint](#API_CreateEndpoint_ResponseSyntax) **   <a name="DMS-CreateEndpoint-response-Endpoint"></a>
The endpoint that was created.
Type: [Endpoint](API_Endpoint.md) object

## Errors
<a name="API_CreateEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
 AWS DMS cannot access the KMS key.
 ** message **

HTTP Status Code: 400

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

 ** S3AccessDeniedFault **
Insufficient privileges are preventing access to an Amazon S3 object.
HTTP Status Code: 400

## Examples
<a name="API_CreateEndpoint_Examples"></a>

### Example
<a name="API_CreateEndpoint_Example_1"></a>

This example illustrates one usage of CreateEndpoint.

#### Sample Request
<a name="API_CreateEndpoint_Example_1_Request"></a>

```
      POST / HTTP/1.1
      Host: dms.<region>.<domain>
       x-amz-Date: <Date>
        Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
         User-Agent: <UserAgentString>
          Content-Type: application/x-amz-json-1.1
          Content-Length: <PayloadSizeBytes>
           Connection: Keep-Alive
           X-Amz-Target: AmazonDMSv20160101.CreateEndpoint
{
   "EndpointIdentifier":"test-endpoint-1",
           "   EndpointType":"source",
           "   EngineName":"mysql",
   "Username":"username",
   "Password":"password",
   "ServerName":"test-source.cxln7iyxx1lo.us-west-2.rds.amazonaws.com",
           "   Port":3306,
   "DatabaseName":"",
   "ExtraConnectionAttributes":"",
   "KmsKeyId":"",
   "Tags":[
      {
         "Key":"",
         "Value":""
      }
   ]
}
```

#### Sample Response
<a name="API_CreateEndpoint_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "Endpoint":{
      "Username":"username",
      "Status":"active",
      "EndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM",
      "ServerName":"test-source.cxln7iyxx1lo.us-west-2.rds.amazonaws.com",
      "EndpointType":"SOURCE",
      "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/4dc17316-5543-
4ded-b1e3-d53a7cfb411d",
      "EngineName":"mysql",
      "EndpointIdentifier":"test-endpoint-1",
      "Port":3306
   }
}
```

## See Also
<a name="API_CreateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateEndpoint)
