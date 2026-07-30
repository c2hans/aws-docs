---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator EvaluatorModelConfig
<a name="aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig"></a>

 The model configuration that specifies which foundation model to use and how to configure it for evaluation.

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig-syntax.json"></a>

```
{
  "[BedrockEvaluatorModelConfig](#cfn-bedrockagentcore-evaluator-evaluatormodelconfig-bedrockevaluatormodelconfig)" : {{BedrockEvaluatorModelConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig-syntax.yaml"></a>

```
  [BedrockEvaluatorModelConfig](#cfn-bedrockagentcore-evaluator-evaluatormodelconfig-bedrockevaluatormodelconfig): {{
    BedrockEvaluatorModelConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig-properties"></a>

`BedrockEvaluatorModelConfig`  <a name="cfn-bedrockagentcore-evaluator-evaluatormodelconfig-bedrockevaluatormodelconfig"></a>
 The Amazon Bedrock model configuration for evaluation.
*Required*: Yes
*Type*: [BedrockEvaluatorModelConfig](aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
