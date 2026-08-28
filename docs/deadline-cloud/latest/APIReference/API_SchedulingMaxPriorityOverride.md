---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SchedulingMaxPriorityOverride.html
---

# SchedulingMaxPriorityOverride
<a name="API_SchedulingMaxPriorityOverride"></a>

Defines the override behavior for jobs at the maximum priority (100) in weighted balanced scheduling.

## Contents
<a name="API_SchedulingMaxPriorityOverride_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** alwaysScheduleFirst **   <a name="deadlinecloud-Type-SchedulingMaxPriorityOverride-alwaysScheduleFirst"></a>
Jobs at the maximum priority (100) are always scheduled before other jobs, regardless of the weighted scheduling formula. If multiple jobs have priority 100, ties are broken using the standard weighted formula.
Type: [SchedulingMaxPriorityOverrideAlwaysScheduleFirst](API_SchedulingMaxPriorityOverrideAlwaysScheduleFirst.md) object
Required: No

## See Also
<a name="API_SchedulingMaxPriorityOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SchedulingMaxPriorityOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SchedulingMaxPriorityOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SchedulingMaxPriorityOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
