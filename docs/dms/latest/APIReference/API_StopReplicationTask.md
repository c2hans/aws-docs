---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StopReplicationTask.html
---

# StopReplicationTask
<a name="API_StopReplicationTask"></a>

Stops the replication task.

## Request Syntax
<a name="API_StopReplicationTask_RequestSyntax"></a>

```
{
   "ReplicationTaskArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StopReplicationTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplicationTaskArn](#API_StopReplicationTask_RequestSyntax) **   <a name="DMS-StopReplicationTask-request-ReplicationTaskArn"></a>
The Amazon Resource Name(ARN) of the replication task to be stopped.
Type: String
Required: Yes

## Response Syntax
<a name="API_StopReplicationTask_ResponseSyntax"></a>

```
{
   "ReplicationTask": {
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
}
```

## Response Elements
<a name="API_StopReplicationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationTask](#API_StopReplicationTask_ResponseSyntax) **   <a name="DMS-StopReplicationTask-response-ReplicationTask"></a>
The replication task stopped.
Type: [ReplicationTask](API_ReplicationTask.md) object

## Errors
<a name="API_StopReplicationTask_Errors"></a>

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
<a name="API_StopReplicationTask_Examples"></a>

### Example
<a name="API_StopReplicationTask_Example_1"></a>

This example illustrates one usage of StopReplicationTask.

#### Sample Request
<a name="API_StopReplicationTask_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.StopReplicationTask
{
   "ReplicationTaskArn":"arn:aws:dms:us-east-
1:123456789012:task:OEAMB3NXSTZ6LFYZFEPPBBXPYM"
}
```

#### Sample Response
<a name="API_StopReplicationTask_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationTask":{
      "SourceEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE",
      "ReplicationTaskIdentifier":"task1",
      "ReplicationInstanceArn":"arn:aws:dms:us-east-
1:123456789012:rep:6USOU366XFJUWATDJGBCJS3VIQ",
      "TableMappings":"{\n \"TableMappings\": [\n {\n \"Type\":
\"Include\",\n \"SourceSchema\": \"/\",\n \"SourceTable\": \"/\"\n
}\n ]\n}\n\n",
      "ReplicationTaskStartDate":1457659049.081,
      "Status":"stopping",
      "ReplicationTaskArn":"arn:aws:dms:us-east-
1:123456789012:task:OEAMB3NXSTZ6LFYZFEPPBBXPYM",
      "ReplicationTaskCreationDate":1457658407.492,
      "MigrationType":"full-load",
      "TargetEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:GVBUJQXJZASXWHTWCLN2WNT57E",
      "ReplicationTaskSettings":"{\"TargetMetadata\":{\"TargetSchema\":\"\",\"SupportLobs\":true,\"FullLobMod
e\":true,\"LobChunkSize\":64,\"LimitedSizeLobMode\":false,\"LobMaxSize\":0},\
"      FullLoadSettings\":{
         \"FullLoadEnabled\":true,
         \
"TargetTablePrepMode\":\"DROP_AND_CREATE\",
         \"CreatePkAfterFullLoad\":false,
         \"
StopTaskCachedChangesApplied\":false,
         \"StopTaskCachedChangesNotApplied\":false,
         \"ResumeEnabled\":false,
         \"ResumeMinTableSize\":100000,
         \"ResumeOnlyClustered
PKTables\":true,
         \"MaxFullLoadSubTasks\":8,
         \"TransactionConsistencyTimeout\":6         00,
         \"CommitRate\":10000
      },
      \"Logging\":{
         \"EnableLogging\":false
      }
   }   "
}
}
```

## See Also
<a name="API_StopReplicationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StopReplicationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StopReplicationTask)
