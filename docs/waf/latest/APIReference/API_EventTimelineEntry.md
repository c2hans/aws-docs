---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_EventTimelineEntry.html
---

# EventTimelineEntry

A change to the label, confidence, or API patterns of an API security event.

## Contents
<a name="API_EventTimelineEntry_Contents"></a>

 ** ApiPatterns **   <a name="WAF-Type-EventTimelineEntry-ApiPatterns"></a>
The API patterns that the event involved at the time of the change.
Type: Array of [ApiPattern](API_ApiPattern.md) objects
Array Members: Maximum number of 20 items.
Required: No

 ** ChangeTime **   <a name="WAF-Type-EventTimelineEntry-ChangeTime"></a>
The time of the change.
Type: Timestamp
Required: No

 ** Confidence **   <a name="WAF-Type-EventTimelineEntry-Confidence"></a>
The confidence level of the event detection at the time of the change: `LOW`, `MEDIUM`, or `HIGH`.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** Label **   <a name="WAF-Type-EventTimelineEntry-Label"></a>
The fully qualified name of the label that was assigned to the event at the time of the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: No

## See Also
<a name="API_EventTimelineEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/EventTimelineEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/EventTimelineEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/EventTimelineEntry)
