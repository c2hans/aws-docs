---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TuningJobCompletionCriteria.html
---

# TuningJobCompletionCriteria
<a name="API_TuningJobCompletionCriteria"></a>

The job completion criteria.

## Contents
<a name="API_TuningJobCompletionCriteria_Contents"></a>

 ** BestObjectiveNotImproving **   <a name="sagemaker-Type-TuningJobCompletionCriteria-BestObjectiveNotImproving"></a>
A flag to stop your hyperparameter tuning job if model performance fails to improve as evaluated against an objective function.
Type: [BestObjectiveNotImproving](API_BestObjectiveNotImproving.md) object
Required: No

 ** ConvergenceDetected **   <a name="sagemaker-Type-TuningJobCompletionCriteria-ConvergenceDetected"></a>
A flag to top your hyperparameter tuning job if automatic model tuning (AMT) has detected that your model has converged as evaluated against your objective function.
Type: [ConvergenceDetected](API_ConvergenceDetected.md) object
Required: No

 ** TargetObjectiveMetricValue **   <a name="sagemaker-Type-TuningJobCompletionCriteria-TargetObjectiveMetricValue"></a>
The value of the objective metric.
Type: Float
Required: No

## See Also
<a name="API_TuningJobCompletionCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TuningJobCompletionCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TuningJobCompletionCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TuningJobCompletionCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
