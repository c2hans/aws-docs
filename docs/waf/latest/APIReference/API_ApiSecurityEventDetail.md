---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ApiSecurityEventDetail.html
---

# ApiSecurityEventDetail

The API security details of an event.

## Contents
<a name="API_ApiSecurityEventDetail_Contents"></a>

 ** ApiPatterns **   <a name="WAF-Type-ApiSecurityEventDetail-ApiPatterns"></a>
The API patterns that the event involves. The list contains up to 20 API patterns.
Type: Array of [ApiPattern](API_ApiPattern.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** Category **   <a name="WAF-Type-ApiSecurityEventDetail-Category"></a>
The API security threat category of the event. For example, `API2:2023`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** Confidence **   <a name="WAF-Type-ApiSecurityEventDetail-Confidence"></a>
The confidence level of the event detection: `LOW`, `MEDIUM`, or `HIGH`.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** EventActors **   <a name="WAF-Type-ApiSecurityEventDetail-EventActors"></a>
The event actors that are associated with the event. The list contains up to 20 event actors. To retrieve the details of an event actor, provide its `EventActorId` to [GetEventActor](API_GetEventActor.md).
Type: Array of [EventActorReference](API_EventActorReference.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** Label **   <a name="WAF-Type-ApiSecurityEventDetail-Label"></a>
The fully qualified name of the label that AWS WAF assigned to the event. For example, `awswaf:managed:aws:api-security:credential-stuffing-high`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: No

 ** Timeline **   <a name="WAF-Type-ApiSecurityEventDetail-Timeline"></a>
The changes to the event's label, confidence, and API patterns over time, ordered from oldest to newest. The list contains up to 32 entries.
For [ListEvents](API_ListEvents.md) and [ListEventsByWebACL](API_ListEventsByWebACL.md), this is returned only if you specify `TIMELINE` in the request `Include` setting.
Type: Array of [EventTimelineEntry](API_EventTimelineEntry.md) objects
Array Members: Maximum number of 32 items.
Required: No

## See Also
<a name="API_ApiSecurityEventDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ApiSecurityEventDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ApiSecurityEventDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ApiSecurityEventDetail)
