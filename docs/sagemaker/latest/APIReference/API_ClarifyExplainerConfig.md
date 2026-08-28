---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClarifyExplainerConfig.html
---

# ClarifyExplainerConfig
<a name="API_ClarifyExplainerConfig"></a>

The configuration parameters for the SageMaker Clarify explainer.

## Contents
<a name="API_ClarifyExplainerConfig_Contents"></a>

 ** ShapConfig **   <a name="sagemaker-Type-ClarifyExplainerConfig-ShapConfig"></a>
The configuration for SHAP analysis.
Type: [ClarifyShapConfig](API_ClarifyShapConfig.md) object
Required: Yes

 ** EnableExplanations **   <a name="sagemaker-Type-ClarifyExplainerConfig-EnableExplanations"></a>
A JMESPath boolean expression used to filter which records to explain. Explanations are activated by default. See [`EnableExplanations`](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable)for additional information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** InferenceConfig **   <a name="sagemaker-Type-ClarifyExplainerConfig-InferenceConfig"></a>
The inference configuration parameter for the model container.
Type: [ClarifyInferenceConfig](API_ClarifyInferenceConfig.md) object
Required: No

## See Also
<a name="API_ClarifyExplainerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClarifyExplainerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClarifyExplainerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClarifyExplainerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
