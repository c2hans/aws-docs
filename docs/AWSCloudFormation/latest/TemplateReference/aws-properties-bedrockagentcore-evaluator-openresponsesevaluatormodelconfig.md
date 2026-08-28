---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator OpenResponsesEvaluatorModelConfig
<a name="aws-properties-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig"></a>

<a name="aws-properties-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-description"></a>The `OpenResponsesEvaluatorModelConfig` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Evaluator](aws-resource-bedrockagentcore-evaluator.md).

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-syntax.json"></a>

```
{
  "[MaxOutputTokens](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-maxoutputtokens)" : {{Integer}},
  "[ModelId](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-modelid)" : {{String}},
  "[Reasoning](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-reasoning)" : {{ReasoningConfiguration}},
  "[Temperature](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-temperature)" : {{Number}},
  "[TopP](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-syntax.yaml"></a>

```
  [MaxOutputTokens](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-maxoutputtokens): {{Integer}}
  [ModelId](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-modelid): {{String}}
  [Reasoning](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-reasoning): {{
    ReasoningConfiguration}}
  [Temperature](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-temperature): {{Number}}
  [TopP](#cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-properties"></a>

`MaxOutputTokens`  <a name="cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-maxoutputtokens"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-modelid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Reasoning`  <a name="cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-reasoning"></a>
Property description not available.
*Required*: No
*Type*: [ReasoningConfiguration](aws-properties-bedrockagentcore-evaluator-reasoningconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-temperature"></a>
Property description not available.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrockagentcore-evaluator-openresponsesevaluatormodelconfig-topp"></a>
Property description not available.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
