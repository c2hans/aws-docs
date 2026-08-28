---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PrefetchRetrieval.html
---

# PrefetchRetrieval
<a name="API_PrefetchRetrieval"></a>

A complex type that contains settings governing when MediaTailor prefetches ads, and which dynamic variables that MediaTailor includes in the request to the ad decision server.

## Contents
<a name="API_PrefetchRetrieval_Contents"></a>

 ** EndTime **   <a name="mediatailor-Type-PrefetchRetrieval-EndTime"></a>
The time when prefetch retrieval ends for the ad break. Prefetching will be attempted for manifest requests that occur at or before this time.
Type: Timestamp
Required: Yes

 ** DynamicVariables **   <a name="mediatailor-Type-PrefetchRetrieval-DynamicVariables"></a>
The dynamic variables to use for substitution during prefetch requests to the ad decision server (ADS).
You initially configure [dynamic variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html) for the ADS URL when you set up your playback configuration. When you specify `DynamicVariables` for prefetch retrieval, MediaTailor includes the dynamic variables in the request to the ADS.
Type: String to string map
Required: No

 ** StartTime **   <a name="mediatailor-Type-PrefetchRetrieval-StartTime"></a>
The time when prefetch retrievals can start for this break. Ad prefetching will be attempted for manifest requests that occur at or after this time. Defaults to the current time. If not specified, the prefetch retrieval starts as soon as possible.
Type: Timestamp
Required: No

 ** TrafficShapingRetrievalWindow **   <a name="mediatailor-Type-PrefetchRetrieval-TrafficShapingRetrievalWindow"></a>
The configuration that tells AWS Elemental MediaTailor how many seconds to spread out requests to the ad decision server (ADS). Instead of sending ADS requests for all sessions at the same time, MediaTailor spreads the requests across the amount of time specified in the retrieval window.
Type: [TrafficShapingRetrievalWindow](API_TrafficShapingRetrievalWindow.md) object
Required: No

 ** TrafficShapingTpsConfiguration **   <a name="mediatailor-Type-PrefetchRetrieval-TrafficShapingTpsConfiguration"></a>
The configuration for TPS-based traffic shaping. This approach limits requests to the ad decision server (ADS) based on transactions per second and concurrent users.
Type: [TrafficShapingTpsConfiguration](API_TrafficShapingTpsConfiguration.md) object
Required: No

 ** TrafficShapingType **   <a name="mediatailor-Type-PrefetchRetrieval-TrafficShapingType"></a>
Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.
Type: String
Valid Values: `RETRIEVAL_WINDOW | TPS`
Required: No

## See Also
<a name="API_PrefetchRetrieval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/PrefetchRetrieval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/PrefetchRetrieval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/PrefetchRetrieval)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
