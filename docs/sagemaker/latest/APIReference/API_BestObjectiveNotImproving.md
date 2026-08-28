---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BestObjectiveNotImproving.html
---

# BestObjectiveNotImproving
<a name="API_BestObjectiveNotImproving"></a>

A structure that keeps track of which training jobs launched by your hyperparameter tuning job are not improving model performance as evaluated against an objective function.

## Contents
<a name="API_BestObjectiveNotImproving_Contents"></a>

 ** MaxNumberOfTrainingJobsNotImproving **   <a name="sagemaker-Type-BestObjectiveNotImproving-MaxNumberOfTrainingJobsNotImproving"></a>
The number of training jobs that have failed to improve model performance by 1% or greater over prior training jobs as evaluated against an objective function.
Type: Integer
Valid Range: Minimum value of 3.
Required: No

## See Also
<a name="API_BestObjectiveNotImproving_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/BestObjectiveNotImproving)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/BestObjectiveNotImproving)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/BestObjectiveNotImproving)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
