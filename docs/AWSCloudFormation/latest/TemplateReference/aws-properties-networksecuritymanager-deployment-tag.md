---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networksecuritymanager-deployment-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkSecurityManager::Deployment Tag
<a name="aws-properties-networksecuritymanager-deployment-tag"></a>

A key-value pair to associate with a deployment. For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-networksecuritymanager-deployment-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networksecuritymanager-deployment-tag-syntax.json"></a>

```
{
  "[Key](#cfn-networksecuritymanager-deployment-tag-key)" : {{String}},
  "[Value](#cfn-networksecuritymanager-deployment-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networksecuritymanager-deployment-tag-syntax.yaml"></a>

```
  [Key](#cfn-networksecuritymanager-deployment-tag-key): {{String}}
  [Value](#cfn-networksecuritymanager-deployment-tag-value): {{String}}
```

## Properties
<a name="aws-properties-networksecuritymanager-deployment-tag-properties"></a>

`Key`  <a name="cfn-networksecuritymanager-deployment-tag-key"></a>
The key name of the tag. Specify a value that's 1 to 128 characters in length. The key can contain letters, numbers, spaces, and the characters `_`, `.`, `:`, `/`, `=`, `+`, `-`, and `@`. You can't prefix the key with `aws:`, because that prefix is reserved.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networksecuritymanager-deployment-tag-value"></a>
The value for the tag. Specify a value that's 0 to 256 characters in length. You can specify an empty string.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
