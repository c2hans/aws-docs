---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig EvaluatorReference
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference"></a>

 A reference to an evaluator used in the online evaluation configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference-syntax.json"></a>

```
{
  "[EvaluatorId](#cfn-bedrockagentcore-onlineevaluationconfig-evaluatorreference-evaluatorid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference-syntax.yaml"></a>

```
  [EvaluatorId](#cfn-bedrockagentcore-onlineevaluationconfig-evaluatorreference-evaluatorid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference-properties"></a>

`EvaluatorId`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-evaluatorreference-evaluatorid"></a>
 The unique identifier of the evaluator. Can reference builtin evaluators (e.g., `Builtin.Helpfulness`) or custom evaluators.
*Required*: Yes
*Type*: String
*Pattern*: `^(Builtin\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
