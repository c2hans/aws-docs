---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEndpoints.html
---

# DescribeEndpoints
<a name="API_DescribeEndpoints"></a>

Returns information about the endpoints for your account in the current region.

## Request Syntax
<a name="API_DescribeEndpoints_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeEndpoints_RequestSyntax) **   <a name="DMS-DescribeEndpoints-request-Filters"></a>
Filters applied to the endpoints.
Valid filter names: endpoint-arn \| endpoint-type \| endpoint-id \| engine-name
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeEndpoints_RequestSyntax) **   <a name="DMS-DescribeEndpoints-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeEndpoints_RequestSyntax) **   <a name="DMS-DescribeEndpoints-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeEndpoints_ResponseSyntax"></a>

```
{
   "Endpoints": [
      {
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
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoints](#API_DescribeEndpoints_ResponseSyntax) **   <a name="DMS-DescribeEndpoints-response-Endpoints"></a>
Endpoint description.
Type: Array of [Endpoint](API_Endpoint.md) objects

 ** [Marker](#API_DescribeEndpoints_ResponseSyntax) **   <a name="DMS-DescribeEndpoints-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

## Errors
<a name="API_DescribeEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeEndpoints_Examples"></a>

### Example
<a name="API_DescribeEndpoints_Example_1"></a>

This example illustrates one usage of DescribeEndpoints.

#### Sample Request
<a name="API_DescribeEndpoints_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeEndpoints
{
   "Filters":[
      {
         "Name":"endpoint-type",
         "Values":[
            "source"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeEndpoints_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "Endpoints":[
      {
         "Username":"dms",
         "Status":"active",
         "EndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:SFLP3SJIHID2WOFLWY2OKWKVEE",
         "ServerName":"ec2-52-32-48-61.us-west-2.compute.amazonaws.com",
         "EndpointType":"SOURCE",
         "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/945c4e7d-
4ec4-44be-b58a-c8a7adf57dcd",
         "DatabaseName":"sbtest",
         "EngineName":"mysql",
         "EndpointIdentifier":"pri100",
         "Port":8193
      },
      {
         "Username":"admin",
         "Status":"active",
         "EndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:TJTJ2JZCIH3CWFR4VC32WEJRU4",
         "ServerName":"test.oracle.com",
         "EndpointType":"SOURCE",
         "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/24021b31-
f21c-4a2d-b772-59bce32a9e43",
         "DatabaseName":"ORCL",
         "EngineName":"oracle",
         "EndpointIdentifier":"test",
         "Port":1521
      }
   ]
}
```

## See Also
<a name="API_DescribeEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeEndpoints)
