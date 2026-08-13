---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentConfiguration.html
---

# AgentConfiguration
<a name="API_AgentConfiguration"></a>

 The response of [`ConfigureAgent`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html) that specifies if an agent profiles or not and for how long to return profiling data.

## Contents
<a name="API_AgentConfiguration_Contents"></a>

 ** periodInSeconds **   <a name="profiler-Type-AgentConfiguration-periodInSeconds"></a>
 How long a profiling agent should send profiling data using [`ConfigureAgent`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html). For example, if this is set to 300, the profiling agent calls [`ConfigureAgent`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html) every 5 minutes to submit the profiled data collected during that period.
Type: Integer
Required: Yes

 ** shouldProfile **   <a name="profiler-Type-AgentConfiguration-shouldProfile"></a>
 A `Boolean` that specifies whether the profiling agent collects profiling data or not. Set to `true` to enable profiling.
Type: Boolean
Required: Yes

 ** agentParameters **   <a name="profiler-Type-AgentConfiguration-agentParameters"></a>
 Parameters used by the profiler. The valid parameters are:
+  `MaxStackDepth` - The maximum depth of the stacks in the code that is represented in the profile. For example, if CodeGuru Profiler finds a method `A`, which calls method `B`, which calls method `C`, which calls method `D`, then the depth is 4. If the `maxDepth` is set to 2, then the profiler evaluates `A` and `B`.
+  `MemoryUsageLimitPercent` - The percentage of memory that is used by the profiler.
+  `MinimumTimeForReportingInMilliseconds` - The minimum time in milliseconds between sending reports.
+  `ReportingIntervalInMilliseconds` - The reporting interval in milliseconds used to report profiles.
+  `SamplingIntervalInMilliseconds` - The sampling interval in milliseconds that is used to profile samples.
Type: String to string map
Valid Keys: `SamplingIntervalInMilliseconds | ReportingIntervalInMilliseconds | MinimumTimeForReportingInMilliseconds | MemoryUsageLimitPercent | MaxStackDepth`
Required: No

## See Also
<a name="API_AgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/AgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/AgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/AgentConfiguration)
