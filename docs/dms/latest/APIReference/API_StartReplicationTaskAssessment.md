---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessment.html
---

# StartReplicationTaskAssessment
<a name="API_StartReplicationTaskAssessment"></a>

 Starts the replication task assessment for unsupported data types in the source database.

You can only use this operation for a task if the following conditions are true:
+ The task must be in the `stopped` state.
+ The task must have successful connections to the source and target.

If either of these conditions are not met, an `InvalidResourceStateFault` error will result.

For information about AWS DMS task assessments, see [Creating a task assessment report](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html) in the * AWS Database Migration Service User Guide*.

## Request Syntax
<a name="API_StartReplicationTaskAssessment_RequestSyntax"></a>

```
{
   "ReplicationTaskArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StartReplicationTaskAssessment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReplicationTaskArn](#API_StartReplicationTaskAssessment_RequestSyntax) **   <a name="DMS-StartReplicationTaskAssessment-request-ReplicationTaskArn"></a>
 The Amazon Resource Name (ARN) of the replication task.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartReplicationTaskAssessment_ResponseSyntax"></a>

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
<a name="API_StartReplicationTaskAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationTask](#API_StartReplicationTaskAssessment_ResponseSyntax) **   <a name="DMS-StartReplicationTaskAssessment-response-ReplicationTask"></a>
 The assessed replication task.
Type: [ReplicationTask](API_ReplicationTask.md) object

## Errors
<a name="API_StartReplicationTaskAssessment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_StartReplicationTaskAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartReplicationTaskAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartReplicationTaskAssessment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
