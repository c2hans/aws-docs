---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteEndpoint.html
---

# DeleteEndpoint
<a name="API_DeleteEndpoint"></a>

Deletes the specified endpoint.

**Note**
All tasks associated with the endpoint must be deleted before you can delete the endpoint.

## Request Syntax
<a name="API_DeleteEndpoint_RequestSyntax"></a>

```
{
   "EndpointArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndpointArn](#API_DeleteEndpoint_RequestSyntax) **   <a name="DMS-DeleteEndpoint-request-EndpointArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteEndpoint_ResponseSyntax"></a>

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
<a name="API_DeleteEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoint](#API_DeleteEndpoint_ResponseSyntax) **   <a name="DMS-DeleteEndpoint-response-Endpoint"></a>
The endpoint that was deleted.
Type: [Endpoint](API_Endpoint.md) object

## Errors
<a name="API_DeleteEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DeleteEndpoint_Examples"></a>

### Example
<a name="API_DeleteEndpoint_Example_1"></a>

This example illustrates one usage of DeleteEndpoint.

#### Sample Request
<a name="API_DeleteEndpoint_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.DeleteEndpoint
{
"EndpointArn": "arn:aws:dms:us-east-
1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM"
}
```

#### Sample Response
<a name="API_DeleteEndpoint_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "Endpoint":{
      "Username":"username",
      "Status":"deleting",
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
<a name="API_DeleteEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DeleteEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DeleteEndpoint)
