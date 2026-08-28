---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SchedulingConfiguration.html
---

# SchedulingConfiguration
<a name="API_SchedulingConfiguration"></a>

The scheduling configuration for a queue. Defines the strategy used to assign workers to jobs.

## Contents
<a name="API_SchedulingConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** priorityBalanced **   <a name="deadlinecloud-Type-SchedulingConfiguration-priorityBalanced"></a>
Workers are distributed evenly across all jobs at the highest priority level. When workers cannot be evenly divided, the extra workers are assigned to the jobs submitted earliest. If a job has fewer remaining tasks than its share of workers, the surplus workers are redistributed to other jobs at the same priority level.
Type: [PriorityBalancedSchedulingConfiguration](API_PriorityBalancedSchedulingConfiguration.md) object
Required: No

 ** priorityFifo **   <a name="deadlinecloud-Type-SchedulingConfiguration-priorityFifo"></a>
Workers are assigned to the highest-priority job first. When multiple jobs share the same priority, the job submitted earliest receives workers first. This is the default scheduling configuration for new queues.
Type: [PriorityFifoSchedulingConfiguration](API_PriorityFifoSchedulingConfiguration.md) object
Required: No

 ** weightedBalanced **   <a name="deadlinecloud-Type-SchedulingConfiguration-weightedBalanced"></a>
Workers are assigned to jobs based on a weighted formula that considers job priority, error count, submission time, and the number of tasks currently rendering. Each factor has a configurable weight that determines its influence on scheduling decisions.
Type: [WeightedBalancedSchedulingConfiguration](API_WeightedBalancedSchedulingConfiguration.md) object
Required: No

## See Also
<a name="API_SchedulingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SchedulingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SchedulingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SchedulingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
