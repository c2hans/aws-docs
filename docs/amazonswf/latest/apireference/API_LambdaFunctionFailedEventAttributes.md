---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_LambdaFunctionFailedEventAttributes.html
---

# LambdaFunctionFailedEventAttributes
<a name="API_LambdaFunctionFailedEventAttributes"></a>

Provides the details of the `LambdaFunctionFailed` event. It isn't set for other event types.

## Contents
<a name="API_LambdaFunctionFailedEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-LambdaFunctionFailedEventAttributes-scheduledEventId"></a>
The ID of the `LambdaFunctionScheduled` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-LambdaFunctionFailedEventAttributes-startedEventId"></a>
The ID of the `LambdaFunctionStarted` event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** details **   <a name="SWF-Type-LambdaFunctionFailedEventAttributes-details"></a>
The details of the failure.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

 ** reason **   <a name="SWF-Type-LambdaFunctionFailedEventAttributes-reason"></a>
The reason provided for the failure.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_LambdaFunctionFailedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/LambdaFunctionFailedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/LambdaFunctionFailedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/LambdaFunctionFailedEventAttributes)
