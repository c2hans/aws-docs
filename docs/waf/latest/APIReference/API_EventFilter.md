---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_EventFilter.html
---

# EventFilter

A filter to narrow the events that are returned by [ListEvents](API_ListEvents.md) and [ListEventsByWebACL](API_ListEventsByWebACL.md).

## Contents
<a name="API_EventFilter_Contents"></a>

 ** Name **   <a name="WAF-Type-EventFilter-Name"></a>
The name of the field to filter on. Valid values:
+  `EVENT_CATEGORY` - Filter by event category. The only supported filter value is `API_SECURITY`.
+  `RESOURCE_ARN` - Filter by protected resource. The filter values are the Amazon Resource Name (ARN)s of the protected resources.
Type: String
Valid Values: `EVENT_CATEGORY | RESOURCE_ARN`
Required: Yes

 ** Values **   <a name="WAF-Type-EventFilter-Values"></a>
The values to filter on. You can specify up to 10 values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_EventFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/EventFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/EventFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/EventFilter)
