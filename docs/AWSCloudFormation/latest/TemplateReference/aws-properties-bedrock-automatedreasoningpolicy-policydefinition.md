---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-automatedreasoningpolicy-policydefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AutomatedReasoningPolicy PolicyDefinition
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinition"></a>

The complete policy definition containing rules, variables, and types.

## Syntax
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinition-syntax.json"></a>

```
{
  "[Rules](#cfn-bedrock-automatedreasoningpolicy-policydefinition-rules)" : {{[ PolicyDefinitionRule, ... ]}},
  "[Types](#cfn-bedrock-automatedreasoningpolicy-policydefinition-types)" : {{[ PolicyDefinitionType, ... ]}},
  "[Variables](#cfn-bedrock-automatedreasoningpolicy-policydefinition-variables)" : {{[ PolicyDefinitionVariable, ... ]}},
  "[Version](#cfn-bedrock-automatedreasoningpolicy-policydefinition-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinition-syntax.yaml"></a>

```
  [Rules](#cfn-bedrock-automatedreasoningpolicy-policydefinition-rules): {{
    - PolicyDefinitionRule}}
  [Types](#cfn-bedrock-automatedreasoningpolicy-policydefinition-types): {{
    - PolicyDefinitionType}}
  [Variables](#cfn-bedrock-automatedreasoningpolicy-policydefinition-variables): {{
    - PolicyDefinitionVariable}}
  [Version](#cfn-bedrock-automatedreasoningpolicy-policydefinition-version): {{String}}
```

## Properties
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinition-properties"></a>

`Rules`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinition-rules"></a>
The collection of rules that define the policy logic.
*Required*: No
*Type*: Array of [PolicyDefinitionRule](aws-properties-bedrock-automatedreasoningpolicy-policydefinitionrule.md)
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Types`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinition-types"></a>
The custom types defined within the policy definition.
*Required*: No
*Type*: Array of [PolicyDefinitionType](aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontype.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Variables`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinition-variables"></a>
The variables used within the policy definition.
*Required*: No
*Type*: Array of [PolicyDefinitionVariable](aws-properties-bedrock-automatedreasoningpolicy-policydefinitionvariable.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinition-version"></a>
The version of the policy definition.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
