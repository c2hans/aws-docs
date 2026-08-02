---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_OtaTaskExecutionSummary.html
---

# OtaTaskExecutionSummary
<a name="API_OtaTaskExecutionSummary"></a>

Structure representing one over-the-air (OTA) task execution summary.

## Contents
<a name="API_OtaTaskExecutionSummary_Contents"></a>

 ** ExecutionNumber **   <a name="managedintegrations-Type-OtaTaskExecutionSummary-ExecutionNumber"></a>
The execution number of the over-the-air (OTA) task execution summary.
Type: Long
Required: No

 ** LastUpdatedAt **   <a name="managedintegrations-Type-OtaTaskExecutionSummary-LastUpdatedAt"></a>
The timestamp value of when the over-the-air (OTA) task execution summary was last updated.
Type: Timestamp
Required: No

 ** QueuedAt **   <a name="managedintegrations-Type-OtaTaskExecutionSummary-QueuedAt"></a>
The timestamp value of when the over-the-air (OTA) task execution summary is targeted to start.
Type: Timestamp
Required: No

 ** RetryAttempt **   <a name="managedintegrations-Type-OtaTaskExecutionSummary-RetryAttempt"></a>
The number of retry attempts for starting the over-the-air (OTA) task execution summary after a failed attempt.
Type: Integer
Required: No

 ** StartedAt **   <a name="managedintegrations-Type-OtaTaskExecutionSummary-StartedAt"></a>
The timestamp value of when the over-the-air (OTA) task execution summary started.
Type: Timestamp
Required: No

 ** Status **   <a name="managedintegrations-Type-OtaTaskExecutionSummary-Status"></a>
The status of the over-the-air (OTA) task execution summary.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT | REJECTED | REMOVED | CANCELED`
Required: No

## See Also
<a name="API_OtaTaskExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/OtaTaskExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/OtaTaskExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/OtaTaskExecutionSummary)
