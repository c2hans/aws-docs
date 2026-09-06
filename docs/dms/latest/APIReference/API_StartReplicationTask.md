---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html
---

# StartReplicationTask
<a name="API_StartReplicationTask"></a>

Starts the replication task.

For more information about AWS DMS tasks, see [Working with Migration Tasks ](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html) in the * AWS Database Migration Service User Guide.*

## Request Syntax
<a name="API_StartReplicationTask_RequestSyntax"></a>

```
{
   "CdcStartPosition": "{{string}}",
   "CdcStartTime": {{number}},
   "CdcStopPosition": "{{string}}",
   "ReplicationTaskArn": "{{string}}",
   "StartReplicationTaskType": "{{string}}"
}
```

## Request Parameters
<a name="API_StartReplicationTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CdcStartPosition](#API_StartReplicationTask_RequestSyntax) **   <a name="DMS-StartReplicationTask-request-CdcStartPosition"></a>
Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
 The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position “2018-03-08T12:12:12”
Checkpoint Example: --cdc-start-position "checkpoint:V1\#27\#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876\#0\#0\#\*\#0\#93"
LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the `slotName` extra connection attribute to the name of this logical replication slot. For more information, see [Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib).
Type: String
Required: No

 ** [CdcStartTime](#API_StartReplicationTask_RequestSyntax) **   <a name="DMS-StartReplicationTask-request-CdcStartTime"></a>
Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.
Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”
Type: Timestamp
Required: No

 ** [CdcStopPosition](#API_StartReplicationTask_RequestSyntax) **   <a name="DMS-StartReplicationTask-request-CdcStopPosition"></a>
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position “server\_time:2018-02-09T12:12:12”
Commit time example: --cdc-stop-position “commit\_time:2018-02-09T12:12:12“
Type: String
Required: No

 ** [ReplicationTaskArn](#API_StartReplicationTask_RequestSyntax) **   <a name="DMS-StartReplicationTask-request-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) of the replication task to be started.
Type: String
Required: Yes

 ** [StartReplicationTaskType](#API_StartReplicationTask_RequestSyntax) **   <a name="DMS-StartReplicationTask-request-StartReplicationTaskType"></a>
The type of replication task to start.
 `start-replication` is the only valid action that can be used for the first time a task with the migration type of `full-load`full-load, `full-load-and-cdc` or `cdc` is run. Any other action used for the first time on a given task, such as `resume-processing` and reload-target will result in data errors.
You can also use [ReloadTables](API_ReloadTables.md) to reload specific tables that failed during migration instead of restarting the task.
For a `full-load` task, the resume-processing option will reload any tables that were partially loaded or not yet loaded during the full load phase.
For a `full-load-and-cdc` task, DMS migrates table data, and then applies data changes that occur on the source. To load all the tables again, and start capturing source changes, use `reload-target`. Otherwise use `resume-processing`, to replicate the changes from the last stop position.
For a `cdc` only task, to start from a specific position, you must use start-replication and also specify the start position. Check the source endpoint DMS documentation for any limitations. For example, not all sources support starting from a time.
 `resume-processing` is only available for previously executed tasks.
Type: String
Valid Values: `start-replication | resume-processing | reload-target`
Required: Yes

## Response Syntax
<a name="API_StartReplicationTask_ResponseSyntax"></a>

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
<a name="API_StartReplicationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationTask](#API_StartReplicationTask_ResponseSyntax) **   <a name="DMS-StartReplicationTask-response-ReplicationTask"></a>
The replication task started.
Type: [ReplicationTask](API_ReplicationTask.md) object

## Errors
<a name="API_StartReplicationTask_Errors"></a>

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
<a name="API_StartReplicationTask_Examples"></a>

### Example
<a name="API_StartReplicationTask_Example_1"></a>

This example illustrates one usage of StartReplicationTask.

#### Sample Request
<a name="API_StartReplicationTask_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.StartReplicationTask
{
   "ReplicationTaskArn":"arn:aws:dms:us-east-
1:123456789012:task:RALPZGYI3IUSJCBKKIRBEURKDY",
   "StartReplicationTaskType":"reload-target",
   "CdcStartTime":null
}
```

#### Sample Response
<a name="API_StartReplicationTask_Example_1_Response"></a>

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
      "ReplicationTaskIdentifier":"aks145",
      "ReplicationInstanceArn":"arn:aws:dms:us-east-
1:123456789012:rep:6USOU366XFJUWATDJGBCJS3VIQ",
      "TableMappings":"{ \n\t\"TableMappings\": [ { \n\t\t\"Type\":
\"Include\",\n\t\t \"SourceSchema\": \"testDB\",\n\t\t \"SourceTable\":
\"%\" \n\t}, { \n\t\t\"Type\": \"Include\",\n\t\t
\"SourceSchema\": \"testDB\",\n\t\t \"SourceTable\": \"%\" \n\t} ]\n}",
      "ReplicationTaskStartDate":1457658794.056,
      "Status":"starting",
      "ReplicationTaskArn":"arn:aws:dms:us-east-
1:123456789012:task:RALPZGYI3IUSJCBKKIRBEURKDY",
      "ReplicationTaskCreationDate":1449185680.107,
      "MigrationType":"full-load",
      "TargetEndpointArn":"arn:aws:dms:us-east-
1:123456789012:endpoint:GVBUJQXJZASXWHTWCLN2WNT57E",
      "ReplicationTaskSettings":"{\"TargetMetadata\":{\"TargetSchema\":\"\",\"SupportLobs\":true,\"FullLobMod
e\":true,\"LobChunkSize\":64,\"LimitedSizeLobMode\":false,\"LobMaxSize\":0},\
"      FullLoadSettings\":{
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
   }   "
}
}
```

## See Also
<a name="API_StartReplicationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartReplicationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartReplicationTask)
