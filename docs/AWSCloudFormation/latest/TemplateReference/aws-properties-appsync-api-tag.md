---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-api-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Api Tag
<a name="aws-properties-appsync-api-tag"></a>

A tag (key-value pair) for this API.

## Syntax
<a name="aws-properties-appsync-api-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-api-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appsync-api-tag-key)" : {{String}},
  "[Value](#cfn-appsync-api-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-api-tag-syntax.yaml"></a>

```
  [Key](#cfn-appsync-api-tag-key): {{String}}
  [Value](#cfn-appsync-api-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appsync-api-tag-properties"></a>

`Key`  <a name="cfn-appsync-api-tag-key"></a>
Describes the key of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[ a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appsync-api-tag-value"></a>
Describes the value of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[\s\w+-=\.:/@]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
