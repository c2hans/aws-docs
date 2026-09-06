---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ActivitySucceededEventDetails.html
---

# ActivitySucceededEventDetails
<a name="API_ActivitySucceededEventDetails"></a>

Contains details about an activity that successfully terminated during an execution.

## Contents
<a name="API_ActivitySucceededEventDetails_Contents"></a>

 ** output **   <a name="StepFunctions-Type-ActivitySucceededEventDetails-output"></a>
The JSON data output by the activity task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** outputDetails **   <a name="StepFunctions-Type-ActivitySucceededEventDetails-outputDetails"></a>
Contains details about the output of an execution history event.
Type: [HistoryEventExecutionDataDetails](API_HistoryEventExecutionDataDetails.md) object
Required: No

## See Also
<a name="API_ActivitySucceededEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ActivitySucceededEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ActivitySucceededEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ActivitySucceededEventDetails)
