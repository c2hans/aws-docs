---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_EventBridgeParameters.html
---

# EventBridgeParameters
<a name="API_EventBridgeParameters"></a>

The templated target type for the EventBridge [https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) API operation.

## Contents
<a name="API_EventBridgeParameters_Contents"></a>

 ** DetailType **   <a name="scheduler-Type-EventBridgeParameters-DetailType"></a>
A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Source **   <a name="scheduler-Type-EventBridgeParameters-Source"></a>
The source of the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(?=[/\.\-_A-Za-z0-9]+)((?!aws\.).*)|(\$(\.[\w_-]+(\[(\d+|\*)\])*)*)`
Required: Yes

## See Also
<a name="API_EventBridgeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/EventBridgeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/EventBridgeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/EventBridgeParameters)
