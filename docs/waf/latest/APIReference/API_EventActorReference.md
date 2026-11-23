---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_EventActorReference.html
---

# EventActorReference

A reference to an event actor that is associated with an API security event.

## Contents
<a name="API_EventActorReference_Contents"></a>

 ** EventActorId **   <a name="WAF-Type-EventActorReference-EventActorId"></a>
The unique identifier of the event actor. You provide this to [GetEventActor](API_GetEventActor.md) to retrieve the details of the event actor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: No

 ** EventActorValue **   <a name="WAF-Type-EventActorReference-EventActorValue"></a>
The observed identifier of the event actor. For example, a client IP address or an authentication fingerprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_EventActorReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/EventActorReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/EventActorReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/EventActorReference)
