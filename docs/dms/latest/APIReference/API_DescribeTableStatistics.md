---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeTableStatistics.html
---

# DescribeTableStatistics
<a name="API_DescribeTableStatistics"></a>

Returns table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted.

Note that the "last updated" column the DMS console only indicates the time that AWS DMS last updated the table statistics record for a table. It does not indicate the time of the last update to the table.

## Request Syntax
<a name="API_DescribeTableStatistics_RequestSyntax"></a>

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
   "ReplicationTaskArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTableStatistics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeTableStatistics_RequestSyntax) **   <a name="DMS-DescribeTableStatistics-request-Filters"></a>
Filters applied to table statistics.
Valid filter names: schema-name \| table-name \| table-state
A combination of filters creates an AND condition where each record matches all specified filters.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeTableStatistics_RequestSyntax) **   <a name="DMS-DescribeTableStatistics-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeTableStatistics_RequestSyntax) **   <a name="DMS-DescribeTableStatistics-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 500.
Type: Integer
Required: No

 ** [ReplicationTaskArn](#API_DescribeTableStatistics_RequestSyntax) **   <a name="DMS-DescribeTableStatistics-request-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) of the replication task.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeTableStatistics_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ReplicationTaskArn": "string",
   "TableStatistics": [
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
<a name="API_DescribeTableStatistics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeTableStatistics_ResponseSyntax) **   <a name="DMS-DescribeTableStatistics-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [ReplicationTaskArn](#API_DescribeTableStatistics_ResponseSyntax) **   <a name="DMS-DescribeTableStatistics-response-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) of the replication task.
Type: String

 ** [TableStatistics](#API_DescribeTableStatistics_ResponseSyntax) **   <a name="DMS-DescribeTableStatistics-response-TableStatistics"></a>
The table statistics.
Type: Array of [TableStatistics](API_TableStatistics.md) objects

## Errors
<a name="API_DescribeTableStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeTableStatistics_Examples"></a>

### Example
<a name="API_DescribeTableStatistics_Example_1"></a>

This example illustrates one usage of DescribeTableStatistics.

#### Sample Request
<a name="API_DescribeTableStatistics_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeTableStatistics
{
     "ReplicationTaskArn": "arn:aws:dms:us-west-
     2:918017823489:task:WZVIPF3D4AJSNJASB42D4Z7GBE",
     "SchemaName": "",
     "TableNames": [
          ""
          ],
     "MaxRecords": 0,
     "Marker": ""
}
```

#### Sample Response
<a name="API_DescribeTableStatistics_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
"ReplicationTaskArn": "arn:aws:dms:us-west-
2:918017823489:task:WZVIPF3D4AJSNJASB42D4Z7GBE",
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
<a name="API_DescribeTableStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeTableStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeTableStatistics)
