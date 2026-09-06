---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PrefetchConsumption.html
---

# PrefetchConsumption
<a name="API_PrefetchConsumption"></a>

For single prefetch, describes how and when that MediaTailor places prefetched ads into upcoming ad breaks.

## Contents
<a name="API_PrefetchConsumption_Contents"></a>

 ** EndTime **   <a name="mediatailor-Type-PrefetchConsumption-EndTime"></a>
The time when MediaTailor no longer considers the prefetched ads for use in an ad break. MediaTailor automatically deletes prefetch schedules no less than seven days after the end time. If you'd like to manually delete the prefetch schedule, you can call `DeletePrefetchSchedule`.
Type: Timestamp
Required: Yes

 ** AvailMatchingCriteria **   <a name="mediatailor-Type-PrefetchConsumption-AvailMatchingCriteria"></a>
If you only want MediaTailor to insert prefetched ads into avails (ad breaks) that match specific dynamic variables, such as `scte.event_id`, set the avail matching criteria.
Type: Array of [AvailMatchingCriteria](API_AvailMatchingCriteria.md) objects
Required: No

 ** StartTime **   <a name="mediatailor-Type-PrefetchConsumption-StartTime"></a>
The time when prefetched ads are considered for use in an ad break. If you don't specify `StartTime`, the prefetched ads are available after MediaTailor retrieves them from the ad decision server.
Type: Timestamp
Required: No

## See Also
<a name="API_PrefetchConsumption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/PrefetchConsumption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/PrefetchConsumption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/PrefetchConsumption)
