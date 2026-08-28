---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-automatedreasoningpolicy-policydefinitionvariable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AutomatedReasoningPolicy PolicyDefinitionVariable
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionvariable"></a>

A variable defined within the policy that can be used in rules.

## Syntax
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionvariable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionvariable-syntax.json"></a>

```
{
  "[Description](#cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-description)" : {{String}},
  "[Name](#cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-name)" : {{String}},
  "[Type](#cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionvariable-syntax.yaml"></a>

```
  [Description](#cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-description): {{String}}
  [Name](#cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-name): {{String}}
  [Type](#cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionvariable-properties"></a>

`Description`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-description"></a>
A description of a variable defined in the policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[\s\S]+$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-name"></a>
The name of a variable defined in the policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitionvariable-type"></a>
The data type of a variable defined in the policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
