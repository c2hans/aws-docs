---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator LlmAsAJudgeEvaluatorConfig
<a name="aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig"></a>

 The LLM-as-a-Judge configuration that uses a language model to evaluate agent performance based on custom instructions and rating scales.

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-syntax.json"></a>

```
{
  "[Instructions](#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-instructions)" : {{String}},
  "[ModelConfig](#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-modelconfig)" : {{EvaluatorModelConfig}},
  "[RatingScale](#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-ratingscale)" : {{RatingScale}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-syntax.yaml"></a>

```
  [Instructions](#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-instructions): {{String}}
  [ModelConfig](#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-modelconfig): {{
    EvaluatorModelConfig}}
  [RatingScale](#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-ratingscale): {{
    RatingScale}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-properties"></a>

`Instructions`  <a name="cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-instructions"></a>
 The evaluation instructions that guide the language model in assessing agent performance, including criteria and evaluation guidelines.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelConfig`  <a name="cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-modelconfig"></a>
 The model configuration that specifies which foundation model to use and how to configure it for evaluation.
*Required*: Yes
*Type*: [EvaluatorModelConfig](aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RatingScale`  <a name="cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-ratingscale"></a>
 The rating scale that defines how the evaluator should score agent performance, either numerical or categorical.
*Required*: Yes
*Type*: [RatingScale](aws-properties-bedrockagentcore-evaluator-ratingscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
