---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig Rule
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-rule"></a>

 The evaluation rule containing sampling configuration, filters, and session settings.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-rule-syntax.json"></a>

```
{
  "[Filters](#cfn-bedrockagentcore-onlineevaluationconfig-rule-filters)" : {{[ Filter, ... ]}},
  "[SamplingConfig](#cfn-bedrockagentcore-onlineevaluationconfig-rule-samplingconfig)" : {{SamplingConfig}},
  "[SessionConfig](#cfn-bedrockagentcore-onlineevaluationconfig-rule-sessionconfig)" : {{SessionConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-rule-syntax.yaml"></a>

```
  [Filters](#cfn-bedrockagentcore-onlineevaluationconfig-rule-filters): {{
    - Filter}}
  [SamplingConfig](#cfn-bedrockagentcore-onlineevaluationconfig-rule-samplingconfig): {{
    SamplingConfig}}
  [SessionConfig](#cfn-bedrockagentcore-onlineevaluationconfig-rule-sessionconfig): {{
    SessionConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-rule-properties"></a>

`Filters`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-rule-filters"></a>
 The list of filters that determine which agent traces should be included in the evaluation based on trace properties.
*Required*: No
*Type*: Array of [Filter](aws-properties-bedrockagentcore-onlineevaluationconfig-filter.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SamplingConfig`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-rule-samplingconfig"></a>
 The sampling configuration that determines what percentage of agent traces to evaluate.
*Required*: Yes
*Type*: [SamplingConfig](aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionConfig`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-rule-sessionconfig"></a>
 The session configuration that defines timeout settings for detecting when agent sessions are complete and ready for evaluation.
*Required*: No
*Type*: [SessionConfig](aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
