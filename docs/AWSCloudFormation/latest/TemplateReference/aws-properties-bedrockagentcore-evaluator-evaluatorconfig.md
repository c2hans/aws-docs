---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-evaluatorconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator EvaluatorConfig
<a name="aws-properties-bedrockagentcore-evaluator-evaluatorconfig"></a>

 The configuration of the evaluator, including LLM-as-a-Judge settings for custom evaluators.

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-evaluatorconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-evaluatorconfig-syntax.json"></a>

```
{
  "[CodeBased](#cfn-bedrockagentcore-evaluator-evaluatorconfig-codebased)" : {{CodeBasedEvaluatorConfig}},
  "[Derived](#cfn-bedrockagentcore-evaluator-evaluatorconfig-derived)" : {{DerivedEvaluatorConfig}},
  "[LlmAsAJudge](#cfn-bedrockagentcore-evaluator-evaluatorconfig-llmasajudge)" : {{LlmAsAJudgeEvaluatorConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-evaluatorconfig-syntax.yaml"></a>

```
  [CodeBased](#cfn-bedrockagentcore-evaluator-evaluatorconfig-codebased): {{
    CodeBasedEvaluatorConfig}}
  [Derived](#cfn-bedrockagentcore-evaluator-evaluatorconfig-derived): {{
    DerivedEvaluatorConfig}}
  [LlmAsAJudge](#cfn-bedrockagentcore-evaluator-evaluatorconfig-llmasajudge): {{
    LlmAsAJudgeEvaluatorConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-evaluatorconfig-properties"></a>

`CodeBased`  <a name="cfn-bedrockagentcore-evaluator-evaluatorconfig-codebased"></a>
Property description not available.
*Required*: No
*Type*: [CodeBasedEvaluatorConfig](aws-properties-bedrockagentcore-evaluator-codebasedevaluatorconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Derived`  <a name="cfn-bedrockagentcore-evaluator-evaluatorconfig-derived"></a>
Property description not available.
*Required*: No
*Type*: [DerivedEvaluatorConfig](aws-properties-bedrockagentcore-evaluator-derivedevaluatorconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LlmAsAJudge`  <a name="cfn-bedrockagentcore-evaluator-evaluatorconfig-llmasajudge"></a>
 The LLM-as-a-Judge configuration that uses a language model to evaluate agent performance based on custom instructions and rating scales.
*Required*: No
*Type*: [LlmAsAJudgeEvaluatorConfig](aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
