---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig.html
---

# AgentOrchestrationConfig
<a name="API_AgentOrchestrationConfig"></a>

 Specifies whether profiling is enabled or disabled for a profiling group. It is used by [`ConfigureAgent`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html) to enable or disable profiling for a profiling group.

## Contents
<a name="API_AgentOrchestrationConfig_Contents"></a>

 ** profilingEnabled **   <a name="profiler-Type-AgentOrchestrationConfig-profilingEnabled"></a>
 A `Boolean` that specifies whether the profiling agent collects profiling data or not. Set to `true` to enable profiling.
Type: Boolean
Required: Yes

## See Also
<a name="API_AgentOrchestrationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/AgentOrchestrationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/AgentOrchestrationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/AgentOrchestrationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
