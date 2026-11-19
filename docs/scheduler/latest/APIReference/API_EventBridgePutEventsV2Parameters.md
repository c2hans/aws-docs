---
source_url: https://docs.aws.amazon.com/scheduler/latest/APIReference/API_EventBridgePutEventsV2Parameters.html
---

# EventBridgePutEventsV2Parameters

The templated target type for the EventBridge Custom event bus (eventsv2) [PutEvents](https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutEvents.html) API operation.

## Contents
<a name="API_EventBridgePutEventsV2Parameters_Contents"></a>

 ** DetailType **   <a name="scheduler-Type-EventBridgePutEventsV2Parameters-DetailType"></a>
A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Source **   <a name="scheduler-Type-EventBridgePutEventsV2Parameters-Source"></a>
The source of the event. The source can't start with the `aws.` prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(?=[/\.\-_A-Za-z0-9]+)((?!aws\.).*)|(\$(\.[\w_-]+(\[(\d+|\*)\])*)*)`
Required: Yes

## See Also
<a name="API_EventBridgePutEventsV2Parameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/scheduler-2021-06-30/EventBridgePutEventsV2Parameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/EventBridgePutEventsV2Parameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/scheduler-2021-06-30/EventBridgePutEventsV2Parameters)
