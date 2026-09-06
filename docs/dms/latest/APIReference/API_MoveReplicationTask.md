---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MoveReplicationTask.html
---

# MoveReplicationTask
<a name="API_MoveReplicationTask"></a>

Moves a replication task from its current replication instance to a different target replication instance using the specified parameters. The target replication instance must be created with the same or later AWS DMS version as the current replication instance.

## Request Syntax
<a name="API_MoveReplicationTask_RequestSyntax"></a>

```
{
   "ReplicationTaskArn": "{{string}}",
   "TargetReplicationInstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_MoveReplicationTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplicationTaskArn](#API_MoveReplicationTask_RequestSyntax) **   <a name="DMS-MoveReplicationTask-request-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) of the task that you want to move.
Type: String
Required: Yes

 ** [TargetReplicationInstanceArn](#API_MoveReplicationTask_RequestSyntax) **   <a name="DMS-MoveReplicationTask-request-TargetReplicationInstanceArn"></a>
The ARN of the replication instance where you want to move the task to.
Type: String
Required: Yes

## Response Syntax
<a name="API_MoveReplicationTask_ResponseSyntax"></a>

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
<a name="API_MoveReplicationTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationTask](#API_MoveReplicationTask_ResponseSyntax) **   <a name="DMS-MoveReplicationTask-response-ReplicationTask"></a>
The replication task that was moved.
Type: [ReplicationTask](API_ReplicationTask.md) object

## Errors
<a name="API_MoveReplicationTask_Errors"></a>

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

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_MoveReplicationTask_Examples"></a>

### Example
<a name="API_MoveReplicationTask_Example_1"></a>

This example illustrates one usage of MoveReplicationTask.

#### Sample Request
<a name="API_MoveReplicationTask_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.MoveReplicationTask
{
   "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:GBQBVYT7IIWCUUE44KI7ITKAK2OIURGWGDR4QZY",
   "TargetReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:UMBQHEHRZ2WG23LSVP767KHNWGHSXVTTSSUXZCI"
}
```

#### Sample Response
<a name="API_MoveReplicationTask_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationTask": {
      "ReplicationTaskIdentifier": "task-test",
      "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:GDBXFEKRITMGQO2POUA6VHZPIY",
      "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:DIGHLLJZKQUN3VEF2MQC7D4VNE",
      "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:HBNEJHHRZ2WG23LSVP767KHNWGHSXVTTSASHB",
      "MigrationType": "full-load-and-cdc",
      "TableMappings": "{\n \"TableMappings\": [
      \n {\n \"Type\": \"Include\",\n \"SourceSchema\": \"/\",\n \"SourceTable\": \"/\"\n
         }\n ]\n}\n\n",
      "ReplicationTaskSettings": "",
      "Status": "moving",
      "ReplicationTaskCreationDate": 1595513932.394
      "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:GBQBVYT7IIWCUUE44KI7ITKAK2OIURGWGDR4QZY",
      "TargetReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:UMBQHEHRZ2WG23LSVP767KHNWGHSXVTTSSUXZCI"
   }
}
```

## See Also
<a name="API_MoveReplicationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/MoveReplicationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MoveReplicationTask)
