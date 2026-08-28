---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationEventSummary.html
---

# AutomationEventSummary
<a name="API_automation_AutomationEventSummary"></a>

 A summary of automation events grouped by specified dimensions.

## Contents
<a name="API_automation_AutomationEventSummary_Contents"></a>

 ** dimensions **   <a name="computeoptimizer-Type-automation_AutomationEventSummary-dimensions"></a>
The dimensions used to group this summary, such as event status.
Type: Array of [SummaryDimension](API_automation_SummaryDimension.md) objects
Required: No

 ** key **   <a name="computeoptimizer-Type-automation_AutomationEventSummary-key"></a>
The key identifier for this summary grouping.
Type: String
Required: No

 ** timePeriod **   <a name="computeoptimizer-Type-automation_AutomationEventSummary-timePeriod"></a>
The time period covered by this summary, with inclusive start time and exclusive end time.
Type: [TimePeriod](API_automation_TimePeriod.md) object
Required: No

 ** total **   <a name="computeoptimizer-Type-automation_AutomationEventSummary-total"></a>
The aggregated totals for this summary, including event count and estimated savings.
Type: [SummaryTotals](API_automation_SummaryTotals.md) object
Required: No

## See Also
<a name="API_automation_AutomationEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/AutomationEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/AutomationEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/AutomationEventSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
