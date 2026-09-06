---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-server-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server Tag
<a name="aws-properties-transfer-server-tag"></a>

Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called `Group` and assign the values `Research` and `Accounting` to that group.

## Syntax
<a name="aws-properties-transfer-server-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-server-tag-syntax.json"></a>

```
{
  "[Key](#cfn-transfer-server-tag-key)" : {{String}},
  "[Value](#cfn-transfer-server-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-server-tag-syntax.yaml"></a>

```
  [Key](#cfn-transfer-server-tag-key): {{String}}
  [Value](#cfn-transfer-server-tag-value): {{String}}
```

## Properties
<a name="aws-properties-transfer-server-tag-properties"></a>

`Key`  <a name="cfn-transfer-server-tag-key"></a>
The name assigned to the tag that you create.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-transfer-server-tag-value"></a>
Contains one or more values that you assigned to the key name you create.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
