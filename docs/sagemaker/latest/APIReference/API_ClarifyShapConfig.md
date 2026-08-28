---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClarifyShapConfig.html
---

# ClarifyShapConfig
<a name="API_ClarifyShapConfig"></a>

The configuration for SHAP analysis using SageMaker Clarify Explainer.

## Contents
<a name="API_ClarifyShapConfig_Contents"></a>

 ** ShapBaselineConfig **   <a name="sagemaker-Type-ClarifyShapConfig-ShapBaselineConfig"></a>
The configuration for the SHAP baseline of the Kernal SHAP algorithm.
Type: [ClarifyShapBaselineConfig](API_ClarifyShapBaselineConfig.md) object
Required: Yes

 ** NumberOfSamples **   <a name="sagemaker-Type-ClarifyShapConfig-NumberOfSamples"></a>
The number of samples to be used for analysis by the Kernal SHAP algorithm.
The number of samples determines the size of the synthetic dataset, which has an impact on latency of explainability requests. For more information, see the **Synthetic data** of [Configure and create an endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Seed **   <a name="sagemaker-Type-ClarifyShapConfig-Seed"></a>
The starting value used to initialize the random number generator in the explainer. Provide a value for this parameter to obtain a deterministic SHAP result.
Type: Integer
Required: No

 ** TextConfig **   <a name="sagemaker-Type-ClarifyShapConfig-TextConfig"></a>
A parameter that indicates if text features are treated as text and explanations are provided for individual units of text. Required for natural language processing (NLP) explainability only.
Type: [ClarifyTextConfig](API_ClarifyTextConfig.md) object
Required: No

 ** UseLogit **   <a name="sagemaker-Type-ClarifyShapConfig-UseLogit"></a>
A Boolean toggle to indicate if you want to use the logit function (true) or log-odds units (false) for model predictions. Defaults to false.
Type: Boolean
Required: No

## See Also
<a name="API_ClarifyShapConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClarifyShapConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClarifyShapConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClarifyShapConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
