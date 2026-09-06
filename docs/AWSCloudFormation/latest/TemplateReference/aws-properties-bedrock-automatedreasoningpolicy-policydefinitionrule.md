---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-automatedreasoningpolicy-policydefinitionrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AutomatedReasoningPolicy PolicyDefinitionRule
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionrule"></a>

A rule within the policy definition that defines logical constraints.

## Syntax
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionrule-syntax.json"></a>

```
{
  "[AlternateExpression](#cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-alternateexpression)" : {{String}},
  "[Expression](#cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-expression)" : {{String}},
  "[Id](#cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionrule-syntax.yaml"></a>

```
  [AlternateExpression](#cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-alternateexpression): {{String}}
  [Expression](#cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-expression): {{String}}
  [Id](#cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-id): {{String}}
```

## Properties
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitionrule-properties"></a>

`AlternateExpression`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-alternateexpression"></a>
An alternative expression for the policy rule.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-expression"></a>
The logical expression that defines the rule.
*Required*: Yes
*Type*: String
*Pattern*: `^[\s\S]+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitionrule-id"></a>
The unique identifier for the policy definition rule.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z][0-9A-Z]{11}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
