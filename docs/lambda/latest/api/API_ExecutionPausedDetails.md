---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ExecutionPausedDetails.html
---

# ExecutionPausedDetails

Details about a [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) that paused. The event timestamp is when the execution paused.

## Contents
<a name="API_ExecutionPausedDetails_Contents"></a>

 ** ExecutionTimeoutPaused **   <a name="lambda-Type-ExecutionPausedDetails-ExecutionTimeoutPaused"></a>
Specifies whether the pause also paused the execution timeout.
Type: Boolean
Required: Yes

 ** PauseRequestTimestamp **   <a name="lambda-Type-ExecutionPausedDetails-PauseRequestTimestamp"></a>
The date and time when you requested the pause, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: Yes

 ** Reason **   <a name="lambda-Type-ExecutionPausedDetails-Reason"></a>
The reason that you provided when you paused the execution.
Type: [EventPauseReason](API_EventPauseReason.md) object
Required: No

## See Also
<a name="API_ExecutionPausedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ExecutionPausedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ExecutionPausedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ExecutionPausedDetails)
