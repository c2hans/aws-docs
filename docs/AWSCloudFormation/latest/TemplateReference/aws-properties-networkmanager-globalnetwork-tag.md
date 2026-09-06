---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-globalnetwork-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::GlobalNetwork Tag
<a name="aws-properties-networkmanager-globalnetwork-tag"></a>

Describes a tag.

## Syntax
<a name="aws-properties-networkmanager-globalnetwork-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-globalnetwork-tag-syntax.json"></a>

```
{
  "[Key](#cfn-networkmanager-globalnetwork-tag-key)" : {{String}},
  "[Value](#cfn-networkmanager-globalnetwork-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkmanager-globalnetwork-tag-syntax.yaml"></a>

```
  [Key](#cfn-networkmanager-globalnetwork-tag-key): {{String}}
  [Value](#cfn-networkmanager-globalnetwork-tag-value): {{String}}
```

## Properties
<a name="aws-properties-networkmanager-globalnetwork-tag-properties"></a>

`Key`  <a name="cfn-networkmanager-globalnetwork-tag-key"></a>
The tag key.
Constraints: Maximum length of 128 characters.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networkmanager-globalnetwork-tag-value"></a>
The tag value.
Constraints: Maximum length of 256 characters.
*Required*: Yes
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `0`
*Maximum*: `10000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
