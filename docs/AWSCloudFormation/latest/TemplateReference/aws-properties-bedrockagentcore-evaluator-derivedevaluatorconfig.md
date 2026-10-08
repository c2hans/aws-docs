---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-derivedevaluatorconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator DerivedEvaluatorConfig
<a name="aws-properties-bedrockagentcore-evaluator-derivedevaluatorconfig"></a>

<a name="aws-properties-bedrockagentcore-evaluator-derivedevaluatorconfig-description"></a>The `DerivedEvaluatorConfig` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Evaluator](aws-resource-bedrockagentcore-evaluator.md).

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-derivedevaluatorconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-derivedevaluatorconfig-syntax.json"></a>

```
{
  "[BaseEvaluatorId](#cfn-bedrockagentcore-evaluator-derivedevaluatorconfig-baseevaluatorid)" : {{String}},
  "[ModelConfig](#cfn-bedrockagentcore-evaluator-derivedevaluatorconfig-modelconfig)" : {{EvaluatorModelConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-derivedevaluatorconfig-syntax.yaml"></a>

```
  [BaseEvaluatorId](#cfn-bedrockagentcore-evaluator-derivedevaluatorconfig-baseevaluatorid): {{String}}
  [ModelConfig](#cfn-bedrockagentcore-evaluator-derivedevaluatorconfig-modelconfig): {{
    EvaluatorModelConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-derivedevaluatorconfig-properties"></a>

`BaseEvaluatorId`  <a name="cfn-bedrockagentcore-evaluator-derivedevaluatorconfig-baseevaluatorid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9._-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelConfig`  <a name="cfn-bedrockagentcore-evaluator-derivedevaluatorconfig-modelconfig"></a>
Property description not available.
*Required*: Yes
*Type*: [EvaluatorModelConfig](aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
