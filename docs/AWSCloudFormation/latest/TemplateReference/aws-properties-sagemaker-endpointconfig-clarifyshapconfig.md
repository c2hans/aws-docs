---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-clarifyshapconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ClarifyShapConfig
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapconfig"></a>

The configuration for SHAP analysis using SageMaker Clarify Explainer.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapconfig-syntax.json"></a>

```
{
  "[NumberOfSamples](#cfn-sagemaker-endpointconfig-clarifyshapconfig-numberofsamples)" : {{Integer}},
  "[Seed](#cfn-sagemaker-endpointconfig-clarifyshapconfig-seed)" : {{Integer}},
  "[ShapBaselineConfig](#cfn-sagemaker-endpointconfig-clarifyshapconfig-shapbaselineconfig)" : {{ClarifyShapBaselineConfig}},
  "[TextConfig](#cfn-sagemaker-endpointconfig-clarifyshapconfig-textconfig)" : {{ClarifyTextConfig}},
  "[UseLogit](#cfn-sagemaker-endpointconfig-clarifyshapconfig-uselogit)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapconfig-syntax.yaml"></a>

```
  [NumberOfSamples](#cfn-sagemaker-endpointconfig-clarifyshapconfig-numberofsamples): {{Integer}}
  [Seed](#cfn-sagemaker-endpointconfig-clarifyshapconfig-seed): {{Integer}}
  [ShapBaselineConfig](#cfn-sagemaker-endpointconfig-clarifyshapconfig-shapbaselineconfig): {{
    ClarifyShapBaselineConfig}}
  [TextConfig](#cfn-sagemaker-endpointconfig-clarifyshapconfig-textconfig): {{
    ClarifyTextConfig}}
  [UseLogit](#cfn-sagemaker-endpointconfig-clarifyshapconfig-uselogit): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapconfig-properties"></a>

`NumberOfSamples`  <a name="cfn-sagemaker-endpointconfig-clarifyshapconfig-numberofsamples"></a>
The number of samples to be used for analysis by the Kernal SHAP algorithm.
The number of samples determines the size of the synthetic dataset, which has an impact on latency of explainability requests. For more information, see the **Synthetic data** of [Configure and create an endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Seed`  <a name="cfn-sagemaker-endpointconfig-clarifyshapconfig-seed"></a>
The starting value used to initialize the random number generator in the explainer. Provide a value for this parameter to obtain a deterministic SHAP result.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ShapBaselineConfig`  <a name="cfn-sagemaker-endpointconfig-clarifyshapconfig-shapbaselineconfig"></a>
The configuration for the SHAP baseline of the Kernal SHAP algorithm.
*Required*: Yes
*Type*: [ClarifyShapBaselineConfig](aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TextConfig`  <a name="cfn-sagemaker-endpointconfig-clarifyshapconfig-textconfig"></a>
A parameter that indicates if text features are treated as text and explanations are provided for individual units of text. Required for natural language processing (NLP) explainability only.
*Required*: No
*Type*: [ClarifyTextConfig](aws-properties-sagemaker-endpointconfig-clarifytextconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UseLogit`  <a name="cfn-sagemaker-endpointconfig-clarifyshapconfig-uselogit"></a>
A Boolean toggle to indicate if you want to use the logit function (true) or log-odds units (false) for model predictions. Defaults to false.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
