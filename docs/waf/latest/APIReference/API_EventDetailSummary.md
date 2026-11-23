---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_EventDetailSummary.html
---

# EventDetailSummary

Information about an API security event, returned by [ListEvents](API_ListEvents.md), [ListEventsByWebACL](API_ListEventsByWebACL.md), and [GetEvent](API_GetEvent.md).

## Contents
<a name="API_EventDetailSummary_Contents"></a>

 ** EventId **   <a name="WAF-Type-EventDetailSummary-EventId"></a>
The unique identifier of the event. You provide this to [GetEvent](API_GetEvent.md) to retrieve the details of the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`
Required: Yes

 ** ApiSecurityEventDetail **   <a name="WAF-Type-EventDetailSummary-ApiSecurityEventDetail"></a>
The API security details of the event, such as the label, category, confidence, API patterns, and event actors.
Type: [ApiSecurityEventDetail](API_ApiSecurityEventDetail.md) object
Required: No

 ** EndTime **   <a name="WAF-Type-EventDetailSummary-EndTime"></a>
The time when the event ended. This is not populated while the event is ongoing.
Type: Timestamp
Required: No

 ** EventCategory **   <a name="WAF-Type-EventDetailSummary-EventCategory"></a>
The category of the event. The only supported value is `API_SECURITY`.
Type: String
Valid Values: `API_SECURITY`
Required: No

 ** EventStatus **   <a name="WAF-Type-EventDetailSummary-EventStatus"></a>
The current status of the event.
Type: String
Valid Values: `EVENT_STARTED | EVENT_IN_PROGRESS | EVENT_COMPLETED | EVENT_ENDED`
Required: No

 ** LastUpdatedTime **   <a name="WAF-Type-EventDetailSummary-LastUpdatedTime"></a>
The time when the event was last updated.
Type: Timestamp
Required: No

 ** ResourceArn **   <a name="WAF-Type-EventDetailSummary-ResourceArn"></a>
The Amazon Resource Name (ARN) of the protected resource that the event is associated with.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** StartTime **   <a name="WAF-Type-EventDetailSummary-StartTime"></a>
The time when the event started.
Type: Timestamp
Required: No

 ** WebAclArn **   <a name="WAF-Type-EventDetailSummary-WebAclArn"></a>
The Amazon Resource Name (ARN) of the web ACL that the event is associated with.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_EventDetailSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/EventDetailSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/EventDetailSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/EventDetailSummary)
