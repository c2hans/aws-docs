---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html
---

# AggregatedProfileTime
<a name="API_AggregatedProfileTime"></a>

 Specifies the aggregation period and aggregation start time for an aggregated profile. An aggregated profile is used to collect posted agent profiles during an aggregation period. There are three possible aggregation periods (1 day, 1 hour, or 5 minutes).

## Contents
<a name="API_AggregatedProfileTime_Contents"></a>

 ** period **   <a name="profiler-Type-AggregatedProfileTime-period"></a>
 The aggregation period. This indicates the period during which an aggregation profile collects posted agent profiles for a profiling group. Use one of three valid durations that are specified using the ISO 8601 format.
+  `P1D` — 1 day
+  `PT1H` — 1 hour
+  `PT5M` — 5 minutes
Type: String
Valid Values: `PT5M | PT1H | P1D`
Required: No

 ** start **   <a name="profiler-Type-AggregatedProfileTime-start"></a>
 The time that aggregation of posted agent profiles for a profiling group starts. The aggregation profile contains profiles posted by the agent starting at this time for an aggregation period specified by the `period` property of the `AggregatedProfileTime` object.
 Specify `start` using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: No

## See Also
<a name="API_AggregatedProfileTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/AggregatedProfileTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/AggregatedProfileTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/AggregatedProfileTime)
