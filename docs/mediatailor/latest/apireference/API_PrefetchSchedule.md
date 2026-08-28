---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PrefetchSchedule.html
---

# PrefetchSchedule
<a name="API_PrefetchSchedule"></a>

A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see [Using ad prefetching](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html) in the *MediaTailor User Guide*.

## Contents
<a name="API_PrefetchSchedule_Contents"></a>

 ** Arn **   <a name="mediatailor-Type-PrefetchSchedule-Arn"></a>
The Amazon Resource Name (ARN) of the prefetch schedule.
Type: String
Required: Yes

 ** Name **   <a name="mediatailor-Type-PrefetchSchedule-Name"></a>
The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.
Type: String
Required: Yes

 ** PlaybackConfigurationName **   <a name="mediatailor-Type-PrefetchSchedule-PlaybackConfigurationName"></a>
The name of the playback configuration to create the prefetch schedule for.
Type: String
Required: Yes

 ** Consumption **   <a name="mediatailor-Type-PrefetchSchedule-Consumption"></a>
Consumption settings determine how, and when, MediaTailor places the prefetched ads into ad breaks for single prefetch schedules. Ad consumption occurs within a span of time that you define, called a *consumption window*. You can designate which ad breaks that MediaTailor fills with prefetch ads by setting avail matching criteria.
Type: [PrefetchConsumption](API_PrefetchConsumption.md) object
Required: No

 ** RecurringPrefetchConfiguration **   <a name="mediatailor-Type-PrefetchSchedule-RecurringPrefetchConfiguration"></a>
The settings that determine how and when MediaTailor prefetches ads and inserts them into ad breaks.
Type: [RecurringPrefetchConfiguration](API_RecurringPrefetchConfiguration.md) object
Required: No

 ** Retrieval **   <a name="mediatailor-Type-PrefetchSchedule-Retrieval"></a>
A complex type that contains settings for prefetch retrieval from the ad decision server (ADS).
Type: [PrefetchRetrieval](API_PrefetchRetrieval.md) object
Required: No

 ** ScheduleType **   <a name="mediatailor-Type-PrefetchSchedule-ScheduleType"></a>
The frequency that MediaTailor creates prefetch schedules. `SINGLE` indicates that this schedule applies to one ad break. `RECURRING` indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.
For more information about the prefetch types and when you might use each, see [Prefetching ads in AWS Elemental MediaTailor.](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html)
Type: String
Valid Values: `SINGLE | RECURRING`
Required: No

 ** StreamId **   <a name="mediatailor-Type-PrefetchSchedule-StreamId"></a>
An optional stream identifier that you can specify in order to prefetch for multiple streams that use the same playback configuration.
Type: String
Required: No

 ** tags **   <a name="mediatailor-Type-PrefetchSchedule-tags"></a>
The tags assigned to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
Type: String to string map
Required: No

## See Also
<a name="API_PrefetchSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/PrefetchSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/PrefetchSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/PrefetchSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
