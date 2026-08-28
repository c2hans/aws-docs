---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ObjectiveStatusCounters.html
---

# ObjectiveStatusCounters
<a name="API_ObjectiveStatusCounters"></a>

Specifies the number of training jobs that this hyperparameter tuning job launched, categorized by the status of their objective metric. The objective metric status shows whether the final objective metric for the training job has been evaluated by the tuning job and used in the hyperparameter tuning process.

## Contents
<a name="API_ObjectiveStatusCounters_Contents"></a>

 ** Failed **   <a name="sagemaker-Type-ObjectiveStatusCounters-Failed"></a>
The number of training jobs whose final objective metric was not evaluated and used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Pending **   <a name="sagemaker-Type-ObjectiveStatusCounters-Pending"></a>
The number of training jobs that are in progress and pending evaluation of their final objective metric.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Succeeded **   <a name="sagemaker-Type-ObjectiveStatusCounters-Succeeded"></a>
The number of training jobs whose final objective metric was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ObjectiveStatusCounters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ObjectiveStatusCounters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ObjectiveStatusCounters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ObjectiveStatusCounters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
