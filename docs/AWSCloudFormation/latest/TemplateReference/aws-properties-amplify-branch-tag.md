---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-branch-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Branch Tag
<a name="aws-properties-amplify-branch-tag"></a>

The `Tag` property specifies a key-value pair for tagging an `AWS:Amplify::Branch` resource.

## Syntax
<a name="aws-properties-amplify-branch-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-branch-tag-syntax.json"></a>

```
{
  "[Key](#cfn-amplify-branch-tag-key)" : {{String}},
  "[Value](#cfn-amplify-branch-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-branch-tag-syntax.yaml"></a>

```
  [Key](#cfn-amplify-branch-tag-key): {{String}}
  [Value](#cfn-amplify-branch-tag-value): {{String}}
```

## Properties
<a name="aws-properties-amplify-branch-tag-properties"></a>

`Key`  <a name="cfn-amplify-branch-tag-key"></a>
Specifies the key for the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-amplify-branch-tag-value"></a>
Specifies the value for the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
