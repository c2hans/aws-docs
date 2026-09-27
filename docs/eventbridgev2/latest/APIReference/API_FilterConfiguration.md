---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_FilterConfiguration.html
---

# FilterConfiguration
<a name="API_FilterConfiguration"></a>

Configuration for filtering events delivered to a subscriber. On CreateSubscriber, Filters is required and must contain at least one Filter with a non-empty Pattern. On UpdateSubscriber, an empty `FilterConfiguration:{}` clears the existing filter. Any non-empty shape (including `{Language:X}` without Filters) must contain a valid Filters list — same contract as CreateSubscriber. A non-empty Filters list overwrites; an omitted FilterConfiguration preserves existing state. All Filters are implicitly ANDed — an event must match every Filter to be delivered.

## Contents
<a name="API_FilterConfiguration_Contents"></a>

 ** Filters **   <a name="eventbridgev2-Type-FilterConfiguration-Filters"></a>
List of filters. An event must match every filter to be delivered.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Language **   <a name="eventbridgev2-Type-FilterConfiguration-Language"></a>
Defaults to EVENT\_BRIDGE\_PATTERN when not specified.
Type: String
Valid Values: `EVENT_BRIDGE_PATTERN`
Required: No

## See Also
<a name="API_FilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/FilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/FilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/FilterConfiguration)
