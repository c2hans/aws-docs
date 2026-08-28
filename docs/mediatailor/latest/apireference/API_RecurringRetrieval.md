---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_RecurringRetrieval.html
---

# RecurringRetrieval
<a name="API_RecurringRetrieval"></a>

With recurring prefetch, MediaTailor automatically prefetches ads for every avail that occurs during the retrieval window. The following configurations describe the MediaTailor behavior when prefetching ads for a live event.

## Contents
<a name="API_RecurringRetrieval_Contents"></a>

 ** DelayAfterAvailEndSeconds **   <a name="mediatailor-Type-RecurringRetrieval-DelayAfterAvailEndSeconds"></a>
The number of seconds that MediaTailor waits after an ad avail before prefetching ads for the next avail. If not set, the default is 0 (no delay).
Type: Integer
Required: No

 ** DynamicVariables **   <a name="mediatailor-Type-RecurringRetrieval-DynamicVariables"></a>
The dynamic variables to use for substitution during prefetch requests to the ADS.
Type: String to string map
Required: No

 ** TrafficShapingRetrievalWindow **   <a name="mediatailor-Type-RecurringRetrieval-TrafficShapingRetrievalWindow"></a>
The configuration that tells AWS Elemental MediaTailor how many seconds to spread out requests to the ad decision server (ADS). Instead of sending ADS requests for all sessions at the same time, MediaTailor spreads the requests across the amount of time specified in the retrieval window.
Type: [TrafficShapingRetrievalWindow](API_TrafficShapingRetrievalWindow.md) object
Required: No

 ** TrafficShapingTpsConfiguration **   <a name="mediatailor-Type-RecurringRetrieval-TrafficShapingTpsConfiguration"></a>
The configuration for TPS-based traffic shaping. This approach limits requests to the ad decision server (ADS) based on transactions per second and concurrent users.
Type: [TrafficShapingTpsConfiguration](API_TrafficShapingTpsConfiguration.md) object
Required: No

 ** TrafficShapingType **   <a name="mediatailor-Type-RecurringRetrieval-TrafficShapingType"></a>
Indicates the type of traffic shaping used to limit the number of requests to the ADS at one time.
Type: String
Valid Values: `RETRIEVAL_WINDOW | TPS`
Required: No

## See Also
<a name="API_RecurringRetrieval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/RecurringRetrieval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/RecurringRetrieval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/RecurringRetrieval)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
