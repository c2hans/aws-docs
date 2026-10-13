---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunction-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunction Tag
<a name="aws-properties-lambda-webfunction-tag"></a>

A key-value pair to associate with the web function.

## Syntax
<a name="aws-properties-lambda-webfunction-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunction-tag-syntax.json"></a>

```
{
  "[Key](#cfn-lambda-webfunction-tag-key)" : {{String}},
  "[Value](#cfn-lambda-webfunction-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-webfunction-tag-syntax.yaml"></a>

```
  [Key](#cfn-lambda-webfunction-tag-key): {{String}}
  [Value](#cfn-lambda-webfunction-tag-value): {{String}}
```

## Properties
<a name="aws-properties-lambda-webfunction-tag-properties"></a>

`Key`  <a name="cfn-lambda-webfunction-tag-key"></a>
The key for the tag. Tag keys are case sensitive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-lambda-webfunction-tag-value"></a>
The value for the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
