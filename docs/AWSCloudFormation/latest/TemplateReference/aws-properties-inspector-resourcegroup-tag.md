---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-inspector-resourcegroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Inspector::ResourceGroup Tag
<a name="aws-properties-inspector-resourcegroup-tag"></a>

A key and value pair. This data type is used as a request parameter in the [SetTagsForResource](https://docs.aws.amazon.com/inspector/v1/APIReference/API_SetTagsForResource.html) action and a response element in the [ListTagsForResource](https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListTagsForResource.html) action.

## Syntax
<a name="aws-properties-inspector-resourcegroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-inspector-resourcegroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-inspector-resourcegroup-tag-key)" : {{String}},
  "[Value](#cfn-inspector-resourcegroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-inspector-resourcegroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-inspector-resourcegroup-tag-key): {{String}}
  [Value](#cfn-inspector-resourcegroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-inspector-resourcegroup-tag-properties"></a>

`Key`  <a name="cfn-inspector-resourcegroup-tag-key"></a>
A tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-inspector-resourcegroup-tag-value"></a>
A value assigned to a tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
