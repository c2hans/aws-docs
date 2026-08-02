---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-transitgatewaypeering-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::TransitGatewayPeering Tag
<a name="aws-properties-networkmanager-transitgatewaypeering-tag"></a>

Describes a tag.

## Syntax
<a name="aws-properties-networkmanager-transitgatewaypeering-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-transitgatewaypeering-tag-syntax.json"></a>

```
{
  "[Key](#cfn-networkmanager-transitgatewaypeering-tag-key)" : {{String}},
  "[Value](#cfn-networkmanager-transitgatewaypeering-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkmanager-transitgatewaypeering-tag-syntax.yaml"></a>

```
  [Key](#cfn-networkmanager-transitgatewaypeering-tag-key): {{String}}
  [Value](#cfn-networkmanager-transitgatewaypeering-tag-value): {{String}}
```

## Properties
<a name="aws-properties-networkmanager-transitgatewaypeering-tag-properties"></a>

`Key`  <a name="cfn-networkmanager-transitgatewaypeering-tag-key"></a>
The tag key.
Constraints: Maximum length of 128 characters.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networkmanager-transitgatewaypeering-tag-value"></a>
The tag value.
Constraints: Maximum length of 256 characters.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
