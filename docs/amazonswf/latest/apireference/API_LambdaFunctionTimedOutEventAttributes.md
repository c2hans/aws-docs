---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_LambdaFunctionTimedOutEventAttributes.html
---

# LambdaFunctionTimedOutEventAttributes
<a name="API_LambdaFunctionTimedOutEventAttributes"></a>

Provides details of the `LambdaFunctionTimedOut` event.

## Contents
<a name="API_LambdaFunctionTimedOutEventAttributes_Contents"></a>

 ** scheduledEventId **   <a name="SWF-Type-LambdaFunctionTimedOutEventAttributes-scheduledEventId"></a>
The ID of the `LambdaFunctionScheduled` event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** startedEventId **   <a name="SWF-Type-LambdaFunctionTimedOutEventAttributes-startedEventId"></a>
The ID of the `ActivityTaskStarted` event that was recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.
Type: Long
Required: Yes

 ** timeoutType **   <a name="SWF-Type-LambdaFunctionTimedOutEventAttributes-timeoutType"></a>
The type of the timeout that caused this event.
Type: String
Valid Values: `START_TO_CLOSE`
Required: No

## See Also
<a name="API_LambdaFunctionTimedOutEventAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/LambdaFunctionTimedOutEventAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/LambdaFunctionTimedOutEventAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/LambdaFunctionTimedOutEventAttributes)
