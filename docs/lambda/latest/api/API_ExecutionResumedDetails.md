---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ExecutionResumedDetails.html
---

# ExecutionResumedDetails
<a name="API_ExecutionResumedDetails"></a>

Details about a [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) that resumed. The event timestamp is when the execution resumed.

## Contents
<a name="API_ExecutionResumedDetails_Contents"></a>

 ** ResumeRequestTimestamp **   <a name="lambda-Type-ExecutionResumedDetails-ResumeRequestTimestamp"></a>
The date and time when you requested the resume, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).
Type: Timestamp
Required: Yes

 ** Reason **   <a name="lambda-Type-ExecutionResumedDetails-Reason"></a>
The reason that you provided when you resumed the execution.
Type: [EventResumeReason](API_EventResumeReason.md) object
Required: No

## See Also
<a name="API_ExecutionResumedDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ExecutionResumedDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ExecutionResumedDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ExecutionResumedDetails)
