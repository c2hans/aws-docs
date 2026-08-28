---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLResolvedAttributes.html
---

# AutoMLResolvedAttributes
<a name="API_AutoMLResolvedAttributes"></a>

The resolved attributes used to configure an AutoML job V2.

## Contents
<a name="API_AutoMLResolvedAttributes_Contents"></a>

 ** AutoMLJobObjective **   <a name="sagemaker-Type-AutoMLResolvedAttributes-AutoMLJobObjective"></a>
Specifies a metric to minimize or maximize as the objective of an AutoML job.
Type: [AutoMLJobObjective](API_AutoMLJobObjective.md) object
Required: No

 ** AutoMLProblemTypeResolvedAttributes **   <a name="sagemaker-Type-AutoMLResolvedAttributes-AutoMLProblemTypeResolvedAttributes"></a>
Defines the resolved attributes specific to a problem type.
Type: [AutoMLProblemTypeResolvedAttributes](API_AutoMLProblemTypeResolvedAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** CompletionCriteria **   <a name="sagemaker-Type-AutoMLResolvedAttributes-CompletionCriteria"></a>
How long a job is allowed to run, or how many candidates a job is allowed to generate.
Type: [AutoMLJobCompletionCriteria](API_AutoMLJobCompletionCriteria.md) object
Required: No

## See Also
<a name="API_AutoMLResolvedAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLResolvedAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLResolvedAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLResolvedAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
