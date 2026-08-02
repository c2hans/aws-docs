---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdatedSessionActionInfo.html
---

# UpdatedSessionActionInfo
<a name="API_UpdatedSessionActionInfo"></a>

The updated session action information as it relates to completion and progress of the session.

## Contents
<a name="API_UpdatedSessionActionInfo_Contents"></a>

 ** completedStatus **   <a name="deadlinecloud-Type-UpdatedSessionActionInfo-completedStatus"></a>
The status of the session upon completion.
Type: String
Valid Values: `SUCCEEDED | FAILED | INTERRUPTED | CANCELED | NEVER_ATTEMPTED`
Required: No

 ** endedAt **   <a name="deadlinecloud-Type-UpdatedSessionActionInfo-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** manifests **   <a name="deadlinecloud-Type-UpdatedSessionActionInfo-manifests"></a>
A list of output manifest properties reported by the worker agent, with each entry corresponding to a manifest property in the job.
Type: Array of [TaskRunManifestPropertiesRequest](API_TaskRunManifestPropertiesRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** processExitCode **   <a name="deadlinecloud-Type-UpdatedSessionActionInfo-processExitCode"></a>
The process exit code. The default Deadline Cloud worker agent converts unsigned 32-bit exit codes to signed 32-bit exit codes.
Type: Integer
Valid Range: Minimum value of -2147483648. Maximum value of 2147483647.
Required: No

 ** progressMessage **   <a name="deadlinecloud-Type-UpdatedSessionActionInfo-progressMessage"></a>
A message to indicate the progress of the updated session action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** progressPercent **   <a name="deadlinecloud-Type-UpdatedSessionActionInfo-progressPercent"></a>
The percentage completed.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-UpdatedSessionActionInfo-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-UpdatedSessionActionInfo-updatedAt"></a>
The updated time.
Type: Timestamp
Required: No

## See Also
<a name="API_UpdatedSessionActionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/UpdatedSessionActionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/UpdatedSessionActionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/UpdatedSessionActionInfo)
