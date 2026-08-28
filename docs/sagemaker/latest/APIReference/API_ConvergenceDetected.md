---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html
---

# ConvergenceDetected
<a name="API_ConvergenceDetected"></a>

A flag to indicating that automatic model tuning (AMT) has detected model convergence, defined as a lack of significant improvement (1% or less) against an objective metric.

## Contents
<a name="API_ConvergenceDetected_Contents"></a>

 ** CompleteOnConvergence **   <a name="sagemaker-Type-ConvergenceDetected-CompleteOnConvergence"></a>
A flag to stop a tuning job once AMT has detected that the job has converged.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

## See Also
<a name="API_ConvergenceDetected_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ConvergenceDetected)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ConvergenceDetected)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ConvergenceDetected)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
