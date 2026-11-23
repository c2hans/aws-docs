---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_EventActorDetail.html
---

# EventActorDetail

The details of an event actor, returned by [GetEventActor](API_GetEventActor.md).

## Contents
<a name="API_EventActorDetail_Contents"></a>

 ** Summary **   <a name="WAF-Type-EventActorDetail-Summary"></a>
The latest observed attributes of the event actor.
Type: [EventActorDetailSummary](API_EventActorDetailSummary.md) object
Required: Yes

 ** Changes **   <a name="WAF-Type-EventActorDetail-Changes"></a>
The history of changes to the network attributes of the event actor, ordered from oldest to newest. The list contains up to 20 entries.
Type: Array of [EventActorChange](API_EventActorChange.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** Events **   <a name="WAF-Type-EventActorDetail-Events"></a>
The API security events that the event actor is associated with. The list contains up to 20 events.
Type: Array of [RelatedEvent](API_RelatedEvent.md) objects
Array Members: Maximum number of 20 items.
Required: No

## See Also
<a name="API_EventActorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/EventActorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/EventActorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/EventActorDetail)
