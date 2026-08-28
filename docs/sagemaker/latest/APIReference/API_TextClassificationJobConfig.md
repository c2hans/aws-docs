---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextClassificationJobConfig.html
---

# TextClassificationJobConfig
<a name="API_TextClassificationJobConfig"></a>

The collection of settings used by an AutoML job V2 for the text classification problem type.

## Contents
<a name="API_TextClassificationJobConfig_Contents"></a>

 ** ContentColumn **   <a name="sagemaker-Type-TextClassificationJobConfig-ContentColumn"></a>
The name of the column used to provide the sentences to be classified. It should not be the same as the target column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** TargetLabelColumn **   <a name="sagemaker-Type-TextClassificationJobConfig-TargetLabelColumn"></a>
The name of the column used to provide the class labels. It should not be same as the content column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** CompletionCriteria **   <a name="sagemaker-Type-TextClassificationJobConfig-CompletionCriteria"></a>
How long a job is allowed to run, or how many candidates a job is allowed to generate.
Type: [AutoMLJobCompletionCriteria](API_AutoMLJobCompletionCriteria.md) object
Required: No

## See Also
<a name="API_TextClassificationJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TextClassificationJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TextClassificationJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TextClassificationJobConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
