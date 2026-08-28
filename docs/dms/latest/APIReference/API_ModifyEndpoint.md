---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyEndpoint.html
---

# ModifyEndpoint
<a name="API_ModifyEndpoint"></a>

Modifies the specified endpoint.

**Note**
For a MySQL source or target endpoint, don't explicitly specify the database using the `DatabaseName` request parameter on the `ModifyEndpoint` API call. Specifying `DatabaseName` when you modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the AWS DMS task.

## Request Syntax
<a name="API_ModifyEndpoint_RequestSyntax"></a>

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
   "EndpointArn": "{{string}}",
   "EndpointIdentifier": "{{string}}",
   "EndpointType": "{{string}}",
   "EngineName": "{{string}}",
   "ExactSettings": {{boolean}},
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
<a name="API_ModifyEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CertificateArn](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** [DatabaseName](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-DatabaseName"></a>
The name of the endpoint database. For a MySQL source or target endpoint, do not specify DatabaseName.
Type: String
Required: No

 ** [DmsTransferSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-DmsTransferSettings"></a>
The settings in JSON format for the DMS transfer type of source endpoint.
Attributes include the following:
+ serviceAccessRoleArn - The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the `iam:PassRole` action.
+ BucketName - The name of the S3 bucket to use.
Shorthand syntax for these settings is as follows: `ServiceAccessRoleArn=string ,BucketName=string`
JSON syntax for these settings is as follows: `{ "ServiceAccessRoleArn": "string", "BucketName": "string"} `
Type: [DmsTransferSettings](API_DmsTransferSettings.md) object
Required: No

 ** [DocDbSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-DocDbSettings"></a>
Settings in JSON format for the source DocumentDB endpoint. For more information about the available settings, see the configuration properties section in [ Using DocumentDB as a Target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html) in the * AWS Database Migration Service User Guide.*
Type: [DocDbSettings](API_DocDbSettings.md) object
Required: No

 ** [DynamoDbSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-DynamoDbSettings"></a>
Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see [Using Object Mapping to Migrate Data to DynamoDB](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping) in the * AWS Database Migration Service User Guide.*
Type: [DynamoDbSettings](API_DynamoDbSettings.md) object
Required: No

 ** [ElasticsearchSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-ElasticsearchSettings"></a>
Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see [Extra Connection Attributes When Using OpenSearch as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration) in the * AWS Database Migration Service User Guide.*
Type: [ElasticsearchSettings](API_ElasticsearchSettings.md) object
Required: No

 ** [EndpointArn](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-EndpointArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
Type: String
Required: Yes

 ** [EndpointIdentifier](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-EndpointIdentifier"></a>
The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
Type: String
Required: No

 ** [EndpointType](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-EndpointType"></a>
The type of endpoint. Valid values are `source` and `target`.
Type: String
Valid Values: `source | target`
Required: No

 ** [EngineName](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-EngineName"></a>
The database engine name. Valid values, depending on the EndpointType, include `"mysql"`, `"oracle"`, `"postgres"`, `"mariadb"`, `"aurora"`, `"aurora-postgresql"`, `"redshift"`, `"s3"`, `"db2"`, `"db2-zos"`, `"azuredb"`, `"sybase"`, `"dynamodb"`, `"mongodb"`, `"kinesis"`, `"kafka"`, `"elasticsearch"`, `"documentdb"`, `"sqlserver"`, `"neptune"`, and `"babelfish"`.
Type: String
Required: No

 ** [ExactSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-ExactSettings"></a>
If this attribute is Y, the current call to `ModifyEndpoint` replaces all existing endpoint settings with the exact settings that you specify in this call. If this attribute is N, the current call to `ModifyEndpoint` does two things:
+ It replaces any endpoint settings that already exist with new values, for settings with the same names.
+ It creates new endpoint settings that you specify in the call, for settings with different names.
For example, if you call `create-endpoint ... --endpoint-settings '{"a":1}' ...`, the endpoint has the following endpoint settings: `'{"a":1}'`. If you then call `modify-endpoint ... --endpoint-settings '{"b":2}' ...` for the same endpoint, the endpoint has the following settings: `'{"a":1,"b":2}'`.
However, suppose that you follow this with a call to `modify-endpoint ... --endpoint-settings '{"b":2}' --exact-settings ...` for that same endpoint again. Then the endpoint has the following settings: `'{"b":2}'`. All existing settings are replaced with the exact settings that you specify.
Type: Boolean
Required: No

 ** [ExternalTableDefinition](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-ExternalTableDefinition"></a>
The external table definition.
Type: String
Required: No

 ** [ExtraConnectionAttributes](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-ExtraConnectionAttributes"></a>
Additional attributes associated with the connection. To reset this parameter, pass the empty string ("") as an argument.
Type: String
Required: No

 ** [GcpMySQLSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-GcpMySQLSettings"></a>
Settings in JSON format for the source GCP MySQL endpoint.
Type: [GcpMySQLSettings](API_GcpMySQLSettings.md) object
Required: No

 ** [IBMDb2Settings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-IBMDb2Settings"></a>
Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see [Extra connection attributes when using Db2 LUW as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [IBMDb2Settings](API_IBMDb2Settings.md) object
Required: No

 ** [KafkaSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-KafkaSettings"></a>
Settings in JSON format for the target Apache Kafka endpoint. For more information about the available settings, see [Using object mapping to migrate data to a Kafka topic](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping) in the * AWS Database Migration Service User Guide.*
Type: [KafkaSettings](API_KafkaSettings.md) object
Required: No

 ** [KinesisSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-KinesisSettings"></a>
Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about the available settings, see [Using object mapping to migrate data to a Kinesis data stream](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping) in the * AWS Database Migration Service User Guide.*
Type: [KinesisSettings](API_KinesisSettings.md) object
Required: No

 ** [MicrosoftSQLServerSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-MicrosoftSQLServerSettings"></a>
Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see [Extra connection attributes when using SQL Server as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib) and [ Extra connection attributes when using SQL Server as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [MicrosoftSQLServerSettings](API_MicrosoftSQLServerSettings.md) object
Required: No

 ** [MongoDbSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-MongoDbSettings"></a>
Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see the configuration properties section in [Endpoint configuration settings when using MongoDB as a source for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration) in the * AWS Database Migration Service User Guide.*
Type: [MongoDbSettings](API_MongoDbSettings.md) object
Required: No

 ** [MySQLSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-MySQLSettings"></a>
Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see [Extra connection attributes when using MySQL as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib) and [Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [MySQLSettings](API_MySQLSettings.md) object
Required: No

 ** [NeptuneSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-NeptuneSettings"></a>
Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see [Specifying graph-mapping rules using Gremlin and R2RML for Amazon Neptune as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings) in the * AWS Database Migration Service User Guide.*
Type: [NeptuneSettings](API_NeptuneSettings.md) object
Required: No

 ** [OracleSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-OracleSettings"></a>
Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see [Extra connection attributes when using Oracle as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib) and [ Extra connection attributes when using Oracle as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [OracleSettings](API_OracleSettings.md) object
Required: No

 ** [Password](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-Password"></a>
The password to be used to login to the endpoint database.
Type: String
Required: No

 ** [Port](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-Port"></a>
The port used by the endpoint database.
Type: Integer
Required: No

 ** [PostgreSQLSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-PostgreSQLSettings"></a>
Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see [Extra connection attributes when using PostgreSQL as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib) and [ Extra connection attributes when using PostgreSQL as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [PostgreSQLSettings](API_PostgreSQLSettings.md) object
Required: No

 ** [RedisSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-RedisSettings"></a>
Settings in JSON format for the Redis target endpoint.
Type: [RedisSettings](API_RedisSettings.md) object
Required: No

 ** [RedshiftSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-RedshiftSettings"></a>
Provides information that defines an Amazon Redshift endpoint.
Type: [RedshiftSettings](API_RedshiftSettings.md) object
Required: No

 ** [S3Settings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-S3Settings"></a>
Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see [Extra Connection Attributes When Using Amazon S3 as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring) in the * AWS Database Migration Service User Guide.*
Type: [S3Settings](API_S3Settings.md) object
Required: No

 ** [ServerName](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-ServerName"></a>
The name of the server where the endpoint database resides.
Type: String
Required: No

 ** [ServiceAccessRoleArn](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-ServiceAccessRoleArn"></a>
 The Amazon Resource Name (ARN) for the IAM role you want to use to modify the endpoint. The role must allow the `iam:PassRole` action.
Type: String
Required: No

 ** [SslMode](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-SslMode"></a>
The SSL mode used to connect to the endpoint. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

 ** [SybaseSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-SybaseSettings"></a>
Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see [Extra connection attributes when using SAP ASE as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib) and [Extra connection attributes when using SAP ASE as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib) in the * AWS Database Migration Service User Guide.*
Type: [SybaseSettings](API_SybaseSettings.md) object
Required: No

 ** [TimestreamSettings](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-TimestreamSettings"></a>
Settings in JSON format for the target Amazon Timestream endpoint.
Type: [TimestreamSettings](API_TimestreamSettings.md) object
Required: No

 ** [Username](#API_ModifyEndpoint_RequestSyntax) **   <a name="DMS-ModifyEndpoint-request-Username"></a>
The user name to be used to login to the endpoint database.
Type: String
Required: No

## Response Syntax
<a name="API_ModifyEndpoint_ResponseSyntax"></a>

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
<a name="API_ModifyEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoint](#API_ModifyEndpoint_ResponseSyntax) **   <a name="DMS-ModifyEndpoint-response-Endpoint"></a>
The modified endpoint.
Type: [Endpoint](API_Endpoint.md) object

## Errors
<a name="API_ModifyEndpoint_Errors"></a>

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

## Examples
<a name="API_ModifyEndpoint_Examples"></a>

### Example
<a name="API_ModifyEndpoint_Example_1"></a>

This example illustrates one usage of ModifyEndpoint.

#### Sample Request
<a name="API_ModifyEndpoint_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256
Credential=<Credential>,
SignedHeaders=contenttype;date;host;user-
agent;x-amz-date;x-amz-target;x-amzn-
requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.ModifyEndpoint
{
   "EndpointArn":"arn:aws:dms:us-east-1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM",
   "EndpointIdentifier":"",
   "EndpointType":"target",
   "EngineName":"",
   "Username":"",
   "Password":"",
   "ServerName":"",
   "Port":0,
   "DatabaseName":"",
   "ExtraConnectionAttributes":""
}
```

#### Sample Response
<a name="API_ModifyEndpoint_Example_1_Response"></a>

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
      "ServerName":"apurvap-source.cxln7iyxx1lo.us-west-
2.rds.amazonaws.com",
      "EndpointType":"TARGET",
      "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/4dc17316-5543-
4ded-b1e3-d53a7cfb411d",
      "ExtraConnectionAttributes":"parallelLoadThreads=1",
      "EngineName":"mysql",
      "EndpointIdentifier":"test-endpoint-1",
      "Port":3306
   }
}
```

## See Also
<a name="API_ModifyEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ModifyEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ModifyEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
