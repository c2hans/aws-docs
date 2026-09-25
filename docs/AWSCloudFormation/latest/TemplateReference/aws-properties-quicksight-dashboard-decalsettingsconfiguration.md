---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-decalsettingsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DecalSettingsConfiguration
<a name="aws-properties-quicksight-dashboard-decalsettingsconfiguration"></a>

Decal settings configuration for a column

## Syntax
<a name="aws-properties-quicksight-dashboard-decalsettingsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-decalsettingsconfiguration-syntax.json"></a>

```
{
  "[CustomDecalSettings](#cfn-quicksight-dashboard-decalsettingsconfiguration-customdecalsettings)" : {{[ DecalSettings, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-decalsettingsconfiguration-syntax.yaml"></a>

```
  [CustomDecalSettings](#cfn-quicksight-dashboard-decalsettingsconfiguration-customdecalsettings): {{
    - DecalSettings}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-decalsettingsconfiguration-properties"></a>

`CustomDecalSettings`  <a name="cfn-quicksight-dashboard-decalsettingsconfiguration-customdecalsettings"></a>
A list of up to 50 decal settings.
*Required*: No
*Type*: Array of [DecalSettings](aws-properties-quicksight-dashboard-decalsettings.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
