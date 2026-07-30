---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appconfig-extensionassociation-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppConfig::ExtensionAssociation Tag
<a name="aws-properties-appconfig-extensionassociation-tag"></a>

Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.

## Syntax
<a name="aws-properties-appconfig-extensionassociation-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appconfig-extensionassociation-tag-syntax.json"></a>

```
{
  "[Key](#cfn-appconfig-extensionassociation-tag-key)" : {{String}},
  "[Value](#cfn-appconfig-extensionassociation-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-appconfig-extensionassociation-tag-syntax.yaml"></a>

```
  [Key](#cfn-appconfig-extensionassociation-tag-key): {{String}}
  [Value](#cfn-appconfig-extensionassociation-tag-value): {{String}}
```

## Properties
<a name="aws-properties-appconfig-extensionassociation-tag-properties"></a>

`Key`  <a name="cfn-appconfig-extensionassociation-tag-key"></a>
A key and optional value to help you categorize resources.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-appconfig-extensionassociation-tag-value"></a>
An optional tag value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
