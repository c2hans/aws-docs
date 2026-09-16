---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTableStatistics.html
---

# DescribeReplicationTableStatistics
<a name="API_DescribeReplicationTableStatistics"></a>

Returns table and schema statistics for one or more provisioned replications that use a given AWS DMS Serverless replication configuration.

## Request Syntax
<a name="API_DescribeReplicationTableStatistics_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "ReplicationConfigArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReplicationTableStatistics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeReplicationTableStatistics_RequestSyntax) **   <a name="DMS-DescribeReplicationTableStatistics-request-Filters"></a>
Filters applied to the replication table statistics.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeReplicationTableStatistics_RequestSyntax) **   <a name="DMS-DescribeReplicationTableStatistics-request-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplicationTableStatistics_RequestSyntax) **   <a name="DMS-DescribeReplicationTableStatistics-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [ReplicationConfigArn](#API_DescribeReplicationTableStatistics_RequestSyntax) **   <a name="DMS-DescribeReplicationTableStatistics-request-ReplicationConfigArn"></a>
The replication config to describe.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeReplicationTableStatistics_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ReplicationConfigArn": "string",
   "ReplicationTableStatistics": [
      {
         "AppliedDdls": number,
         "AppliedDeletes": number,
         "AppliedInserts": number,
         "AppliedUpdates": number,
         "Ddls": number,
         "Deletes": number,
         "FullLoadCondtnlChkFailedRows": number,
         "FullLoadEndTime": number,
         "FullLoadErrorRows": number,
         "FullLoadReloaded": boolean,
         "FullLoadRows": number,
         "FullLoadStartTime": number,
         "Inserts": number,
         "LastUpdateTime": number,
         "ResyncProgress": number,
         "ResyncRowsAttempted": number,
         "ResyncRowsFailed": number,
         "ResyncRowsSucceeded": number,
         "ResyncState": "string",
         "SchemaName": "string",
         "TableName": "string",
         "TableState": "string",
         "Updates": number,
         "ValidationFailedRecords": number,
         "ValidationPendingRecords": number,
         "ValidationState": "string",
         "ValidationStateDetails": "string",
         "ValidationSuspendedRecords": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplicationTableStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeReplicationTableStatistics_ResponseSyntax) **   <a name="DMS-DescribeReplicationTableStatistics-response-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [ReplicationConfigArn](#API_DescribeReplicationTableStatistics_ResponseSyntax) **   <a name="DMS-DescribeReplicationTableStatistics-response-ReplicationConfigArn"></a>
The Amazon Resource Name of the replication config.
Type: String

 ** [ReplicationTableStatistics](#API_DescribeReplicationTableStatistics_ResponseSyntax) **   <a name="DMS-DescribeReplicationTableStatistics-response-ReplicationTableStatistics"></a>
Returns table statistics on the replication, including table name, rows inserted, rows updated, and rows deleted.
Type: Array of [TableStatistics](API_TableStatistics.md) objects

## Errors
<a name="API_DescribeReplicationTableStatistics_Errors"></a>

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
<a name="API_DescribeReplicationTableStatistics_Examples"></a>

### Example
<a name="API_DescribeReplicationTableStatistics_Example_1"></a>

This example illustrates one usage of DescribeReplicationTableStatistics.

#### Sample Request
<a name="API_DescribeReplicationTableStatistics_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
 SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.DescribeReplicationTableStatistics
{
   "ReplicationConfigArn": "arn:aws:dms:us-east-
1:123456789012:replication-config:WZVIPF3D4AJSNJASB42D4Z7GBE",
   "SchemaName": "",
   "TableNames": [
      ""
   ],
   "MaxRecords": 0,
   "Marker": ""
}
```

#### Sample Response
<a name="API_DescribeReplicationTableStatistics_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationConfigArn": "arn:aws:dms:us-east-
1:123456789012:replication-config:WZVIPF3D4AJSNJASB42D4Z7GBE",
   "TableStatistics": [
      {
         "SchemaName": "travel",
         "TableName": "vehicle",
         "Inserts": 3872,
         "Deletes": 0,
         "Updates": 0,
         "Ddls": 1,
         "AppliedInserts": 3872,
         "AppliedDeletes": 0,
         "AppliedUpdates": 0,
         "AppliedDdls": 1,
         "FullLoadRows": 0,
         "FullLoadCondtnlChkFailedRows": 0,
         "FullLoadErrorRows": 0,
         "FullLoadStartTime": 1658436291.83,
         "FullLoadEndTime": 1658437392.059,
         "FullLoadReloaded": false,
         "LastUpdateTime": 1658437401.063,
         "TableState": "Table completed",
         "ScheduledForReload": false,
         "ValidationPendingRecords": 0,
         "ValidationFailedRecords": 0,
         "ValidationSuspendedRecords": 0,
         "ValidationState": "Not enabled"
      },
      {
         "SchemaName": "travel",
         "TableName": "drivers",
         "Inserts": 20,
         "Deletes": 0,
         "Updates": 0,
         "Ddls": 1,
         "AppliedInserts": 20,
         "AppliedDeletes": 0,
         "AppliedUpdates": 0,
         "AppliedDdls": 1,
         "FullLoadRows": 0,
         "FullLoadCondtnlChkFailedRows": 0,
         "FullLoadErrorRows": 0,
         "FullLoadStartTime": 1658436291.534,
         "FullLoadEndTime": 1658436483.802,
         "FullLoadReloaded": false,
         "LastUpdateTime": 1658437212.063,
         "TableState": "Table completed",
         "ScheduledForReload": false,
         "ValidationPendingRecords": 0,
         "ValidationFailedRecords": 0,
         "ValidationSuspendedRecords": 0,
         "ValidationState": "Not enabled"
      },
      {
         "SchemaName": "travel",
         "TableName": "passengers",
         "Inserts": 60,
         "Deletes": 0,
         "Updates": 0,
         "Ddls": 1,
         "AppliedInserts": 60,
         "AppliedDeletes": 0,
         "AppliedUpdates": 0,
         "AppliedDdls": 1,
         "FullLoadRows": 0,
         "FullLoadCondtnlChkFailedRows": 0,
         "FullLoadErrorRows": 0,
         "FullLoadStartTime": 1658446502.641,
         "FullLoadEndTime": 1658454293.712,
         "FullLoadReloaded": false,
         "LastUpdateTime": 1658454301.153,
         "TableState": "Table completed",
         "ScheduledForReload": false,
         "ValidationPendingRecords": 0,
         "ValidationFailedRecords": 0,
         "ValidationSuspendedRecords": 0,
         "ValidationState": "Not enabled"
      }
   ]
}
```

## See Also
<a name="API_DescribeReplicationTableStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplicationTableStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplicationTableStatistics)
