---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-workspace-workspacethemeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Workspace WorkspaceThemeConfig
<a name="aws-properties-connect-workspace-workspacethemeconfig"></a>

Contains detailed theme configuration for a workspace, including colors, images, and typography.

## Syntax
<a name="aws-properties-connect-workspace-workspacethemeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-workspace-workspacethemeconfig-syntax.json"></a>

```
{
  "[Palette](#cfn-connect-workspace-workspacethemeconfig-palette)" : {{WorkspaceThemePalette}},
  "[Typography](#cfn-connect-workspace-workspacethemeconfig-typography)" : {{WorkspaceThemeTypography}}
}
```

### YAML
<a name="aws-properties-connect-workspace-workspacethemeconfig-syntax.yaml"></a>

```
  [Palette](#cfn-connect-workspace-workspacethemeconfig-palette): {{
    WorkspaceThemePalette}}
  [Typography](#cfn-connect-workspace-workspacethemeconfig-typography): {{
    WorkspaceThemeTypography}}
```

## Properties
<a name="aws-properties-connect-workspace-workspacethemeconfig-properties"></a>

`Palette`  <a name="cfn-connect-workspace-workspacethemeconfig-palette"></a>
The color palette configuration for the workspace theme.
*Required*: No
*Type*: [WorkspaceThemePalette](aws-properties-connect-workspace-workspacethemepalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Typography`  <a name="cfn-connect-workspace-workspacethemeconfig-typography"></a>
The typography configuration for the workspace theme.
*Required*: No
*Type*: [WorkspaceThemeTypography](aws-properties-connect-workspace-workspacethemetypography.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
