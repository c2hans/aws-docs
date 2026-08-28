---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontypevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AutomatedReasoningPolicy PolicyDefinitionTypeValue
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontypevalue"></a>

A value associated with a custom type in the policy definition.

## Syntax
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-syntax.json"></a>

```
{
  "[Description](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-description)" : {{String}},
  "[Value](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-syntax.yaml"></a>

```
  [Description](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-description): {{String}}
  [Value](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-value): {{String}}
```

## Properties
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-properties"></a>

`Description`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-description"></a>
A description of the policy definition type value.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]+$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitiontypevalue-value"></a>
The value associated with a policy definition type.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
