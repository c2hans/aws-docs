---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_LambdaFunctionStartedEventAttributes.html
---

# LambdaFunctionStartedEventAttributes
<a name="API_LambdaFunctionStartedEventAttributes"></a>

Provides the details of the `LambdaFunctionStarted` event. It isn't set for other event types.

## Contents
<a name="API_LambdaFunctionStartedEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-LambdaFunctionStartedEventAttributes-scheduledEventId"></a>
The ID of the `LambdaFunctionScheduled` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
Type: Long
Required: Yes

## See Also
<a name="API_LambdaFunctionStartedEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/LambdaFunctionStartedEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/LambdaFunctionStartedEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/LambdaFunctionStartedEventAttributes)
