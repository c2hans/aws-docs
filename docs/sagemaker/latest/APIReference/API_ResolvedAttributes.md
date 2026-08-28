---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResolvedAttributes.html
---

# ResolvedAttributes
<a name="API_ResolvedAttributes"></a>

The resolved attributes.

## Contents
<a name="API_ResolvedAttributes_Contents"></a>

 ** AutoMLJobObjective **   <a name="sagemaker-Type-ResolvedAttributes-AutoMLJobObjective"></a>
Specifies a metric to minimize or maximize as the objective of an AutoML job.
Type: [AutoMLJobObjective](API_AutoMLJobObjective.md) object
Required: No

 ** CompletionCriteria **   <a name="sagemaker-Type-ResolvedAttributes-CompletionCriteria"></a>
How long a job is allowed to run, or how many candidates a job is allowed to generate.
Type: [AutoMLJobCompletionCriteria](API_AutoMLJobCompletionCriteria.md) object
Required: No

 ** ProblemType **   <a name="sagemaker-Type-ResolvedAttributes-ProblemType"></a>
The problem type.
Type: String
Valid Values: `BinaryClassification | MulticlassClassification | Regression`
Required: No

## See Also
<a name="API_ResolvedAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ResolvedAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ResolvedAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ResolvedAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
