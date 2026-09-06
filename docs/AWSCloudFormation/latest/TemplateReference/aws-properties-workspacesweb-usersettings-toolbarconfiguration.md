---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-usersettings-toolbarconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::UserSettings ToolbarConfiguration
<a name="aws-properties-workspacesweb-usersettings-toolbarconfiguration"></a>

The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.

## Syntax
<a name="aws-properties-workspacesweb-usersettings-toolbarconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-usersettings-toolbarconfiguration-syntax.json"></a>

```
{
  "[HiddenToolbarItems](#cfn-workspacesweb-usersettings-toolbarconfiguration-hiddentoolbaritems)" : {{[ String, ... ]}},
  "[MaxDisplayResolution](#cfn-workspacesweb-usersettings-toolbarconfiguration-maxdisplayresolution)" : {{String}},
  "[ToolbarType](#cfn-workspacesweb-usersettings-toolbarconfiguration-toolbartype)" : {{String}},
  "[VisualMode](#cfn-workspacesweb-usersettings-toolbarconfiguration-visualmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspacesweb-usersettings-toolbarconfiguration-syntax.yaml"></a>

```
  [HiddenToolbarItems](#cfn-workspacesweb-usersettings-toolbarconfiguration-hiddentoolbaritems): {{
    - String}}
  [MaxDisplayResolution](#cfn-workspacesweb-usersettings-toolbarconfiguration-maxdisplayresolution): {{String}}
  [ToolbarType](#cfn-workspacesweb-usersettings-toolbarconfiguration-toolbartype): {{String}}
  [VisualMode](#cfn-workspacesweb-usersettings-toolbarconfiguration-visualmode): {{String}}
```

## Properties
<a name="aws-properties-workspacesweb-usersettings-toolbarconfiguration-properties"></a>

`HiddenToolbarItems`  <a name="cfn-workspacesweb-usersettings-toolbarconfiguration-hiddentoolbaritems"></a>
The list of toolbar items to be hidden.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxDisplayResolution`  <a name="cfn-workspacesweb-usersettings-toolbarconfiguration-maxdisplayresolution"></a>
The maximum display resolution that is allowed for the session.
*Required*: No
*Type*: String
*Allowed values*: `size4096X2160 | size3840X2160 | size3440X1440 | size2560X1440 | size1920X1080 | size1280X720 | size1024X768 | size800X600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolbarType`  <a name="cfn-workspacesweb-usersettings-toolbarconfiguration-toolbartype"></a>
The type of toolbar displayed during the session.
*Required*: No
*Type*: String
*Allowed values*: `Floating | Docked`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualMode`  <a name="cfn-workspacesweb-usersettings-toolbarconfiguration-visualmode"></a>
The visual mode of the toolbar.
*Required*: No
*Type*: String
*Allowed values*: `Dark | Light`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
