---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RelatedEvent.html
---

# RelatedEvent

An API security event that an event actor is associated with.

## Contents
<a name="API_RelatedEvent_Contents"></a>

 ** ApiPatterns **   <a name="WAF-Type-RelatedEvent-ApiPatterns"></a>
The API patterns that the event involves.
Type: Array of [ApiPattern](API_ApiPattern.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** Category **   <a name="WAF-Type-RelatedEvent-Category"></a>
The API security threat category of the event. For example, `API2:2023`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** Confidence **   <a name="WAF-Type-RelatedEvent-Confidence"></a>
The confidence level of the event detection: `LOW`, `MEDIUM`, or `HIGH`.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** EventId **   <a name="WAF-Type-RelatedEvent-EventId"></a>
The unique identifier of the event. You provide this to [GetEvent](API_GetEvent.md) to retrieve the details of the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: No

 ** Label **   <a name="WAF-Type-RelatedEvent-Label"></a>
The fully qualified name of the label that AWS WAF assigned to the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: No

 ** StartTime **   <a name="WAF-Type-RelatedEvent-StartTime"></a>
The time when the event started.
Type: Timestamp
Required: No

## See Also
<a name="API_RelatedEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RelatedEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RelatedEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RelatedEvent)
