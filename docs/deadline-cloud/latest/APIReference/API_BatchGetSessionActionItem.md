---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetSessionActionItem.html
---

# BatchGetSessionActionItem
<a name="API_BatchGetSessionActionItem"></a>

The details of a session action returned in a batch get operation.

## Contents
<a name="API_BatchGetSessionActionItem_Contents"></a>

 ** definition **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-definition"></a>
The session action definition.
Type: [SessionActionDefinition](API_SessionActionDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-farmId"></a>
The farm ID of the session action.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-jobId"></a>
The job ID of the session action.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-queueId"></a>
The queue ID of the session action.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** sessionActionId **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-sessionActionId"></a>
The session action ID.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

 ** sessionId **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-sessionId"></a>
The session ID for the session action.
Type: String
Pattern: `session-[0-9a-f]{32}`
Required: Yes

 ** status **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-status"></a>
The status of the session action.
Type: String
Valid Values: `ASSIGNED | RUNNING | CANCELING | SUCCEEDED | FAILED | INTERRUPTED | CANCELED | NEVER_ATTEMPTED | SCHEDULED | RECLAIMING | RECLAIMED`
Required: Yes

 ** acquiredLimits **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-acquiredLimits"></a>
The limits that were acquired for the session action.
Type: Array of [AcquiredLimit](API_AcquiredLimit.md) objects
Required: No

 ** endedAt **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** manifests **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-manifests"></a>
The manifests for the session action.
Type: Array of [TaskRunManifestPropertiesResponse](API_TaskRunManifestPropertiesResponse.md) objects
Required: No

 ** processExitCode **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-processExitCode"></a>
The exit code to apply to the session action.
Type: Integer
Valid Range: Minimum value of -2147483648. Maximum value of 2147483647.
Required: No

 ** progressMessage **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-progressMessage"></a>
The message that communicates the progress of the session action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** progressPercent **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-progressPercent"></a>
The completion percentage for the session action.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** workerUpdatedAt **   <a name="deadlinecloud-Type-BatchGetSessionActionItem-workerUpdatedAt"></a>
The date and time the resource was updated by a worker.
Type: Timestamp
Required: No

## See Also
<a name="API_BatchGetSessionActionItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetSessionActionItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetSessionActionItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetSessionActionItem)
