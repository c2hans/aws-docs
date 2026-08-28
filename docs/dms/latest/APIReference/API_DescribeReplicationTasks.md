---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTasks.html
---

# DescribeReplicationTasks
<a name="API_DescribeReplicationTasks"></a>

Returns information about replication tasks for your account in the current region.

## Request Syntax
<a name="API_DescribeReplicationTasks_RequestSyntax"></a>

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
   "WithoutSettings": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeReplicationTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeReplicationTasks_RequestSyntax) **   <a name="DMS-DescribeReplicationTasks-request-Filters"></a>
Filters applied to replication tasks.
Valid filter names: replication-task-arn \| replication-task-id \| migration-type \| endpoint-arn \| replication-instance-arn
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeReplicationTasks_RequestSyntax) **   <a name="DMS-DescribeReplicationTasks-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplicationTasks_RequestSyntax) **   <a name="DMS-DescribeReplicationTasks-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** [WithoutSettings](#API_DescribeReplicationTasks_RequestSyntax) **   <a name="DMS-DescribeReplicationTasks-request-WithoutSettings"></a>
An option to set to avoid returning information about settings. Use this to reduce overhead when setting information is too large. To use this option, choose `true`; otherwise, choose `false` (the default).
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeReplicationTasks_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ReplicationTasks": [
      {
         "CdcStartPosition": "string",
         "CdcStopPosition": "string",
         "LastFailureMessage": "string",
         "MigrationType": "string",
         "RecoveryCheckpoint": "string",
         "ReplicationInstanceArn": "string",
         "ReplicationTaskArn": "string",
         "ReplicationTaskCreationDate": number,
         "ReplicationTaskIdentifier": "string",
         "ReplicationTaskSettings": "string",
         "ReplicationTaskStartDate": number,
         "ReplicationTaskStats": {
            "ElapsedTimeMillis": number,
            "FreshStartDate": number,
            "FullLoadFinishDate": number,
            "FullLoadProgressPercent": number,
            "FullLoadStartDate": number,
            "StartDate": number,
            "StopDate": number,
            "TablesErrored": number,
            "TablesLoaded": number,
            "TablesLoading": number,
            "TablesQueued": number
         },
         "SourceEndpointArn": "string",
         "Status": "string",
         "StopReason": "string",
         "TableMappings": "string",
         "TargetEndpointArn": "string",
         "TargetReplicationInstanceArn": "string",
         "TaskData": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplicationTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeReplicationTasks_ResponseSyntax) **   <a name="DMS-DescribeReplicationTasks-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [ReplicationTasks](#API_DescribeReplicationTasks_ResponseSyntax) **   <a name="DMS-DescribeReplicationTasks-response-ReplicationTasks"></a>
A description of the replication tasks.
Type: Array of [ReplicationTask](API_ReplicationTask.md) objects

## Errors
<a name="API_DescribeReplicationTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeReplicationTasks_Examples"></a>

### Example
<a name="API_DescribeReplicationTasks_Example_1"></a>

This example illustrates one usage of DescribeReplicationTasks.

#### Sample Request
<a name="API_DescribeReplicationTasks_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeReplicationTasks
{
   "Filters":[
      {
         "Name":"endpoint-arn",
         "Values":[
            "arn:aws:dms:us-east-
1:123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeReplicationTasks_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationTasks":[
      {
         "SourceEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE",
         "ReplicationTaskIdentifier":"aks145",
         "ReplicationInstanceArn":"arn:aws:dms:us-east-
1:123456789012:rep:6USOU366XFJUWATDJGBCJS3VIQ",
         "TableMappings":"{ \n\t\"TableMappings\": [ {
\n\t\t\"Type\": \"Include\",\n\t\t \"SourceSchema\": \"testDB\",\n\t\t
\"SourceTable\": \"%\" \n\t}, { \n\t\t\"Type\": \"Include\",\n\t\t
\"SourceSchema\": \"testDB\",\n\t\t \"SourceTable\": \"%\" \n\t} ]\n}",
         "ReplicationTaskStartDate":1452868617.764,
         "ReplicationTaskStats":{
            "TablesLoading":0,
            "TablesQueued":0,
            "TablesErrored":0,
            "FullLoadProgressPercent":100,
            "TablesLoaded":0,
            "ElapsedTimeMillis":0
         },
         "Status":"stopped",
         "ReplicationTaskArn":"arn:aws:dms:us-east-
1:123456789012:task:RALPZGYI3IUSJCBKKIRBEURKDY",
         "ReplicationTaskCreationDate":1449185680.107,
         "MigrationType":"full-load",
         "TargetEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:GVBUJQXJZASXWHTWCLN2WNT57E",
         "ReplicationTaskSettings":"{\"TargetMetadata\":{\"TargetSchema\":\"\",\"SupportLobs\":true,\"FullLobMod
e\":true,\"LobChunkSize\":64,\"LimitedSizeLobMode\":false,\"LobMaxSize\":0},\
"         FullLoadSettings\":{
            \"FullLoadEnabled\":true,
            \"
TargetTablePrepMode\":\"DO_NOTHING\",
            \"CreatePkAfterFullLoad\":false,
            \"StopTaskCachedChangesApplied\":false,
            \"StopTaskCachedChangesNotApplied\":false,
            \"Re
sumeEnabled\":false,
            \"ResumeMinTableSize\":100000,
            \"ResumeOnlyClusteredPKTabl
es\":true,
            \"MaxFullLoadSubTasks\":8,
            \"TransactionConsistencyTimeout\":600,
            \"C
ommitRate\":10000
         }
      }      "
   }
]
}
```

### Example
<a name="API_DescribeReplicationTasks_Example_2"></a>

This example illustrates one usage of DescribeReplicationTasks.

#### Sample Request
<a name="API_DescribeReplicationTasks_Example_2_Request"></a>

```
aws dms describe-replication-tasks --filters "Name=replication-task-arn,Values=arn:aws:dms:us-west-2:012345678912:task:AAABBBCCC0123456789YYYZZZ0"
```

#### Sample Response
<a name="API_DescribeReplicationTasks_Example_2_Response"></a>

```
{
    "ReplicationTasks": [
        {
            "ReplicationTaskIdentifier": "<Task identifier>",
            "SourceEndpointArn": "<Source Endpoint ARN>",
            "TargetEndpointArn": "<Target Endpoint ARN>",
            "ReplicationInstanceArn": "<Instance ARN>",
            "MigrationType": "full-load",
            "TableMappings": "...output omitted...",
            "ReplicationTaskSettings": "...output omitted...",
            "Status": "ready",
            "StopReason": "Stop Reason NORMAL",
            "ReplicationTaskCreationDate": "2024-02-20T15:05:59.827000+00:00",
            "ReplicationTaskArn": "<Task ARN>",
            "ReplicationTaskStats": {
                "FullLoadProgressPercent": 0,
                "ElapsedTimeMillis": 0,
                "TablesLoaded": 0,
                "TablesLoading": 0,
                "TablesQueued": 0,
                "TablesErrored": 0
            }
        }
    ]
}
```

### Example
<a name="API_DescribeReplicationTasks_Example_3"></a>

This example illustrates one usage of DescribeReplicationTasks.

#### Sample Request
<a name="API_DescribeReplicationTasks_Example_3_Request"></a>

```
aws dms describe-replication-tasks --filters "Name=endpoint-arn,Values=arn:aws:dms:us-west-2:012345678912:endpoint:AAABBBCCC0123456789YYYZZZ0"
```

#### Sample Response
<a name="API_DescribeReplicationTasks_Example_3_Response"></a>

```
{
    "ReplicationTasks": [
        {
            "ReplicationTaskIdentifier": "<Task identifier>",
            "SourceEndpointArn": "<Source Endpoint ARN>",
            "TargetEndpointArn": "<Target Endpoint ARN>",
            "ReplicationInstanceArn": "<Instance ARN>",
            "MigrationType": "cdc",
            "TableMappings": "...output omitted...",
            "ReplicationTaskSettings": "...output omitted...",
            "Status": "stopped",
            "StopReason": "Stop Reason NORMAL",
            "ReplicationTaskCreationDate": "2023-12-07T15:26:08.594000+00:00",
            "ReplicationTaskStartDate": "2023-12-07T17:31:09.127000+00:00",
            "CdcStartPosition": "2023-12-07T15:38:51",
            "RecoveryCheckpoint": "checkpoint:V1#156#00000032:00000a55:000c#0#217#00000032:00000a5a:0003#0#213",
            "ReplicationTaskArn": "<Task ARN>",
            "ReplicationTaskStats": {
                "FullLoadProgressPercent": 100,
                "ElapsedTimeMillis": 4262,
                "TablesLoaded": 3,
                "TablesLoading": 0,
                "TablesQueued": 0,
                "TablesErrored": 0,
                "FreshStartDate": "2023-12-07T17:31:16.987000+00:00",
                "StartDate": "2023-12-07T17:31:16.987000+00:00",
                "StopDate": "2023-12-07T17:39:30.181000+00:00"
            }
        }
        {
            "ReplicationTaskIdentifier": "<Task identifier 2>",
            <...>
        },
        {
            "ReplicationTaskIdentifier": "<Task identifier 3>",
            <...>
        }
    ]
}
```

### Example
<a name="API_DescribeReplicationTasks_Example_4"></a>

This example illustrates one usage of DescribeReplicationTasks.

#### Sample Request
<a name="API_DescribeReplicationTasks_Example_4_Request"></a>

```
aws dms describe-replication-tasks --filters "Name=migration-type,Values=full-load,cdc"
```

#### Sample Response
<a name="API_DescribeReplicationTasks_Example_4_Response"></a>

```
{
    "ReplicationTasks": [
        {
            "ReplicationTaskIdentifier": "<Task identifier>",
            "SourceEndpointArn": "<Source Endpoint ARN>",
            "TargetEndpointArn": "<Target Endpoint ARN>",
            "ReplicationInstanceArn": "<Instance ARN>",
            "MigrationType": "cdc",
            "TableMappings": "...output omitted...",
            "ReplicationTaskSettings": "...output omitted...",
            "Status": "stopped",
            "StopReason": "Stop Reason NORMAL",
            "ReplicationTaskCreationDate": "2023-12-07T15:26:08.594000+00:00",
            "ReplicationTaskStartDate": "2023-12-07T17:31:09.127000+00:00",
            "CdcStartPosition": "2023-12-07T15:38:51",
            "RecoveryCheckpoint": "checkpoint:V1#156#00000032:00000a55:000c#0#217#00000032:00000a5a:0003#0#213",
            "ReplicationTaskArn": "<Task ARN>",
            "ReplicationTaskStats": {
                "FullLoadProgressPercent": 100,
                "ElapsedTimeMillis": 4262,
                "TablesLoaded": 3,
                "TablesLoading": 0,
                "TablesQueued": 0,
                "TablesErrored": 0,
                "FreshStartDate": "2023-12-07T17:31:16.987000+00:00",
                "StartDate": "2023-12-07T17:31:16.987000+00:00",
                "StopDate": "2023-12-07T17:39:30.181000+00:00"
            }
        },
        {
            "ReplicationTaskIdentifier": "<Task identifier>",
            "SourceEndpointArn": "<Source Endpoint ARN>",
            "TargetEndpointArn": "<Target Endpoint ARN>",
            "ReplicationInstanceArn": "<Instance ARN>",
            "MigrationType": "full-load",
            "TableMappings": "...output omitted...",
            "ReplicationTaskSettings": "...output omitted...",
            "Status": "stopped",
            "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED",
            "ReplicationTaskCreationDate": "2023-02-28T13:02:34.389000+00:00",
            "ReplicationTaskStartDate": "2023-02-28T14:33:59.617000+00:00",
            "RecoveryCheckpoint": "checkpoint:V1#5015#00000007.c99042d0.00000001.000c.01.0000:401032.58563.16#0#0#*#0#0",
            "ReplicationTaskArn": "<Task ARN>",
            "ReplicationTaskStats": {
                "FullLoadProgressPercent": 100,
                "ElapsedTimeMillis": 0,
                "TablesLoaded": 0,
                "TablesLoading": 0,
                "TablesQueued": 0,
                "TablesErrored": 1,
                "FreshStartDate": "2023-02-28T14:34:10.998000+00:00",
                "StartDate": "2023-02-28T14:34:10.998000+00:00",
                "StopDate": "2023-02-28T14:34:51.004000+00:00"
            }
        }
    ]
}
```

## See Also
<a name="API_DescribeReplicationTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplicationTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplicationTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
