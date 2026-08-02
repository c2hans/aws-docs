---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idnamespace-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdNamespace Tag
<a name="aws-properties-entityresolution-idnamespace-tag"></a>

The tags used to organize, track, or control access for this resource.

## Syntax
<a name="aws-properties-entityresolution-idnamespace-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idnamespace-tag-syntax.json"></a>

```
{
  "[Key](#cfn-entityresolution-idnamespace-tag-key)" : {{String}},
  "[Value](#cfn-entityresolution-idnamespace-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idnamespace-tag-syntax.yaml"></a>

```
  [Key](#cfn-entityresolution-idnamespace-tag-key): {{String}}
  [Value](#cfn-entityresolution-idnamespace-tag-value): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idnamespace-tag-properties"></a>

`Key`  <a name="cfn-entityresolution-idnamespace-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-entityresolution-idnamespace-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
