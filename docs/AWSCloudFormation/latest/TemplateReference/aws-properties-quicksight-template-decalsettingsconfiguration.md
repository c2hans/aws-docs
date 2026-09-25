---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-decalsettingsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DecalSettingsConfiguration
<a name="aws-properties-quicksight-template-decalsettingsconfiguration"></a>

Decal settings configuration for a column

## Syntax
<a name="aws-properties-quicksight-template-decalsettingsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-decalsettingsconfiguration-syntax.json"></a>

```
{
  "[CustomDecalSettings](#cfn-quicksight-template-decalsettingsconfiguration-customdecalsettings)" : {{[ DecalSettings, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-decalsettingsconfiguration-syntax.yaml"></a>

```
  [CustomDecalSettings](#cfn-quicksight-template-decalsettingsconfiguration-customdecalsettings): {{
    - DecalSettings}}
```

## Properties
<a name="aws-properties-quicksight-template-decalsettingsconfiguration-properties"></a>

`CustomDecalSettings`  <a name="cfn-quicksight-template-decalsettingsconfiguration-customdecalsettings"></a>
A list of up to 50 decal settings.
*Required*: No
*Type*: Array of [DecalSettings](aws-properties-quicksight-template-decalsettings.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
