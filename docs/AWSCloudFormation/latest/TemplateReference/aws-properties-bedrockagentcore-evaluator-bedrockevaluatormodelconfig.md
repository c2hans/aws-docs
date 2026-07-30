---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator BedrockEvaluatorModelConfig
<a name="aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig"></a>

 The Amazon Bedrock model configuration for evaluation.

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-syntax.json"></a>

```
{
  "[AdditionalModelRequestFields](#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-additionalmodelrequestfields)" : {{Json}},
  "[InferenceConfig](#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-inferenceconfig)" : {{InferenceConfiguration}},
  "[ModelId](#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-modelid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-syntax.yaml"></a>

```
  [AdditionalModelRequestFields](#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-additionalmodelrequestfields): {{Json}}
  [InferenceConfig](#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-inferenceconfig): {{
    InferenceConfiguration}}
  [ModelId](#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-modelid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-properties"></a>

`AdditionalModelRequestFields`  <a name="cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-additionalmodelrequestfields"></a>
 Additional model-specific request fields to customize model behavior beyond the standard inference configuration.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceConfig`  <a name="cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-inferenceconfig"></a>
 The inference configuration parameters that control model behavior during evaluation, including temperature, token limits, and sampling settings.
*Required*: No
*Type*: [InferenceConfiguration](aws-properties-bedrockagentcore-evaluator-inferenceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-modelid"></a>
 The identifier of the Amazon Bedrock model to use for evaluation. Must be a supported foundation model available in your region.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
