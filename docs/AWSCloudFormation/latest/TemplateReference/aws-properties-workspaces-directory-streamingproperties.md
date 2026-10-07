---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-streamingproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory StreamingProperties
<a name="aws-properties-workspaces-directory-streamingproperties"></a>

Describes the streaming properties.

## Syntax
<a name="aws-properties-workspaces-directory-streamingproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-streamingproperties-syntax.json"></a>

```
{
  "[GlobalAccelerator](#cfn-workspaces-directory-streamingproperties-globalaccelerator)" : {{GlobalAcceleratorForDirectory}},
  "[StorageConnectors](#cfn-workspaces-directory-streamingproperties-storageconnectors)" : {{[ StorageConnector, ... ]}},
  "[StreamingExperiencePreferredProtocol](#cfn-workspaces-directory-streamingproperties-streamingexperiencepreferredprotocol)" : {{String}},
  "[UserSettings](#cfn-workspaces-directory-streamingproperties-usersettings)" : {{[ UserSetting, ... ]}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-streamingproperties-syntax.yaml"></a>

```
  [GlobalAccelerator](#cfn-workspaces-directory-streamingproperties-globalaccelerator): {{
    GlobalAcceleratorForDirectory}}
  [StorageConnectors](#cfn-workspaces-directory-streamingproperties-storageconnectors): {{
    - StorageConnector}}
  [StreamingExperiencePreferredProtocol](#cfn-workspaces-directory-streamingproperties-streamingexperiencepreferredprotocol): {{String}}
  [UserSettings](#cfn-workspaces-directory-streamingproperties-usersettings): {{
    - UserSetting}}
```

## Properties
<a name="aws-properties-workspaces-directory-streamingproperties-properties"></a>

`GlobalAccelerator`  <a name="cfn-workspaces-directory-streamingproperties-globalaccelerator"></a>
Indicates the Global Accelerator properties.
*Required*: No
*Type*: [GlobalAcceleratorForDirectory](aws-properties-workspaces-directory-globalacceleratorfordirectory.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConnectors`  <a name="cfn-workspaces-directory-streamingproperties-storageconnectors"></a>
Indicates the storage connector used
*Required*: No
*Type*: Array of [StorageConnector](aws-properties-workspaces-directory-storageconnector.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamingExperiencePreferredProtocol`  <a name="cfn-workspaces-directory-streamingproperties-streamingexperiencepreferredprotocol"></a>
Indicates the type of preferred protocol for the streaming experience.
*Required*: No
*Type*: String
*Allowed values*: `TCP | UDP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserSettings`  <a name="cfn-workspaces-directory-streamingproperties-usersettings"></a>
Indicates the permission settings asscoiated with the user.
*Required*: No
*Type*: Array of [UserSetting](aws-properties-workspaces-directory-usersetting.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
