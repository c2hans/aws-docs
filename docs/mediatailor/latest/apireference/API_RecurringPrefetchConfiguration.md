---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_RecurringPrefetchConfiguration.html
---

# RecurringPrefetchConfiguration
<a name="API_RecurringPrefetchConfiguration"></a>

The configuration that defines how MediaTailor performs recurring prefetch.

## Contents
<a name="API_RecurringPrefetchConfiguration_Contents"></a>

 ** EndTime **   <a name="mediatailor-Type-RecurringPrefetchConfiguration-EndTime"></a>
The end time for the window that MediaTailor prefetches and inserts ads in a live event.
Type: Timestamp
Required: Yes

 ** RecurringConsumption **   <a name="mediatailor-Type-RecurringPrefetchConfiguration-RecurringConsumption"></a>
The settings that determine how and when MediaTailor places prefetched ads into upcoming ad breaks for recurring prefetch scedules.
Type: [RecurringConsumption](API_RecurringConsumption.md) object
Required: Yes

 ** RecurringRetrieval **   <a name="mediatailor-Type-RecurringPrefetchConfiguration-RecurringRetrieval"></a>
The configuration for prefetch ad retrieval from the ADS.
Type: [RecurringRetrieval](API_RecurringRetrieval.md) object
Required: Yes

 ** StartTime **   <a name="mediatailor-Type-RecurringPrefetchConfiguration-StartTime"></a>
The start time for the window that MediaTailor prefetches and inserts ads in a live event.
Type: Timestamp
Required: No

## See Also
<a name="API_RecurringPrefetchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/RecurringPrefetchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/RecurringPrefetchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/RecurringPrefetchConfiguration)
