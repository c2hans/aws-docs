---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus.html
---

# ProfilingStatus
<a name="API_ProfilingStatus"></a>

 Profiling status includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile.

## Contents
<a name="API_ProfilingStatus_Contents"></a>

 ** latestAgentOrchestratedAt **   <a name="profiler-Type-ProfilingStatus-latestAgentOrchestratedAt"></a>
The date and time when the profiling agent most recently pinged back. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: No

 ** latestAgentProfileReportedAt **   <a name="profiler-Type-ProfilingStatus-latestAgentProfileReportedAt"></a>
The date and time when the most recent profile was received. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: No

 ** latestAggregatedProfile **   <a name="profiler-Type-ProfilingStatus-latestAggregatedProfile"></a>
 An [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html) object that contains the aggregation period and start time for an aggregated profile.
Type: [AggregatedProfileTime](API_AggregatedProfileTime.md) object
Required: No

## See Also
<a name="API_ProfilingStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/ProfilingStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/ProfilingStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/ProfilingStatus)
