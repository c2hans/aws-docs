---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-connection-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::Connection Tag

Describes a tag.

## Syntax
<a name="aws-properties-networkmanager-connection-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-connection-tag-syntax.json"></a>

```json
{
  "[Key](#cfn-networkmanager-connection-tag-key)" : {{String}},
  "[Value](#cfn-networkmanager-connection-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-networkmanager-connection-tag-syntax.yaml"></a>

```yaml
  [Key](#cfn-networkmanager-connection-tag-key): {{String}}
  [Value](#cfn-networkmanager-connection-tag-value): {{String}}
```

## Properties
<a name="aws-properties-networkmanager-connection-tag-properties"></a>

`Key`  <a name="cfn-networkmanager-connection-tag-key"></a>
The tag key.
Constraints: Maximum length of 128 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[!-~]([ -~]*[!-~])?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-networkmanager-connection-tag-value"></a>
The tag value.
Constraints: Maximum length of 256 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[!-~]([ -~]*[!-~])?$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
