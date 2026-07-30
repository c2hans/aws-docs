---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtableassociation-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTableAssociation Tag
<a name="aws-properties-cleanrooms-configuredtableassociation-tag"></a>

An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

## Syntax
<a name="aws-properties-cleanrooms-configuredtableassociation-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtableassociation-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cleanrooms-configuredtableassociation-tag-key)" : {{String}},
  "[Value](#cfn-cleanrooms-configuredtableassociation-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtableassociation-tag-syntax.yaml"></a>

```
  [Key](#cfn-cleanrooms-configuredtableassociation-tag-key): {{String}}
  [Value](#cfn-cleanrooms-configuredtableassociation-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtableassociation-tag-properties"></a>

`Key`  <a name="cfn-cleanrooms-configuredtableassociation-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cleanrooms-configuredtableassociation-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
