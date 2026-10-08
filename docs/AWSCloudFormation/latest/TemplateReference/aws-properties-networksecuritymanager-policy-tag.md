---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-policy-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Policy Tag
<a name="aws-properties-networksecuritymanager-policy-tag"></a>

A key-value pair to associate with a policy.

For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-networksecuritymanager-policy-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-policy-tag-syntax.json"></a>

```
{
  "[Key](#cfn-networksecuritymanager-policy-tag-key)" : {{String}},
  "[Value](#cfn-networksecuritymanager-policy-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-policy-tag-syntax.yaml"></a>

```
  [Key](#cfn-networksecuritymanager-policy-tag-key): {{String}}
  [Value](#cfn-networksecuritymanager-policy-tag-value): {{String}}
```

## Properties
<a name="aws-properties-networksecuritymanager-policy-tag-properties"></a>

`Key`  <a name="cfn-networksecuritymanager-policy-tag-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networksecuritymanager-policy-tag-value"></a>
The value for the tag. You can specify a value that's 0 to 256 characters in length.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
