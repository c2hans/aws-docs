---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivityScheduledEventDetails.html
---

# ActivityScheduledEventDetails
<a name="API_ActivityScheduledEventDetails"></a>

Contains details about an activity scheduled during an execution.

## Contents
<a name="API_ActivityScheduledEventDetails_Contents"></a>

 ** resource **   <a name="StepFunctions-Type-ActivityScheduledEventDetails-resource"></a>
The Amazon Resource Name (ARN) of the scheduled activity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** heartbeatInSeconds **   <a name="StepFunctions-Type-ActivityScheduledEventDetails-heartbeatInSeconds"></a>
The maximum allowed duration between two heartbeats for the activity task.
Type: Long
Required: No

 ** input **   <a name="StepFunctions-Type-ActivityScheduledEventDetails-input"></a>
The JSON data input to the activity task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** inputDetails **   <a name="StepFunctions-Type-ActivityScheduledEventDetails-inputDetails"></a>
Contains details about the input for an execution history event.
Type: [HistoryEventExecutionDataDetails](API_HistoryEventExecutionDataDetails.md) object
Required: No

 ** timeoutInSeconds **   <a name="StepFunctions-Type-ActivityScheduledEventDetails-timeoutInSeconds"></a>
The maximum allowed duration of the activity task.
Type: Long
Required: No

## See Also
<a name="API_ActivityScheduledEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ActivityScheduledEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ActivityScheduledEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ActivityScheduledEventDetails)
