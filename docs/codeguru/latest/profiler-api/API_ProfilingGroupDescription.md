---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html
---

# ProfilingGroupDescription
<a name="API_ProfilingGroupDescription"></a>

 Contains information about a profiling group.

## Contents
<a name="API_ProfilingGroupDescription_Contents"></a>

 ** agentOrchestrationConfig **   <a name="profiler-Type-ProfilingGroupDescription-agentOrchestrationConfig"></a>
 An [`AgentOrchestrationConfig`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig.html) object that indicates if the profiling group is enabled for profiled or not.
Type: [AgentOrchestrationConfig](API_AgentOrchestrationConfig.md) object
Required: No

 ** arn **   <a name="profiler-Type-ProfilingGroupDescription-arn"></a>
The Amazon Resource Name (ARN) identifying the profiling group resource.
Type: String
Required: No

 ** computePlatform **   <a name="profiler-Type-ProfilingGroupDescription-computePlatform"></a>
 The compute platform of the profiling group. If it is set to `AWSLambda`, then the profiled application runs on AWS Lambda. If it is set to `Default`, then the profiled application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. The default is `Default`.
Type: String
Valid Values: `Default | AWSLambda`
Required: No

 ** createdAt **   <a name="profiler-Type-ProfilingGroupDescription-createdAt"></a>
The time when the profiling group was created. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: No

 ** name **   <a name="profiler-Type-ProfilingGroupDescription-name"></a>
The name of the profiling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: No

 ** profilingStatus **   <a name="profiler-Type-ProfilingGroupDescription-profilingStatus"></a>
 A [`ProfilingStatus`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus.html) object that includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile.
Type: [ProfilingStatus](API_ProfilingStatus.md) object
Required: No

 ** tags **   <a name="profiler-Type-ProfilingGroupDescription-tags"></a>
 A list of the tags that belong to this profiling group.
Type: String to string map
Required: No

 ** updatedAt **   <a name="profiler-Type-ProfilingGroupDescription-updatedAt"></a>
 The date and time when the profiling group was last updated. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.
Type: Timestamp
Required: No

## See Also
<a name="API_ProfilingGroupDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/ProfilingGroupDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/ProfilingGroupDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/ProfilingGroupDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Profiler. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
