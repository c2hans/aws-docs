---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_Summary.html
---

# Summary
<a name="API_Summary"></a>

The summary of a recommendation.

## Contents
<a name="API_Summary_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-Summary-name"></a>
The finding classification of the recommendation.
Type: String
Valid Values: `Underprovisioned | Overprovisioned | Optimized | NotOptimized`
Required: No

 ** reasonCodeSummaries **   <a name="computeoptimizer-Type-Summary-reasonCodeSummaries"></a>
An array of objects that summarize a finding reason code.
Type: Array of [ReasonCodeSummary](API_ReasonCodeSummary.md) objects
Required: No

 ** value **   <a name="computeoptimizer-Type-Summary-value"></a>
The value of the recommendation summary.
Type: Double
Required: No

## See Also
<a name="API_Summary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/Summary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/Summary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/Summary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
