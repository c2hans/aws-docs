---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoParameter.html
---

# AutoParameter
<a name="API_AutoParameter"></a>

The name and an example value of the hyperparameter that you want to use in Autotune. If Automatic model tuning (AMT) determines that your hyperparameter is eligible for Autotune, an optimal hyperparameter range is selected for you.

## Contents
<a name="API_AutoParameter_Contents"></a>

 ** Name **   <a name="sagemaker-Type-AutoParameter-Name"></a>
The name of the hyperparameter to optimize using Autotune.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** ValueHint **   <a name="sagemaker-Type-AutoParameter-ValueHint"></a>
An example value of the hyperparameter to optimize using Autotune.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_AutoParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
