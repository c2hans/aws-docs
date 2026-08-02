---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-workspacespool-applicationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::WorkspacesPool ApplicationSettings
<a name="aws-properties-workspaces-workspacespool-applicationsettings"></a>

The persistent application settings for users in the pool.

## Syntax
<a name="aws-properties-workspaces-workspacespool-applicationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-workspacespool-applicationsettings-syntax.json"></a>

```
{
  "[SettingsGroup](#cfn-workspaces-workspacespool-applicationsettings-settingsgroup)" : {{String}},
  "[Status](#cfn-workspaces-workspacespool-applicationsettings-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-workspacespool-applicationsettings-syntax.yaml"></a>

```
  [SettingsGroup](#cfn-workspaces-workspacespool-applicationsettings-settingsgroup): {{String}}
  [Status](#cfn-workspaces-workspacespool-applicationsettings-status): {{String}}
```

## Properties
<a name="aws-properties-workspaces-workspacespool-applicationsettings-properties"></a>

`SettingsGroup`  <a name="cfn-workspaces-workspacespool-applicationsettings-settingsgroup"></a>
The path prefix for the S3 bucket where users’ persistent application settings are stored.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_./()!*'-]+$`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-workspaces-workspacespool-applicationsettings-status"></a>
Enables or disables persistent application settings for users during their pool sessions.
*Required*: Yes
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
