---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html
---

# CreateReplicationTask
<a name="API_CreateReplicationTask"></a>

Creates a replication task using the specified parameters.

## Request Syntax
<a name="API_CreateReplicationTask_RequestSyntax"></a>

```
{
   "CdcStartPosition": "{{string}}",
   "CdcStartTime": {{number}},
   "CdcStopPosition": "{{string}}",
   "MigrationType": "{{string}}",
   "ReplicationInstanceArn": "{{string}}",
   "ReplicationTaskIdentifier": "{{string}}",
   "ReplicationTaskSettings": "{{string}}",
   "ResourceIdentifier": "{{string}}",
   "SourceEndpointArn": "{{string}}",
   "TableMappings": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "ResourceArn": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetEndpointArn": "{{string}}",
   "TaskData": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateReplicationTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CdcStartPosition](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-CdcStartPosition"></a>
Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.
 The value can be in date, checkpoint, or LSN/SCN format.
Date Example: --cdc-start-position “2018-03-08T12:12:12”
Checkpoint Example: --cdc-start-position "checkpoint:V1\#27\#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876\#0\#0\#\*\#0\#93"
LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”
When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the `slotName` extra connection attribute to the name of this logical replication slot. For more information, see [Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib).
Type: String
Required: No

 ** [CdcStartTime](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-CdcStartTime"></a>
Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.
Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”
Type: Timestamp
Required: No

 ** [CdcStopPosition](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-CdcStopPosition"></a>
Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.
Server time example: --cdc-stop-position “server\_time:2018-02-09T12:12:12”
Commit time example: --cdc-stop-position “commit\_time:2018-02-09T12:12:12“
Type: String
Required: No

 ** [MigrationType](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-MigrationType"></a>
The migration type. Valid values: `full-load` \| `cdc` \| `full-load-and-cdc`
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: Yes

 ** [ReplicationInstanceArn](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of a replication instance.
Type: String
Required: Yes

 ** [ReplicationTaskIdentifier](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-ReplicationTaskIdentifier"></a>
An identifier for the replication task.
Constraints:
+ Must contain 1-255 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Type: String
Required: Yes

 ** [ReplicationTaskSettings](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-ReplicationTaskSettings"></a>
Overall settings for the task, in JSON format. For more information, see [Specifying Task Settings for AWS Database Migration Service Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html) in the * AWS Database Migration Service User Guide.*
Type: String
Required: No

 ** [ResourceIdentifier](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-ResourceIdentifier"></a>
A friendly name for the resource identifier at the end of the `EndpointArn` response parameter that is returned in the created `Endpoint` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as `Example-App-ARN1`. For example, this value might result in the `EndpointArn` value `arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`. If you don't specify a `ResourceIdentifier` value, AWS DMS generates a default identifier value for the end of `EndpointArn`.
Type: String
Required: No

 ** [SourceEndpointArn](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-SourceEndpointArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.
Type: String
Required: Yes

 ** [TableMappings](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-TableMappings"></a>
The table mappings for the task, in JSON format. For more information, see [Using Table Mapping to Specify Task Settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html) in the * AWS Database Migration Service User Guide.*
Type: String
Required: Yes

 ** [Tags](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-Tags"></a>
One or more tags to be assigned to the replication task.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [TargetEndpointArn](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-TargetEndpointArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.
Type: String
Required: Yes

 ** [TaskData](#API_CreateReplicationTask_RequestSyntax) **   <a name="DMS-CreateReplicationTask-request-TaskData"></a>
Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see [Specifying Supplemental Data for Task Settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html) in the * AWS Database Migration Service User Guide.*
Type: String
Required: No

## Response Syntax
<a name="API_CreateReplicationTask_ResponseSyntax"></a>

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
<a name="API_CreateReplicationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationTask](#API_CreateReplicationTask_ResponseSyntax) **   <a name="DMS-CreateReplicationTask-response-ReplicationTask"></a>
The replication task that was created.
Type: [ReplicationTask](API_ReplicationTask.md) object

## Errors
<a name="API_CreateReplicationTask_Errors"></a>

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

## Examples
<a name="API_CreateReplicationTask_Examples"></a>

### Example
<a name="API_CreateReplicationTask_Example_1"></a>

This example illustrates one usage of CreateReplicationTask.

#### Sample Request
<a name="API_CreateReplicationTask_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.CreateReplicationTask
{
    "ReplicationTaskIdentifier":"task1",
    "SourceEndpointArn":"arn:aws:dms:us-east-1:
        123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE",
    "TargetEndpointArn":"arn:aws:dms:us-east-1:
        123456789012:endpoint:GVBUJQXJZASXWHTWCLN2WNT57E",
    "ReplicationInstanceArn":"arn:aws:dms:us-east-1:
        123456789012:rep:6USOU366XFJUWATDJGBCJS3VIQ",
    "MigrationType":"full-load",
    "TableMappings":"file:////home/apurvap/table-mappings.json",
    "ReplicationTaskSettings":"",
    "CdcStartTime":null,
    "Tags":[
        {
            "Key":"",
            "Value":""
        }
    ]
}
```

#### Sample Response
<a name="API_CreateReplicationTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "ReplicationTask":{
        "SourceEndpointArn":"arn:aws:dms:us-east-1:
            123456789012:endpoint:RZZK4EZW5UANC7Y3P4E776WHBE",
        "ReplicationTaskIdentifier":"task1",
        "ReplicationInstanceArn":"arn:aws:dms:us-east-1:
            123456789012:rep:6USOU366XFJUWATDJGBCJS3VIQ",
        "TableMappings":"{\n \"TableMappings\":
            [\n
                {\n \"Type\": \"Include\",\n \"SourceSchema\": \"/\",
                    \n \"SourceTable\": \"/ \"\n
                }\n
            ]\n
        }\n\n",
        "Status":"creating",
        "ReplicationTaskArn":"arn:aws:dms:us-east-1:
            123456789012:task:OEAMB3NXSTZ6LFYZFEPPBBXPYM",
        "ReplicationTaskCreationDate":1457658407.492,
        "MigrationType":"full-load",
        "TargetEndpointArn":"arn:aws:dms:us-east-1:
            123456789012:endpoint:GVBUJQXJZASXWHTWCLN2WNT57E",
        "ReplicationTaskSettings":"{\"TargetMetadata\":
            {\"TargetSchema\":\"\",\"SupportLobs\":true,\"FullLobMode\":
                true,\"LobChunkSize\":64,\"LimitedSizeLobMode\":
                false,\"LobMaxSize\":0},\"FullLoadSettings\":{
                    \"FullLoadEnabled\":true,
                    \"TargetTablePrepMode\":\"DROP_AND_CREATE\",
                    \"CreatePkAfterFullLoad\":false,
                    \"StopTaskCachedChangesApplied\":false,
                    \"StopTaskCachedChangesNotApplied\":false,
                    \"ResumeEnabled\":false,
                    \"ResumeMinTableSize\":100000,
                    \"ResumeOnlyClusteredPKTables\":true,
                    \"MaxFullLoadSubTasks\":8,
                    \"TransactionConsistencyTimeout\":600,
                    \"CommitRate\":10000
             },
             \"Logging\":{
                 \"EnableLogging\":false
             }
        }"
    }
}
```

## See Also
<a name="API_CreateReplicationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CreateReplicationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CreateReplicationTask)
