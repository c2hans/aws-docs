---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-automatedreasoningpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail AutomatedReasoningPolicyConfig
<a name="aws-properties-bedrock-guardrail-automatedreasoningpolicyconfig"></a>

Configuration settings for integrating Automated Reasoning policies with Amazon Bedrock Guardrails.

## Syntax
<a name="aws-properties-bedrock-guardrail-automatedreasoningpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-automatedreasoningpolicyconfig-syntax.json"></a>

```
{
  "[ConfidenceThreshold](#cfn-bedrock-guardrail-automatedreasoningpolicyconfig-confidencethreshold)" : {{Number}},
  "[Policies](#cfn-bedrock-guardrail-automatedreasoningpolicyconfig-policies)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-automatedreasoningpolicyconfig-syntax.yaml"></a>

```
  [ConfidenceThreshold](#cfn-bedrock-guardrail-automatedreasoningpolicyconfig-confidencethreshold): {{Number}}
  [Policies](#cfn-bedrock-guardrail-automatedreasoningpolicyconfig-policies): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-automatedreasoningpolicyconfig-properties"></a>

`ConfidenceThreshold`  <a name="cfn-bedrock-guardrail-automatedreasoningpolicyconfig-confidencethreshold"></a>
The minimum confidence level required for Automated Reasoning policy violations to trigger guardrail actions. Values range from 0.0 to 1.0.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Policies`  <a name="cfn-bedrock-guardrail-automatedreasoningpolicyconfig-policies"></a>
The list of Automated Reasoning policy ARNs that should be applied as part of this guardrail configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `15 | 1`
*Maximum*: `2048 | 2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
