---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ClarifyExplainerConfig
<a name="aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig"></a>

The configuration parameters for the SageMaker Clarify explainer.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig-syntax.json"></a>

```
{
  "[EnableExplanations](#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-enableexplanations)" : {{String}},
  "[InferenceConfig](#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-inferenceconfig)" : {{ClarifyInferenceConfig}},
  "[ShapConfig](#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-shapconfig)" : {{ClarifyShapConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig-syntax.yaml"></a>

```
  [EnableExplanations](#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-enableexplanations): {{String}}
  [InferenceConfig](#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-inferenceconfig): {{
    ClarifyInferenceConfig}}
  [ShapConfig](#cfn-sagemaker-endpointconfig-clarifyexplainerconfig-shapconfig): {{
    ClarifyShapConfig}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-clarifyexplainerconfig-properties"></a>

`EnableExplanations`  <a name="cfn-sagemaker-endpointconfig-clarifyexplainerconfig-enableexplanations"></a>
A JMESPath boolean expression used to filter which records to explain. Explanations are activated by default. See [`EnableExplanations`](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable)for additional information.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InferenceConfig`  <a name="cfn-sagemaker-endpointconfig-clarifyexplainerconfig-inferenceconfig"></a>
The inference configuration parameter for the model container.
*Required*: No
*Type*: [ClarifyInferenceConfig](aws-properties-sagemaker-endpointconfig-clarifyinferenceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ShapConfig`  <a name="cfn-sagemaker-endpointconfig-clarifyexplainerconfig-shapconfig"></a>
The configuration for SHAP analysis.
*Required*: Yes
*Type*: [ClarifyShapConfig](aws-properties-sagemaker-endpointconfig-clarifyshapconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
