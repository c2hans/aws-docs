---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iam-role-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IAM::Role Tag
<a name="aws-properties-iam-role-tag"></a>

A structure that represents user-provided metadata that can be associated with an IAM resource. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

## Syntax
<a name="aws-properties-iam-role-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iam-role-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iam-role-tag-key)" : {{String}},
  "[Value](#cfn-iam-role-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iam-role-tag-syntax.yaml"></a>

```
  [Key](#cfn-iam-role-tag-key): {{String}}
  [Value](#cfn-iam-role-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iam-role-tag-properties"></a>

`Key`  <a name="cfn-iam-role-tag-key"></a>
The key name that can be used to look up or retrieve the associated value. For example, `Department` or `Cost Center` are common choices.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{Z}\p{N}_.:/=+\-@]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iam-role-tag-value"></a>
The value associated with this tag. For example, tags with a key name of `Department` could have values such as `Human Resources`, `Accounting`, and `Support`. Tags with a key name of `Cost Center` might have values that consist of the number associated with the different cost centers in your company. Typically, many resources have tags with the same key name but with different values.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
