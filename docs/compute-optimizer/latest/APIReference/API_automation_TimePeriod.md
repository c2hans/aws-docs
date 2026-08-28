---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_TimePeriod.html
---

# TimePeriod
<a name="API_automation_TimePeriod"></a>

Defines a time range with inclusive start time and exclusive end time for filtering and analysis.

## Contents
<a name="API_automation_TimePeriod_Contents"></a>

 ** endTimeExclusive **   <a name="computeoptimizer-Type-automation_TimePeriod-endTimeExclusive"></a>
The end time of the period, exclusive. Events before this time are included.
Type: Timestamp
Required: No

 ** startTimeInclusive **   <a name="computeoptimizer-Type-automation_TimePeriod-startTimeInclusive"></a>
The start time of the period, inclusive. Events at or after this time are included.
Type: Timestamp
Required: No

## See Also
<a name="API_automation_TimePeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/TimePeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/TimePeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/TimePeriod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
