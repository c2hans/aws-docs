---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::AutomatedReasoningPolicy PolicyDefinitionType
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontype"></a>

A custom type definition within the policy.

## Syntax
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontype-syntax.json"></a>

```
{
  "[Description](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-description)" : {{String}},
  "[Name](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-name)" : {{String}},
  "[Values](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-values)" : {{[ PolicyDefinitionTypeValue, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontype-syntax.yaml"></a>

```
  [Description](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-description): {{String}}
  [Name](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-name): {{String}}
  [Values](#cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-values): {{
    - PolicyDefinitionTypeValue}}
```

## Properties
<a name="aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontype-properties"></a>

`Description`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-description"></a>
A description of the custom type defined in the policy.
*Required*: No
*Type*: String
*Pattern*: `^[\s\S]+$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-name"></a>
The name of a custom type defined in the policy.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-bedrock-automatedreasoningpolicy-policydefinitiontype-values"></a>
The possible values for a custom type defined in the policy.
*Required*: Yes
*Type*: Array of [PolicyDefinitionTypeValue](aws-properties-bedrock-automatedreasoningpolicy-policydefinitiontypevalue.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
