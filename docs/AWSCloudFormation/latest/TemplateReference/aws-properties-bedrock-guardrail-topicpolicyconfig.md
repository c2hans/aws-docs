---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-topicpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail TopicPolicyConfig
<a name="aws-properties-bedrock-guardrail-topicpolicyconfig"></a>

Contains details about topics that the guardrail should identify and deny.

## Syntax
<a name="aws-properties-bedrock-guardrail-topicpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-topicpolicyconfig-syntax.json"></a>

```
{
  "[TopicsConfig](#cfn-bedrock-guardrail-topicpolicyconfig-topicsconfig)" : {{[ TopicConfig, ... ]}},
  "[TopicsTierConfig](#cfn-bedrock-guardrail-topicpolicyconfig-topicstierconfig)" : {{TopicsTierConfig}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-topicpolicyconfig-syntax.yaml"></a>

```
  [TopicsConfig](#cfn-bedrock-guardrail-topicpolicyconfig-topicsconfig): {{
    - TopicConfig}}
  [TopicsTierConfig](#cfn-bedrock-guardrail-topicpolicyconfig-topicstierconfig): {{
    TopicsTierConfig}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-topicpolicyconfig-properties"></a>

`TopicsConfig`  <a name="cfn-bedrock-guardrail-topicpolicyconfig-topicsconfig"></a>
A list of policies related to topics that the guardrail should deny.
*Required*: Yes
*Type*: Array of [TopicConfig](aws-properties-bedrock-guardrail-topicconfig.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicsTierConfig`  <a name="cfn-bedrock-guardrail-topicpolicyconfig-topicstierconfig"></a>
The tier that your guardrail uses for denied topic filters.
*Required*: No
*Type*: [TopicsTierConfig](aws-properties-bedrock-guardrail-topicstierconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
