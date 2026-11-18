---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_PauseDetails.html
---

# PauseDetails
<a name="API_PauseDetails"></a>

Details about a [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) that is pausing or paused.

## Contents
<a name="API_PauseDetails_Contents"></a>

 ** ExecutionTimeoutPaused **   <a name="lambda-Type-PauseDetails-ExecutionTimeoutPaused"></a>
Specifies whether the pause also pauses the execution timeout.
Type: Boolean
Required: Yes

 ** PauseRequestTimestamp **   <a name="lambda-Type-PauseDetails-PauseRequestTimestamp"></a>
The date and time when you requested the pause, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: Yes

 ** Reason **   <a name="lambda-Type-PauseDetails-Reason"></a>
The reason that you provided when you paused the execution. This field is only present if you set `IncludeExecutionData` to `true` in the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_PauseDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/PauseDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/PauseDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/PauseDetails)
